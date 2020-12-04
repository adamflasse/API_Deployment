from flask import Flask, render_template, flash, request, redirect, url_for
from werkzeug import secure_filename
from preprocessing import preprocess
from model import model_func
from predict import predict
import pandas as pd
import os

# '/path/to/the/uploads' | os.getcwd() == current directory
UPLOAD_FOLDER = os.getcwd()+'/Datasets'
ALLOWED_EXTENSIONS = {'json'}

# I copied this upload file section from flask documentation
# https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
app = Flask("__name__")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":  
        # if it is post, you route it to "/prediction"  
        return redirect(url_for('predict_page'))
    else:
        return render_template('index.html') #, error_message=error_message -> error_message_comming_from.preprocessing.preprocess())

# toallow only json file 
def allowed_file(filename):
    return '.' in filename and \
       filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/predict/<uuid>', methods=["POST", "GET"])
@app.route('/prediction', methods=["POST", "GET"])
def predict_page():
    # content = request.get_json()
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # we saved new json file inside Datasets folder. 
        # Now, we call it with process function and then we pass it through our model.
            compatible_df = preprocess(file.filename)
            linreg = model_func()
            y_pred_new = predict(compatible_df, linreg) 
            y_pred_new = str(y_pred_new)

            return render_template("predict.html", price_predicted=y_pred_new ) 
    else:
        return '''
                <html>
                    <body>
                        <form enctype = "multipart/form-data" method = "post"> 
                            <p>Upload File: <input type = "file" name = "file" /> 
                            <p><input type = "submit" value = "Upload" /></p> 
                        </form>
                    </body>
                </html>
                '''

if __name__ == "__main__":
    app.run(debug=True)