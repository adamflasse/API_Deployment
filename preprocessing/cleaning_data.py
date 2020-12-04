import numpy as np
import pandas as pd 
import os


def preprocess(new_json):
    path = 'Datasets/'+str(new_json)
    new_input = pd.read_json(path, orient='index')
    compatible_df = pd.DataFrame()
    compatible_df['property_subtype'] = new_input['property-type']
    compatible_df['area'] = new_input['area']
    compatible_df['rooms_number'] = new_input['rooms-number']
    compatible_df['equipped_kitchen_has'] = new_input['equipped-kitchen']
    compatible_df['garden_area'] = new_input['garden-area']
    compatible_df['terrace_area'] = new_input['terrace-area']
    compatible_df['furnished'] = new_input['furnished']
    compatible_df['swimming_pool_has'] = new_input['swimmingpool']
    compatible_df['land_surface'] = new_input['land-area']
    compatible_df['building_state_agg'] = new_input['building-state']
    compatible_df['open_fire'] = new_input['open-fire']
    compatible_df['longitude'] = 0
    compatible_df['latitude'] = 0
    
    return compatible_df