from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Flask Frontend'

@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    res = requests.post('http://fastapi-service:8000/predict', json=input_data)
    return jsonify(res.json())
