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
    else:
        var = 'Please make a POST request with a JSON object of this format: { "property-type": "APARTMENT" | "HOUSE" | "OTHERS", "area": int, "rooms-number": int, "zip-code": int, "garden": Optional[bool], "garden-area": Optional[int], "terrace": Optional[bool], "terrace-area": Optional[int], "facades-number": Optional[int], "building-state": Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"], "equipped-kitchen": Optional[bool], "furnished": Optional[bool], "open-fire": Optional[bool], "swimmingpool": Optional[bool], "land-area": Optional[int], "full-address": Optional[str] }'

        return var

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
