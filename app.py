from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from preprocessing import preprocess
from model import model_func
from predict import predict
import pandas as pd
import os

app = Flask("__name__")
port = int(os.environ.get("PORT", 5000))

@app.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        return "Alive"
    else:
        return "Server not working"

@app.route('/predict', methods=["POST", "GET"])
def predict_page():
    if request.method == 'POST':

        response = {}
        json_file = request.json
        # we saved new json file inside Datasets folder. 
        # Now, we call it with process function and then we pass it through our model.
        cleaned_json_df = preprocess(json_file)
        
        model = model_func()
        y_pred_new = predict(cleaned_json_df, model) 
        y_pred_new = y_pred_new.tolist()
        response["prediction"] = y_pred_new

        return jsonify(response)
    else:
        return 
        response['error'] = "no input json"
        jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
