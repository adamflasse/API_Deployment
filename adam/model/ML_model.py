import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import ensemble
import pickle

# Gather Data
df = pd.read_csv('/Users/adamflasse/Development/projets/API_deployment/assets/model.csv')

# Prediction target
y = df.price

# Choose features
features = ['postcode', 'area', 'rooms_number',
       'garden', 'garden_area', 'terrace', 'terrace_area', 'land_surface','open_fire', 'swimming_pool_has', 'equipped_kitchen_has', 'furnished' ,'property_subtype_Apartment',
       'property_subtype_House', 'property_subtype_Other', 'building_state_agg_GOOD',
       'building_state_agg_JUST RENOVATED', 'building_state_agg_NEW',
       'building_state_agg_TO REBUILD', 'building_state_agg_TO RENOVATE']

X = df[features]


# Dividing the data into train/test
feature_train, feature_test, label_train, label_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

# Applying machine learning algorithm

model = ensemble.GradientBoostingRegressor(
    n_estimators=400, max_depth=5, min_samples_split=7, learning_rate=0.1, loss='ls')

model.fit(X, y)



def predict(new_features):
    """ We use this function here so it can be called from the prediction module,
    the argument here is to pass the new features in order to predict the price accordingly"""
    pickle.dump(model, open('/Users/adamflasse/Development/projets/API_deployment/assets/model.pkl','wb'))

    modele = pickle.load(open('/Users/adamflasse/Development/projets/API_deployment/assets/model.pkl','rb'))
    price = modele.predict(new_features)
    return price[0]
