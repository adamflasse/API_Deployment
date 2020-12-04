import pandas as pd
import numpy as np
import json


""" 
Peprocess your client data
this program works for one entry (value); or list of entries for each feature
and return a dictionary, that has the same structure of the input JSON dictionary
"""

class Cleaner_SalesData:
    """ Utility class that cleans real estate sale offers data from a CSV file into a pandas DataFrame for further work on it"""
    def __init__(self, url_json):
        # self.url = url
        self.url_json = url_json
        self.sales_data = None
        self.cleaned = False

    def cleaning_feature(self):
        openfile = open(self.url_json)
        jsondata = json.load(openfile)
        self.sales_data= pd.DataFrame([jsondata["0"]])
        openfile.close()

        #if we have csv files
        #na_identifiers = ['NA', 'None', 'Not specified', 'NaN', 'NAN']
        #self.sales_data = pd.read_csv(self.url, sep=",", skipinitialspace=True, na_values=na_identifiers, low_memory=False)
        # # drop these features ['source', 'hyperlink', 'sale', 'land_plot_surface']
        # self.sales_data.drop('hyperlink', axis='columns', inplace=True)
        # self.sales_data.drop('source', axis='columns', inplace=True)
        # self.sales_data.drop('sale', axis='columns', inplace=True)
        # self.sales_data.drop('land_plot_surface', axis='columns', inplace=True)
        # # 3333333333333333333333333333333333333333333333333
        # # self.sales_data.rename(columns={'building_state': 'building-state','garden_area': 'garden-area','property_subtype': 'property-type','postcode': 'zip-code','facades_number': 'facades-number','rooms_number': 'rooms-number','terrace_area': 'terrace-area','land_surface': 'land-area','open_fire': 'open-fire','kitchen_has': 'equipped-kitchen', 'swimming_pool_has':'swimmingpool'}, inplace=True)
        # # #self.sales_data.drop('building-state', axis='columns', inplace=True)
        # #33333333333333333333333333333333333333333333333333333


        ###################################
        ###################################
        #######    Check Obligation Features
        ###################################
        ###################################
        #Obligation, area
        if ('area' not in self.sales_data.columns):
            raise Exception("We can not provide prediction, please input area feature in your data")
        elif  ('property-type' not in self.sales_data.columns):
            raise Exception("We can not provide prediction, please input property-type feature in your data")
        elif ('zip-code' not in self.sales_data.columns):
            raise Exception("We can not provide prediction, please input zip-code feature in your data")
        elif ('rooms-number' not in self.sales_data.columns):
            raise Exception("We can not provide prediction, please input rooms-number feature in your data")
        else:
            pass

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
        ######## generate dummies
        # create dummies, the prefix "", store it in another varialbe
        dummies_region = pd.get_dummies(self.sales_data['property-type'], prefix="property-type")
        # concatenate, dummies with the original df
        self.sales_data = pd.concat([self.sales_data, dummies_region], axis=1, sort=False)
        # drop the region
        self.sales_data.drop('property-type', axis="columns", inplace=True)
        # we need to add extra 2-cols here to get the same size of the X-train
        self.sales_data['property-type_2'] = np.zeros(self.sales_data['area'].shape[0])
        self.sales_data['property-type_3'] = np.zeros(self.sales_data['area'].shape[0])



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
            #### if buildin-state is exist, the generate dummies
            # get the dummies of categorize_state:::: Optional["NEW" | "GOOD" | "TO RENOVATE" | "JUST RENOVATED" | "TO REBUILD"]
            # create dummies, the prefix "", store it in another varialbe
            dummies_region = pd.get_dummies(self.sales_data['building-state'] , prefix="building-state")
            # concatenate, dummies with the original df
            self.sales_data= pd.concat([self.sales_data, dummies_region], axis=1, sort=False)
            # drop the region
            self.sales_data.drop('building-state', axis="columns", inplace=True)  # drop_first="True" if we need to drop the first one
            self.sales_data['building-state_2'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state_3'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state_4'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state_5'] = np.zeros(self.sales_data['area'].shape[0])


        else:
            #if not exist, generate dummies hard coded
            self.sales_data['building-state_NEW'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state_GOOD'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state_TO RENOVATE'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state_JUST RENOVATED'] = np.zeros(self.sales_data['area'].shape[0])
            self.sales_data['building-state_TO REBUILD'] = np.zeros(self.sales_data['area'].shape[0])
            #self.sales_data['building-state'] = self.sales_data['building-state'].apply(lambda x: str(x))


        ############# drop full-adrees, we do not use it in the prediction
        self.sales_data.drop('full-address', axis='columns', inplace=True)
        #
        # features = [
        #     'property_subtype_Apartment',
        #                     'property_subtype_House', 'property_subtype_Other', 'building_state_agg_GOOD',
        #                     'building_state_agg_JUST RENOVATED', 'building_state_agg_NEW',
        #                     'building_state_agg_TO REBUILD', 'building_state_agg_TO RENOVATE']
        #
        #store the features according to the training data set

        # ['area', 'rooms-number', 'zip-code', 'land-area', 'garden', 'garden-area', 'equipped-kitchen', 'swimmingpool',
        #  'furnished', 'open-fire', 'terrace', 'terrace-area', 'facades-number', 'property-type_APARTMENT',
        #  'building-state_NEW']
        #
        # self.sales_data=self.sales_data[['zip-code','area','rooms-number','garden','garden-area','terrace','terrace-area',
        #         'land-area','property-type_APARTMENT','property-type_HOUSE','property-type_OTHERS',]]
        #this is a vector that I have to return
        # X_test=self.sales_data.values
        return(self.sales_data.to_dict('index'))
        #return (self.sales_data.columns.tolist())










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


if __name__=="__main__":
    #url = 'https://raw.githubusercontent.com/FrancescoMariottini/project3/main/inputs/all_sales_data.csv'
    url_json='input_data.json'
    ss=Cleaner_SalesData(url_json)
    print(ss.cleaning_feature())

    #for testing
    # import pandas as pd
    # import json
    # openfile=open(url_json)
    # jsondata=json.load(openfile)
    # print(jsondata["0"])
    # df=pd.DataFrame([jsondata["0"]])
    # print(df)
    # openfile.close()
    #

