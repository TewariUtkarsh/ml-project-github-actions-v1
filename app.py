from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from wsgiref import simple_server
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def index():

    return "Simple Flask Hello World App !!"

port = os.getenv("PORT", 5000)
if(__name__ == '__main__'):
    
    host = '0.0.0.0'

    httpd = simple_server.make_server(host, port, app)

    httpd.serve_forever()

    # app.run(debug=True)