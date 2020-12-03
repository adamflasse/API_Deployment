import pandas as pd
import sys
sys.path.append("..")
from model import model_func

def predict(json_file_name, linreg):
    new_df = pd.read_json(json_file_name, orient='index')
    new_df[['GOOD', 'JUST RENOVATED', 'NEW',
       'TO REBUILD', 'TO RENOVATE', 'Apartment', 'House', 'Other']] = 0
    col1 = new_df['property_subtype'].values[0]
    col3 = new_df['building_state_agg'].values[0]
    new_df[col1] = 1
    new_df[col3] = 1
    new_df.drop(['property_subtype', 'building_state_agg'], axis=1, inplace=True)
    new_df = new_df.astype('float64')
    X_test_new = new_df.values
    y_pred_new = linreg.predict(X_test_new)

    return y_pred_new[0]


json_file_name = 'emre.json'
linreg = model_func()
results = predict(json_file_name, linreg)
print(results)



