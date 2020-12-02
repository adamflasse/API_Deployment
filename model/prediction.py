#import sklearn modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import cross_val_score
import pandas as pd

final_df = pd.read_csv('../Datasets/cleaned_df.csv')

#prepare x and y variables for the model
x = final_df.drop(['price','price_area','house_is', 'divisor', 'coeff', 'postcode'], axis=1)    
# , 'land_surface', 'postcode'
y = final_df['price']    

#transform columns
column_trans = make_column_transformer((OneHotEncoder(), ['swimming_pool_has','open_fire', 'building_state_agg', 'property_subtype']), remainder='passthrough')
X = column_trans.fit_transform(x)

#split into test and train data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#create and apply linear regression model
linreg = LinearRegression().fit(X_train, y_train)
y_pred = linreg.predict(X_test)

print(linreg.score(X_test, y_test))