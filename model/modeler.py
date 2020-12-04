import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#import sklearn modules
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.model_selection import cross_val_score
import os

def model_func():
    print(os.getcwd())
    data = pd.read_csv('Datasets/def_dataset.csv')

    df = data.drop(['source', 'garden', 'terrace', 'basement'], axis=1)

    df = df[df['price'].notna()]        # remove some records with null values
    df = df[df['area'].notna()]         # df = df[df['rooms_number'].notna()]
    df = df[df['building_state_agg'].notna()]

    # Make a dictionary to only have Apartments, houses and others in the property subtype
    dico = {'MIXED_USE_BUILDING': 'Other', 'APARTMENT_BLOCK': 'Apartment', 'HOUSE': 'House', 'EXCEPTIONAL_PROPERTY': 'Other', 'MANSION': 'House', 'VILLA': 'House', 'OTHER_PROPERTY': 'Other', 'TOWN_HOUSE' : 'House', 'COUNTRY_COTTAGE': 'House', 'BUNGALOW': 'House', 'FARMHOUSE': 'House', 'MANOR_HOUSE': 'House', 'APARTMENT': 'Apartment', 'FLAT_STUDIO': 'Apartment', 'LOFT': 'Apartment', 'DUPLEX': 'Apartment', 'PENTHOUSE': 'Apartment', 'GROUND_FLOOR': 'Other', 'KOT': 'Other', 'TRIPLEX': 'Apartment', 'SERVICE_FLAT': 'Apartment' }

    # Make a dictionary to re-work the names of the building_state column
    dico_building_state = {'GOOD': 'GOOD', 'TO_RENOVATE':'TO RENOVATE', 'JUST_RENOVATED': 'JUST RENOVATED',  'AS_NEW': 'NEW', 'TO_RESTORE': 'TO REBUILD'}

    df['building_state_agg'].replace(dico_building_state, inplace= True)
    df['property_subtype'].replace(dico, inplace= True)

    def price_area(df1):    
        df1['coeff'] = np.where(df1['land_surface'] + df1['garden_area'] < 250, 2, np.where(df1['land_surface'] + df1['garden_area'] < 1000, 4, np.where(df1['land_surface'] + df1['garden_area'] < 5000, 8, np.where(df1['land_surface'] + df1['garden_area'] < 10000, 12, 16))))        
        df1['divisor'] = df1['area'] + df1['terrace_area'] + df1['garden_area'] / df1['coeff'] + df1['land_surface']/df1['coeff']
        df1['price_area'] = df1['price']/df1['divisor']
        f = ['open_fire', 'swimming_pool_has', 'furnished', 'equipped_kitchen_has']
        c = [-5000, -15000, -10000, -5000]
        for i in range(len(f)):
            df1['price_area'] += np.where(df1[f[i]] == True, c[i]/df1['divisor'], 0)
        factors = ['AS_NEW', 'JUST_RENOVATED', 'TO_RENOVATE', 'TO_RESTORE']
        rate = [-600, -300, 300, 600]
        for i in range(len(factors)):
            df1['price_area'] += np.where(df1['building_state_agg'] == factors[i],
                                  (rate[i]*(df1['area'] + df1['terrace_area'])/df1['divisor']), 0)
        return df1

    df = price_area(df)
    df = df[df['price_area']<20000]     # outliers for price_area

    df2 = df[(df['price_area'] > 500) & (df['price_area']<5500) & (df['rooms_number']<6)   & (df['area']<500)]

    final_df = df2.dropna()

    #prepare x and y variables for the model
    x = final_df.drop(['price','price_area','house_is', 'divisor', 'coeff', 'postcode'], axis=1)  
    # , 'land_surface', 'postcode'
    y = final_df['price']    

    #transform columns
    def dummy(col, df):
        col_enc = pd.get_dummies(df[col])
        df = pd.concat([df, col_enc], axis=1)   
        df.drop([col], axis=1, inplace=True)
        return df

    x_end = dummy('building_state_agg', x)
    x_end = dummy('property_subtype', x_end)
    x_end.columns
    X = x_end.values

    #split into test and train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

    #create and apply linear regression model
    linreg = LinearRegression().fit(X_train, y_train)   
    return linreg