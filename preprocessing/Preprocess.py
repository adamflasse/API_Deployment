"""
this generates a preprocesed data and preprocessed json file
"""
from Cleaner import Cleaner_SalesData
import json

def Processed_JSON(url_json):


    preprocessed_dict=Cleaner_SalesData(url_json)
    r=preprocessed_dict.cleaning_feature()
    #print(r)
    #write
    with open("preprocessed_data.json", "w") as p1:
        json.dump(r, p1)

    # If we want to load the preprocessed data that is stored in JSON
    data_processed = json.load(open('preprocessed_data.json'))
    print(data_processed )
    z={'0': {'area': 300, 'rooms-number': 2, 'zip-code': 1050, 'land-area': 200, 'garden': True, 'garden-area': 100, 'equipped-kitchen': True, 'swimmingpool': False, 'furnished': True, 'open-fire': True, 'terrace': False, 'terrace-area': 0, 'facades-number': 2, 'property-type_APARTMENT': 1, 'property-type_2': 0.0, 'property-type_3': 0.0, 'building-state_NEW': 1, 'building-state_2': 0.0, 'building-state_3': 0.0, 'building-state_4': 0.0, 'building-state_5': 0.0}}


    features=z["0"]
    testing_features=[]
    testing_features.append(features['area'])
    testing_features.append(features['rooms-number'])
    testing_features.append(features['zip-code'])
    testing_features.append(features['land-area'])
    testing_features.append(features['garden'])
    testing_features.append(features['garden-area'])
    testing_features.append(features['equipped-kitchen'])
    testing_features.append(features['swimmingpool'])
    testing_features.append(features['furnished'])
    testing_features.append(features['open-fire'])
    testing_features.append(features['terrace'])
    testing_features.append(features['terrace-area'])
    testing_features.append(features['facades-number'])

    if 'property-type_APARTMENT' in features:
        testing_features.append(features['property-type_APARTMENT'])
        testing_features.append(features['property-type_2'])
        testing_features.append(features['property-type_3'])
    elif 'property-type_HOUSE' in features:
        testing_features.append(features['property-type_2'])
        testing_features.append(features['property-type_HOUSE'])
        testing_features.append(features['property-type_3'])
    elif 'property-type_OTHERS' in features:
        testing_features.append(features['property-type_2'])
        testing_features.append(features['property-type_3'])
        testing_features.append(features['property-type_OTHERS'])
    else:
        testing_features.append(0)
        testing_features.append(0)
        testing_features.append(0)

    if 'building-state_NEW' in features:
        testing_features.append(features['building-state_NEW'])
        testing_features.append(features['building-state_2'])
        testing_features.append(features['building-state_3'])
        testing_features.append(features['building-state_4'])
        testing_features.append(features['building-state_5'])
    elif 'building-state_GOOD' in features:
        testing_features.append(features['building-state_2'])
        testing_features.append(features['building-state_GOOD'])
        testing_features.append(features['building-state_3'])
        testing_features.append(features['building-state_4'])
        testing_features.append(features['building-state_5'])

    elif 'building-state_TO RENOVATE' in features:
        testing_features.append(features['building-state_2'])
        testing_features.append(features['building-state_3'])
        testing_features.append(features['building-state_TO RENOVATE'])
        testing_features.append(features['building-state_4'])
        testing_features.append(features['building-state_5'])

    elif 'building-state_JUST RENOVATED' in features:
        testing_features.append(features['building-state_2'])
        testing_features.append(features['building-state_3'])
        testing_features.append(features['building-state_4'])
        testing_features.append(features['building-state_JUST RENOVATED'])
        testing_features.append(features['building-state_5'])

    elif 'building-state_TO REBUILD' in features:
        testing_features.append(features['building-state_2'])
        testing_features.append(features['building-state_3'])
        testing_features.append(features['building-state_4'])
        testing_features.append(features['building-state_5'])
        testing_features.append(features['building-state_TO REBUILD'])

    else:
        testing_features.append(0)
        testing_features.append(0)
        testing_features.append(0)
        testing_features.append(0)
        testing_features.append(0)

    return(testing_features)

if __name__=="__main__":
    #you can specify
    url_json = 'input_data.json'
    testing_features=Processed_JSON(url_json)


    #
    # # If we want to load the preprocessed data that is stored in JSON
    # data_processed = json.load(open('preprocessed_data.json'))
    # print(data_processed )
    # z={'0': {'area': 300, 'rooms-number': 2, 'zip-code': 1050, 'land-area': 200, 'garden': True, 'garden-area': 100, 'equipped-kitchen': True, 'swimmingpool': False, 'furnished': True, 'open-fire': True, 'terrace': False, 'terrace-area': 0, 'facades-number': 2, 'property-type_APARTMENT': 1, 'property-type_2': 0.0, 'property-type_3': 0.0, 'building-state_NEW': 1, 'building-state_2': 0.0, 'building-state_3': 0.0, 'building-state_4': 0.0, 'building-state_5': 0.0}}
    #
    #
    # features=z["0"]
    # testing_features=[]
    # testing_features.append(features['area'])
    # testing_features.append(features['rooms-number'])
    # testing_features.append(features['zip-code'])
    # testing_features.append(features['land-area'])
    # testing_features.append(features['garden'])
    # testing_features.append(features['garden-area'])
    # testing_features.append(features['equipped-kitchen'])
    # testing_features.append(features['swimmingpool'])
    # testing_features.append(features['furnished'])
    # testing_features.append(features['open-fire'])
    # testing_features.append(features['terrace'])
    # testing_features.append(features['terrace-area'])
    # testing_features.append(features['facades-number'])
    #
    # if 'property-type_APARTMENT' in features:
    #     testing_features.append(features['property-type_APARTMENT'])
    #     testing_features.append(features['property-type_2'])
    #     testing_features.append(features['property-type_3'])
    # elif 'property-type_HOUSE' in features:
    #     testing_features.append(features['property-type_2'])
    #     testing_features.append(features['property-type_HOUSE'])
    #     testing_features.append(features['property-type_3'])
    # elif 'property-type_OTHERS' in features:
    #     testing_features.append(features['property-type_2'])
    #     testing_features.append(features['property-type_3'])
    #     testing_features.append(features['property-type_OTHERS'])
    # else:
    #     testing_features.append(0)
    #     testing_features.append(0)
    #     testing_features.append(0)
    #
    # if 'building-state_NEW' in features:
    #     testing_features.append(features['building-state_NEW'])
    #     testing_features.append(features['building-state_2'])
    #     testing_features.append(features['building-state_3'])
    #     testing_features.append(features['building-state_4'])
    #     testing_features.append(features['building-state_5'])
    # elif 'building-state_GOOD' in features:
    #     testing_features.append(features['building-state_2'])
    #     testing_features.append(features['building-state_GOOD'])
    #     testing_features.append(features['building-state_3'])
    #     testing_features.append(features['building-state_4'])
    #     testing_features.append(features['building-state_5'])
    #
    # elif 'building-state_TO RENOVATE' in features:
    #     testing_features.append(features['building-state_2'])
    #     testing_features.append(features['building-state_3'])
    #     testing_features.append(features['building-state_TO RENOVATE'])
    #     testing_features.append(features['building-state_4'])
    #     testing_features.append(features['building-state_5'])
    #
    # elif 'building-state_JUST RENOVATED' in features:
    #     testing_features.append(features['building-state_2'])
    #     testing_features.append(features['building-state_3'])
    #     testing_features.append(features['building-state_4'])
    #     testing_features.append(features['building-state_JUST RENOVATED'])
    #     testing_features.append(features['building-state_5'])
    #
    # elif 'building-state_TO REBUILD' in features:
    #     testing_features.append(features['building-state_2'])
    #     testing_features.append(features['building-state_3'])
    #     testing_features.append(features['building-state_4'])
    #     testing_features.append(features['building-state_5'])
    #     testing_features.append(features['building-state_TO REBUILD'])
    #
    # else:
    #     testing_features.append(0)
    #     testing_features.append(0)
    #     testing_features.append(0)
    #     testing_features.append(0)
    #     testing_features.append(0)
    #

    print(testing_features)