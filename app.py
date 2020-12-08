from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
from werkzeug import secure_filename
from preprocessing import preprocess
from model import model_func
from predict import predict
import pandas as pd
import os

app = Flask("__name__")

@app.route('/', methods=["GET"])
def index():
    if request.method == "GET":
        return "Alive"
    else:
        return "Server not working"

# @app.route('/predict/<uuid>', methods=["POST", "GET"])
@app.route('/predict', methods=["POST", "GET"])
def predict_page():
    # content = request.get_json()
    if request.method == 'POST':

        response = {}
        original_json_df = request.json
        # we saved new json file inside Datasets folder. 
        # Now, we call it with process function and then we pass it through our model.
        cleaned_json_df = preprocess(original_json_df)
        if not cleaned_json_df:
            response["error"] = "ERROR:no input json"
        
        model = model_func()
        y_pred_new = predict(cleaned_json_df, model) 
        response["prediction"] = y_pred_new

        return jsonify(response)
    else:
        return jsonify({
            "error": "no input json"
        })

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')