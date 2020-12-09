import numpy as np
import pandas as pd 
import os
import re
import json

""" 
Peprocess your client data
this program works for one entry (value); or list of entries for each feature
and return a dictionary, that has the same structure of the input JSON dictionary
"""

class Cleaner_SalesData:
    """ Utility class that cleans real estate sale offers data from a CSV file into a pandas DataFrame for further work on it"""
    def __init__(self, json_file):
        # self.url = url
        self.json_file = json_file
        self.sales_data = None
        self.cleaned = False

    def cleaning_feature(self):
        # Serializing json  
        json_object = json.dumps(self.json_file, indent = 4) 
          
        # Writing to sample.json 
        with open("Datasets/sample.json", "w") as outfile: 
            outfile.write(json_object) 

        self.sales_data = pd.read_json("Datasets/sample.json", orient='index')

        ###################################
        #######    Check Obligation Features
        ###################################
        ###################################
        #Obligation, area
        if ('area' not in self.sales_data.columns):
            return "We can not provide prediction, please input area feature in your data"
        elif  ('property-type' not in self.sales_data.columns):
            return "We can not provide prediction, please input property-type feature in your data"
        elif ('zip-code' not in self.sales_data.columns):
            return "We can not provide prediction, please input zip-code feature in your data"
        elif ('rooms-number' not in self.sales_data.columns):
            return "We can not provide prediction, please input rooms-number feature in your data"
        else:
            pass
        

        #check if you entered proper feature
        ### zip-code checking
        legal_belgian_postcode_pattern = '[1-9][0-9][0-9][0-9]'
        if ('zip-code' in self.sales_data.columns):
            to_check=self.sales_data['zip-code'].values
            #print(to_check[0])
            # check if the input is number
            if str(to_check[0]).isdigit():
                #check if the entry is correct Belgian zip-code
                extracted_postcodes = re.findall(legal_belgian_postcode_pattern, str(to_check[0]))
                if len(extracted_postcodes) > 0:
                    pass
                else:
                    raise Exception("Please, input correct zip-code")
            else:
                raise Exception("Please, input number zip-code")


        ###################################
        ###################################
        #######    Boolean Features
        ###################################
        ###################################
        #Optional, equipped-kitchen
        if  'equipped-kitchen' in self.sales_data.columns:
            self.sales_data['equipped-kitchen']=self.sales_data['equipped-kitchen'].apply(lambda x: Cleaner_SalesData.bool_or_keep(x))
            #If I have missing value, I replace it with the highest frequency value
            self.sales_data['equipped-kitchen']=self.sales_data['equipped-kitchen'].fillna(self.sales_data['equipped-kitchen'].mode().iloc[0])
            #cast to boolean
            self.sales_data['equipped-kitchen'] = self.sales_data['equipped-kitchen'].apply(lambda x: bool(x))
        else:
            self.sales_data['equipped-kitchen']=np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['equipped-kitchen'] = self.sales_data['equipped-kitchen'].apply(lambda x: bool(x))

        # Optional, furnished
        if  'furnished' in self.sales_data.columns:
            self.sales_data['furnished']=self.sales_data['furnished'].apply(lambda x: Cleaner_SalesData.bool_or_keep(x))
            self.sales_data['furnished']=self.sales_data['furnished'].fillna(self.sales_data['furnished'].mode().iloc[0])
        else:
            self.sales_data['furnished']=np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['furnished'] = self.sales_data['furnished'].apply(lambda x: bool(x))

        # Optional, swimmingpool
        if  'swimmingpool' in self.sales_data.columns:
            self.sales_data['swimmingpool']=self.sales_data['swimmingpool'].apply(lambda x: Cleaner_SalesData.bool_or_keep(x))
            self.sales_data['swimmingpool']=self.sales_data['swimmingpool'].fillna(self.sales_data['swimmingpool'].mode().iloc[0])
            self.sales_data['swimmingpool'] = self.sales_data['swimmingpool'].apply(lambda x: bool(x))
        else:
            self.sales_data['swimmingpool']=np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['swimmingpool'] =self.sales_data['swimmingpool'].apply(lambda x: bool(x))

        #Optional, open-fire
        if  'open-fire' in self.sales_data.columns:
            self.sales_data['open-fire']=self.sales_data['open-fire'].apply(lambda x: Cleaner_SalesData.bool_or_keep(x))
            self.sales_data['open-fire']=self.sales_data['open-fire'].fillna(self.sales_data['open-fire'].mode().iloc[0])
            self.sales_data['open-fire'] = self.sales_data['open-fire'].apply(lambda x: bool(x))
        else:
            self.sales_data['open-fire']=np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['open-fire'] =self.sales_data['open-fire'].apply(lambda x: bool(x))

        #Optional, terrace
        if  'terrace' in self.sales_data.columns:
            self.sales_data['terrace']=self.sales_data['terrace'].apply(lambda x: Cleaner_SalesData.bool_or_keep(x))
            self.sales_data['terrace']=self.sales_data['terrace'].fillna(self.sales_data['terrace'].mode().iloc[0])
            self.sales_data['terrace'] = self.sales_data['terrace'].apply(lambda x: bool(x))
        else:
            self.sales_data['terrace']=np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['terrace'] =self.sales_data['terrace'].apply(lambda x: bool(x))

        #Optional, garden
        if  'garden' in self.sales_data.columns:
            self.sales_data['garden']=self.sales_data['garden'].apply(lambda x: Cleaner_SalesData.bool_or_keep(x))
            self.sales_data['garden']=self.sales_data['garden'].fillna(self.sales_data['garden'].mode().iloc[0])
            self.sales_data['garden'] = self.sales_data['garden'].apply(lambda x: bool(x))
        else:
            self.sales_data['garden']=np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['garden'] =self.sales_data['garden'].apply(lambda x: bool(x))

        ###################################
        ###################################
        #######    Area Features
        ###################################
        ###################################
        #area, remove m2
        self.sales_data['area'] = self.manage_AreaFeature(self.sales_data['area'])

        #land-area": Optional[int],
        if 'land-area' in self.sales_data.columns:
            self.sales_data['land-area']=self.manage_AreaFeature(self.sales_data['land-area'])
        else:
            self.sales_data['land-area'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['land-area'] = self.sales_data['land-area'].apply(lambda x: int(x))

        #"terrace-area": Optional[int],
        if 'terrace-area' in self.sales_data.columns:
            self.sales_data['terrace-area']=self.manage_AreaFeature(self.sales_data['terrace-area'])
        else:
            self.sales_data['terrace-area'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['terrace-area'] = self.sales_data['terrace-area'].apply(lambda x: int(x))

        #garden-area": Optional[int],
        if 'garden-area' in self.sales_data.columns:
            self.sales_data['garden-area']=self.manage_AreaFeature(self.sales_data['garden-area'])
        else:
            self.sales_data['garden-area'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['garden-area'] = self.sales_data['garden-area'].apply(lambda x: int(x))
        ###################################
        ###################################
        #######    Number Features
        ###################################
        ###################################
        #"rooms-number": int,
        #remove outliers
        to_be_deleted_filter = self.sales_data['rooms-number'].apply(lambda x: x == 0 or x >= 100)
        self.sales_data.loc[to_be_deleted_filter, 'rooms-number'] = None
        self.sales_data['rooms-number'] = self.sales_data['rooms-number'].fillna(self.sales_data['rooms-number'].mode().iloc[0])
        self.sales_data['rooms-number'] = self.sales_data['rooms-number'].apply(lambda x: int(x))


        #facades-number": Optional[int],
        if 'facades-number' in self.sales_data.columns:
            to_be_deleted_filter = self.sales_data['facades-number'].apply(lambda x: x == 0 or x > 4)
            self.sales_data.loc[to_be_deleted_filter, 'facades-number'] = None
            self.sales_data['facades-number'] = self.sales_data['facades-number'].fillna(self.sales_data['facades-number'].mode().iloc[0])
            self.sales_data['facades-number'] = self.sales_data['facades-number'].apply(lambda x: int(x))
        else:
            self.sales_data['facades-number'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['facades-number'] = self.sales_data['facades-number'].apply(lambda x: int(x))

        ###################
        ######### TO DO, need TO CHECK AGAIN
        #################
        #"zip-code": int, we could have nan input
        self.sales_data['zip-code'] = self.sales_data['zip-code'].fillna(0)
        self.sales_data['zip-code'] = self.sales_data['zip-code'].apply(lambda x: int(x))

        # #"property-type": "APARTMENT" | "HOUSE" | "OTHERS",
        self.sales_data['property-type']=self.sales_data['property-type'].apply(lambda x: Cleaner_SalesData.property_or_keep(x))
        self.sales_data['property-type']= self.sales_data['property-type'].fillna(0)

        #"full-address": Optional[str],
        if 'full-address' in self.sales_data.columns:
            self.sales_data['full-address'] = self.sales_data['full-address'].apply(lambda x: str(x))
            self.sales_data['full-address'] = self.sales_data['full-address'].fillna(0)
        else:
            self.sales_data['full-address'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['full-address'] = self.sales_data['full-address'].apply(lambda x: str(x))

        #building-state": Optional
        if 'building-state' in self.sales_data.columns:
            self.sales_data['building-state'] = self.sales_data['building-state'].apply(lambda x: Cleaner_SalesData.categorize_state(x))
            self.sales_data['building-state'] = self.sales_data['building-state'].fillna(0)
        else:
            self.sales_data['building-state'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state'] = self.sales_data['building-state'].apply(lambda x: str(x))

        return self.sales_data

    @staticmethod
    def categorize_state(value):
        to_renovate = ['TO_RENOVATE', 'TO_BE_DONE_UP', 'TO_RESTORE', 'old', 'To renovate', 'To be done up',
                       'To restore', "TO RENOVATE"]
        good = ['GOOD', 'Good', 'AS_NEW', 'As new']
        renovated = ['JUST_RENOVATED', 'Just renovated', "JUST RENOVATED"]
        new = ['New',"NEW"]
        to_rebuild=["TO REBUILD","TO_REBUILD", "To rebuild"]
        category = None  # default category (corresponds to values = '0')
        if value in to_renovate:
            category = "TO RENOVATE"
        elif value in good:
            category = "GOOD"
        elif value in renovated:
            category = "JUST RENOVATED"
        elif value in new:
            category = "NEW"
        elif value in to_rebuild:
            category = "TO REBUILD"
        return category

    def manage_AreaFeature(self, Ser):
        #remove m2
        Ser= Ser.apply(lambda x: Cleaner_SalesData.area_remove_m2(x))
        #fill in the empty cells
        #Ser.fillna(Ser.median(), inplace=True)
        Ser= Ser.fillna(Ser.median())
        #cast to int
        Ser = Ser.apply(lambda x: int(x))
        return (Ser)

    @staticmethod
    def property_or_keep(x):
        try:
            if x in ["APARTMENT", "Apartment"]:
                return ("APARTMENT")
            elif x in ["HOUSE", "House"]:
                return ("HOUSE")
            elif str(x).isdigit():
                return None
            elif x not in ["APARTMENT", "Apartment","HOUSE", "House"]:
                return ("OTHERS")
        except ValueError:
                 return None

    @staticmethod
    def bool_or_keep(x):
        try:
            if x in [1, "1", "TRUE", "true", "True",True,"YES", "yes", "Yes"]:
                return (True)
            elif x in [0, "0", "FALSE", "false", "False",False,"NO", "no", "No"]:
                return (False)
        except ValueError:
            return (None)

    @staticmethod
    # a single integer number is extracted from area to remove the m2 measurement units.
    # this simple method was adopted since no commas were found in area field.
    def area_remove_m2(x):
        try:
            return int(x)
        except ValueError:
            x=str(x)
            numbers = [int(s) for s in x.split() if s.isdigit()]
            if len(numbers) == 1:
                return int(numbers[0])
            elif len(numbers) > 1:
                return False
            else:
                return None

def preprocess(json_file):
    #url_json = 'input_data.json'
    ss=Cleaner_SalesData(json_file)
    new_json_df = ss.cleaning_feature()

    if type(new_json_df)==str:
        return new_json_df

    cleaned_json_df = pd.DataFrame()
    cleaned_json_df['postcode'] = new_json_df['zip-code']
    cleaned_json_df['area'] = new_json_df['area']
    cleaned_json_df['rooms_number'] = new_json_df['rooms-number']
    cleaned_json_df['garden'] = new_json_df['garden']
    cleaned_json_df['garden_area'] = new_json_df['garden-area']
    cleaned_json_df['terrace'] = new_json_df['terrace']
    cleaned_json_df['terrace_area'] = new_json_df['terrace-area']
    cleaned_json_df['land_surface'] = new_json_df['land-area']
    cleaned_json_df['open_fire'] = new_json_df['open-fire']
    cleaned_json_df['swimming_pool_has'] = new_json_df['swimmingpool']
    cleaned_json_df['equipped_kitchen_has'] = new_json_df['equipped-kitchen']
    cleaned_json_df['furnished'] = new_json_df['furnished']
    cleaned_json_df['property_subtype'] = new_json_df['property-type']
    cleaned_json_df['building_state'] = new_json_df['building-state']

    cleaned_json_df[['APARTMENT', 'HOUSE', 'OTHERS', 'GOOD',
           'JUST RENOVATED', 'NEW', 'TO REBUILD', 'TO RENOVATE']] = 0

    for i in range(len(cleaned_json_df)):
        property_name = cleaned_json_df.loc[i, 'property_subtype']
        building_state_name = cleaned_json_df.loc[i, 'building_state']
        cleaned_json_df.loc[i, property_name] = 1
        cleaned_json_df.loc[i, building_state_name] = 1

    cleaned_json_df.drop(['property_subtype', 'building_state'], axis=1, inplace=True)
    cleaned_json_df = cleaned_json_df.astype('float64')

    return cleaned_json_df
