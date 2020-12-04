import pandas as pd
import pickle

def predict(cleaned_json_df, model):

    X_new_json = cleaned_json_df.values

    pickle.dump(model, open('Datasets/model.pkl','wb'))
    modele = pickle.load(open('Datasets/model.pkl','rb'))

    y_pred_new = modele.predict(X_new_json)

    return y_pred_new





