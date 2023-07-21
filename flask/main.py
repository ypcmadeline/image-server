from flask import Flask, request, jsonify, send_file
from loguru import logger
import json
import re


app = Flask(__name__)


@app.route('/', methods=['GET'])
def test():
    return send_file('test.jpeg', mimetype='image/jpeg') 


@app.route('/', methods=['POST'])
def postdata():
    f = open('result.json', 'r')
    json_data = json.load(f)
    f.close()
    res = json_data['result']
    data = request.form.get('name')
    x = re.search(rf"{data} *= *([0-9]+.[0-9]+)", res)
    if not x:
        return 'Not Found'
    else: 
        return 'Result: ' + x.group()


@app.route('/test', methods=['GET'])
def getimage():
    return send_file('test.jpeg', mimetype='image/jpeg') 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
