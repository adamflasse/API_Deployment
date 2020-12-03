"""
This return the model that we create by Linear Regression,
It take the data set, and returns the model
param: cleaned_data is the cleaned csv file
"""



import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

def Model_Prediction(cleaned_data):

    #Reading the clened csv file
    df = pd.read_csv("cleaned_data.csv")
    # #I can use immediately the following to get the cleaned df
    # f= Data_Cleaning_Exploration_Visualisation(df)

    # # extract only the features that will be used in LinearRegression
    X= df.drop(['price'], axis=1).values
    y = df['price'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=300, test_size=0.2)

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_test_predict = model.predict(X_test)
    print(f"the r2 score for test data={r2_score(y_test, y_test_predict): .3f}")
    #store the model in pickle file
    return(pickle.dump(model, open('model/final_prediction.pickle', 'wb')))