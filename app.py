from flask import Flask, render_template, request, redirect

app = Flask("__name__")


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":    
        return render_template('predict.html')#, input_json_data)
        pass
    else:
        return render_template('index.html') #, error_message=error_message -> error_message_comming_from.preprocessing.preprocess())
        pass


# @app.route('/predict/<uuid>', methods=["POST", "GET"])
@app.route('/predict', methods=["POST", "GET"])
def predict_page():
    # content = request.get_json()
    price_predicted= '5'
    return render_template("predict.html", price_predicted='price_predicted' )



if __name__ == "__main__":
    app.run(debug=True)
