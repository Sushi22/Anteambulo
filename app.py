from flask import Flask,request, jsonify
import requests
from graph import debug_graph
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/getAll', methods=['GET'])
def get_nodes():
    return jsonify({"data": debug_graph.graph["issues"]})


@app.route('/getAnswer', methods=['GET'])
def get_node_response():
    param_value = request.args.get('selected_option')
    print("param: ", param_value)
    if param_value not in debug_graph.graph:
        return jsonify({"data": [], "isTerminal": True})
    options_list = debug_graph.graph[param_value]
    print("option list: ", options_list)
    response_list = []
    for val in options_list:
        print("val: ", val)
        result = val.split(",")
        obj = {
        "text" : result[0],
        "listLinks" : result[1].split("$") if len(result) > 1 else []
        }
        response_list.append(obj)
    print(options_list)
    return jsonify({"data" : response_list, "isTerminal": False})


@app.route('/addIssueNode', methods=['POST'])
def add_issue_node():
    body_json = request.json
    debug_graph.add_edge("issues",body_json["data"])

@app.route('/addOptionNode', methods=['POST'])
def add_option_node():
    body_json = request.json
    debug_graph.add_edge(body_json['key'],body_json['value'])
    
    

if __name__ == '__main__':
    app.run(debug=True)





































