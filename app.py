from flask import Flask,request, jsonify
import requests
from graph import debug_graph


app = Flask(__name__)


@app.route('/getAll', methods=['GET'])
def get_nodes():
    return jsonify({"data": debug_graph.graph["issues"]})


@app.route('/getAnswer', methods=['GET'])
def get_node_response():
    param_value = request.args.get('selected_option')
    return jsonify({"data" : debug_graph.graph[param_value]})

@app.route('/addIssueNode', methods=['POST'])
def add_issue_node():
    body_json = request.json
    debug_graph.add_edge("issues",body_json["data"])

@app.route('/addOptionNode', methods=['POST'])
def add_option_node();
    body_json = request.json
    debug_graph.add_edge(body_json['key'],body_json['value'])
    
    

if __name__ == '__main__':
    app.run(debug=True)

