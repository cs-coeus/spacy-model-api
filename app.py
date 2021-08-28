import os
from dotenv import dotenv_values
from flask import Flask, jsonify, request

is_production = os.environ.get('FLASK_ENV') == 'production'
authentication_token = os.environ.get('AUTHORIZATION_KEY')
config = dotenv_values(".env")

app = Flask(__name__)


@app.route('/healthcheck')
def health_check():
    return 'OK'


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            # TODO: Replace this with actual model.predict() and return a proper response
            return jsonify({"result": data})
    return jsonify({"error": "Data is invalid or not exist"}), 400
