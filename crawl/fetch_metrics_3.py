import pandas as pd
import requests
from azure.storage.blob import BlobServiceClient, generate_container_sas, ContainerSasPermissions
from time import strftime, localtime
import datetime
import pymongo

load_dotenv()
api_key = os.environ.get("API_KEY")

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["anteambulo"]


class DashboardIds:
    SRE_TRAFFIC_FLOW_AND_HEALTH = "zuhbR77Vk"


class QueryNotFoundException(Exception):
    pass

load_dotenv()
api_key = os.environ.get("API_KEY")


def fetch_dashboard_json(dashboard_uid):
    url  = "https://grafana-k8s-ci.myntra.com/api/dashboards/uid/"
    url = url + dashboard_uid
    response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})
    return response.json()


def fetch_query_exp(json_model):
    exp_list = []
    for panel in json_model.get("dashboard").get("panels"):
        targets = panel.get("targets")
        if targets is None:
            continue
        for target in targets:
            exp = target.get("expr")
            exp_list.append(exp)
    return exp_list


def check_if_query_exists(expr):
    collection = db["query"]
    mongo_query = {"expr": expr}
    existing_document = collection.find_one(mongo_query)
    if existing_document:
        print("Document already exists in MongoDB")
        return True
    else:
        print("Document does not exist in MongoDB")
        return False


def query_datasource(query, start, end):
    ## fill the query params with the right value

    if not check_if_query_exists(query):
        print("Hey... Looks like the model is not trained on query: ", query)
        raise QueryNotFoundException

    ## catch this exception in the parent method and ask the user would they like to train the model on complete dashboard queries
    ## future scope: Option to train the model on single query
    url = "https://thanos-k8s-ci.myntra.com/api/v1/query_range"
    param = {
        "query": query,
        "start": start,
        "end": end
    }
    response = requests.get(url, param)
    df = pd.DataFrame
    timestamp = []
    data = []
    for value in response.get("data").get("result")[0].get("values"):
        timestamp.append(value[0])
        data.append(int(value[1]))
    timestamp = pd.Series(timestamp)
    data = pd.Series(data)
    df["timestamp"] = timestamp
    df["data"] = data
    return df


# json_model = fetch_dashboard_json(DashboardIds.SRE_TRAFFIC_FLOW_AND_HEALTH)
# exp_list = fetch_query_exp(json_model)
# print("exp list: ", exp_list)


def get_query_id(query_expr):
    # maintain a mongo collection with {query_id, query_expr} document
    # call mongodb and fetch the queryId for corresponding query
    collection = db["query"]
    mongo_query = {"expr": query_expr}
    document = collection.find_one(mongo_query)
    if document is None:
        raise QueryNotFoundException
    return document.get("id")


def get_reference_data(query_id):
    # maintain a collection with {query_id, reference_data} document
    # reference data is dataframe with first column as timestamp and other columns as data series for stable times
    collection = db["query"]
    mongo_query = {"id": query_id}
    query_doc = collection.find_one(mongo_query)
    blob_url = query_doc.get("reference_data_url")
    reference_data = pd.read_csv(blob_url)


def get_dashboard_variables(dashboard_id):
    json_model = fetch_dashboard_json(dashboard_id)
    expr_list = fetch_query_exp(json_model)
    variables = []
    for expr in expr_list:
        variables.extend(get_expr_variables(expr))
    return list(set(variables))


def find_anomaly(dashboard_id, start, end, variables):
    json_model = fetch_dashboard_json(dashboard_id)
    expr_list = fetch_query_exp(json_model)
    for expr in expr_list:
        query = expr # update the expr with variables value
        concerned_df = query_datasource(query, start, end)
        query_id = get_query_id(query)
        collection = db["query"]
        query_doc = collection.find_one({"id": query_id})
        blob_url = query_doc.get("reference_data_url")
        reference_df = pd.read_csv(blob_url)
        df = create_dataframe_for_correlation(concerned_df, reference_df, start, end)
        correlation_matrix = get_correlation_matrix(df)
        anomaly_in_correlation_matrix(correlation_matrix)


def anomaly_in_correlation_matrix(matrix):
    for sample in matrix:
        for coeff in sample:
            if coeff < 0.9:
                return True
    return False


def create_dataframe_for_correlation(concerned_df, reference_df, start, end):
    start_time = datetime.datetime.fromtimestamp(start).time()  #strftime('%Y-%m-%d %H:%M:%S', localtime(start))
    end_time = datetime.datetime.fromtimestamp(end).time()
    df = concerned_df
    date_dic = {}
    for row in reference_df.iterrows():
        data = row["data"]
        timestamp = row["timestamp"]
        datetime_ = datetime.datetime.fromtimestamp(timestamp)
        date_ = datetime_.date()
        time_ = datetime_.time()
        if start_time <= time_ <= end_time:
            if date_ in date_dic:
                ser = date_dic[date_]
                ser.append(pd.Series([data]))
                date_dic[date_] = ser
            else :
                date_dic[date_] = pd.Series([data])

    for key, value in date_dic:
        df[key] = value
    return df


def get_correlation_matrix(df):
    num_of_samples = len(df.index)
    batch_size = 100
    matrix = []
    for ind in range(0, num_of_samples, batch_size):
        batch_df = df[ind: min(ind + batch_size, num_of_samples)]
        corr_matrix = batch_df.corr(method="pearson")
        matrix.append(corr_matrix[0][1:])

    return matrix


def get_expr_variables(query_expr):
    variables = []    # find list of variables
    return variables


def get_expr_variables(dashboard_id):
    json_model = fetch_dashboard_json(dashboard_id)
    expr_list = fetch_query_exp(json_model)
    # find list of variables


def train_model(dashboard_id, start, end, variables):
    json_model = fetch_dashboard_json(dashboard_id)
    expr_list = fetch_query_exp(json_model)
    for expr in expr_list:
        query = expr   # put the variable values in expr
        df = query_datasource(query, start, end)
        query_id = get_query_id(query)
        file_path = f'{query_id}.csv'
        blob_url = upload_to_blob(df, file_path)
        collection = db["query"]
        mongo_query = {
            "id": query_id
        }
        query_doc = collection.find_one(mongo_query)
        query_doc["reference_data_url"] = blob_url
        collection.update_one(mongo_query, {"$set": query_doc})


def upload_to_blob(data, file_path, container_name="imagedext", account_url="https://campa.blob.core.windows.net", access_key="DRVx7N/SpCv8XofVYvIW+3nfJFDYIH37KfwAolqR09BxWIYolQnxghozBCMqubcz7+q3O40LpNOYs777N1Xcdg=="):
    data = data.to_csv(encoding="utf-8", index=False)
    block_blob_service = BlobServiceClient(account_url=account_url, credential=access_key)
    blob_client = block_blob_service.get_blob_client(container=container_name, blob=file_path)
    blob_client.upload_blob(data=data)
    return blob_client.url

# queryId -> data series