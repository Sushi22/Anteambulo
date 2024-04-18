from fetch_metrics import get_dashboard_variables, train_model, fetch_dashboard_json, fetch_query_exp, create_and_insert_query
from fetch_metrics import DashboardIds


# variables = get_dashboard_variables(DashboardIds.SRE_TRAFFIC_FLOW_AND_HEALTH)
# json_model = fetch_dashboard_json(DashboardIds.SRE_TRAFFIC_FLOW_AND_HEALTH)
# print("expr list: ", fetch_query_exp(json_model))


variables = {
    "cluster" : "pac-sfcluster01",
    "namespace": "flock"
}
train_model(DashboardIds.SRE_TRAFFIC_FLOW_AND_HEALTH, 1713378600, 1713382200, variables)

query = 'sum(haproxy_backend_http_responses_total{proxy=~\'flock.*\', prom="ingress", cluster="pac-sfcluster01",code=~"1xx|2xx|3xx|4xx"})/sum(haproxy_backend_http_responses_total{proxy=~\'flock.*\', prom="ingress", cluster="pac-sfcluster01"}) * 100'

print("query id: ", create_and_insert_query(query))