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
        
        # Now, we call json data with process function and then we pass it through our model.
        cleaned_json_df = preprocess(json_file)

        if type(cleaned_json_df)==str:
            response["error"] = cleaned_json_df
            return jsonify(response)

        model = model_func()
        y_pred_new = predict(cleaned_json_df, model) 
        y_pred_new = y_pred_new.tolist()
        response["prediction"] = y_pred_new

        return jsonify(response)
    
    elif request.method == 'GET':
        return """<xmp>
            Here is the data format for the POST request:
            {
            'area': int,
            'property-type': 'APARTMENT' | 'HOUSE' | 'OTHERS',
            'rooms-number': int,
            'zip-code': int,
            'garden' : Optional[bool],
            'equipped-kitchen': Optional[bool],
            'furnished': Opional[bool],
            'terrace': Optional[bool],
            'facades-number': Optional[int]
            }
            </xmp>"""
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
