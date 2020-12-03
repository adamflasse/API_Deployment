import pandas as pd
import sys
sys.path.append("..")
from preprocessing import preprocess
from model import model_func

def predict(new_df, linreg):
    #new_df = pd.read_json(json_file_name, orient='index')
    new_df[['GOOD', 'JUST RENOVATED', 'NEW',
       'TO REBUILD', 'TO RENOVATE', "APARTMENT", "HOUSE", "OTHERS"]] = 0
    col1 = new_df['property_subtype'].values[0]
    col3 = new_df['building_state_agg'].values[0]
    new_df[col1] = 1
    new_df[col3] = 1
    new_df.drop(['property_subtype', 'building_state_agg'], axis=1, inplace=True)
    new_df = new_df.astype('float64')
    X_test_new = new_df.values
    y_pred_new = linreg.predict(X_test_new)
    
    return y_pred_new

compatible_df = preprocess()
linreg = model_func()
y_pred_new = predict(compatible_df, linreg)
print(y_pred_new)



