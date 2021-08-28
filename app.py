import os
from dotenv import dotenv_values
from flask import Flask, jsonify, request

from models.model import ModelSpacy

is_production = os.environ.get('FLASK_ENV') == 'production'
authentication_token = os.environ.get('AUTHORIZATION_KEY')
config = dotenv_values(".env")

model = ModelSpacy()
app = Flask(__name__)


@app.route('/healthcheck')
def health_check():
    return 'OK'


@app.route('/predict/sentences/count', methods=['POST'])
def predict_pos():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.get_amount_of_sentences(data)
                return jsonify({"result": result})
            except:
                return jsonify({"error": "Data format wrong"}), 400
    return jsonify({"error": "Data is invalid or not exist"}), 400


@app.route('/predict/pos', methods=['POST'])
def predict_pos():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.get_part_of_speech_dictionary(data)
                return jsonify({"result": result})
            except:
                return jsonify({"error": "Data format wrong"}), 400
    return jsonify({"error": "Data is invalid or not exist"}), 400


@app.route('/predict/noun-chunks', methods=['POST'])
def predict_noun_chunks():
    if request.method == 'POST' and request.json is not None:
        if is_production:
            token = request.headers.get('Authorization').split(' ')[1]
            if token != authentication_token:
                return jsonify({"error": "Unauthorized request"}), 403
        data = request.json['data']
        if data is not None:
            try:
                result = model.get_noun_chunk_array(data)
                return jsonify({"result": result})
            except:
                return jsonify({"error": "Data format wrong"}), 400
    return jsonify({"error": "Data is invalid or not exist"}), 400
