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


@app.route('/addNode', methods=['POST'])
def add_node

    

if __name__ == '__main__':
    app.run(debug=True)
    get_nodes()


