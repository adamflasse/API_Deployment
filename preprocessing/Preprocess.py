"""
this generates a preprocesed data and preprocessed json file
"""
from Cleaner import Cleaner_SalesData
import json

#you can specify
url_json = 'input_data.json'

preprocessed_dict=Cleaner_SalesData(url_json)
r=preprocessed_dict.cleaning_feature()
#print(r)

with open("preprocessed_data.json", "w") as p1:
    json.dump(r, p1)

#If we want to load the preprocessed data that is stored in JSON
data_processed = json.load(open('preprocessed_data.json'))
#print(data_processed )