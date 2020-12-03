

######## import packages

from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from flask_session import Session
import requests

# import preprocess data function from preprocessing folder
from preprocessing.cleaning_data import preprocess

# print shape of Datasets
print(preprocess('./preprocessing/def_dataset.csv'))

"""
This answers the following question:
#1.  Route to check if the server runs
GET /status -> "Alive!"

#2. Route to login
POST /login -> "Login success for user {USER_NAME_HERE} with password of length: {PASSWORD_LENGTH_HERE}!"
body: {
    username: <USER_NAME_HERE>
    password: <PASSWORD_HERE>
}

#3. Route that returns the prediction
GET /predict/<seller_avaible:int>/<month:str>/<customer_visiting_website:int> -> Prediction (int between 2000 and 5000)
"""

######## import packages

from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session


app=Flask(__name__)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem" #to store data about our server only
Session(app)


################## #1.  Route to check if the server runs, GET /status -> "Alive!"
# Get is only enter, we do not need to do anything

# #I am at the home page, then I go immediately to status page)
# @app.route('/')
# def hello():
#     return (redirect(url_for('Status'))) #go immediately to the status

#this is a welcome page that I have 3 button on it
@app.route('/')
def hello():
    return render_template("Welcome_page_1.html")

@app.route('/status')
def Status_page():
    return render_template("Status_page_1.html")



@app.route('/predict/<uuid>', methods=["POST", "GET"])
#@app.route('/predict', methods=["POST", "GET"])
def Predict_page(uuid):
    content = request.get_json()
    result=int(5)
    return render_template("Predict_page_1.html", result=result )

# def LogIn_page():
#     _username="";_password=""; result="";x=""
#     if request.method == 'POST':
#         # # Retrieve the HTTP POST request parameter value from 'request.form' dictionary
#         _username = request.form.get("user")
#         _password = request.form.get("password")
#
#     if len(_password)==6:
#         result="Success"
#     else:
#         result="Not Success"
#     return ()



if __name__=="__main__":
    app.run(debug=True)
