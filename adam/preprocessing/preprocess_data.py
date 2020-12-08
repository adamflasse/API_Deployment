def preprocess(json):
    """ It handles the json format so we can use it to fit the values to the features to predict properly the price """

    area = json['data']['area']
    property_subtype = json['data']["property-type"]
    property = property_type(property_subtype)
    rooms_number = json['data']['rooms-number']

    postcode = json['data']['zip-code']

    if postcode < 1000 or postcode > 10000:
        raise Exception("Wrong zipcode")


    default_model = building_default_model(property_subtype, area)
    try:
        land_area = json['data']['land-area']
    except:
        land_area = default_model['land-area']
    try:
        garden = json['data']['garden']
    except:
        garden = default_model['garden']
    try:
        garden_area = json['data']['garden-area']
    except:
        garden_area = default_model['garden-area']
    try:
        equipped_kitchen = json['data']['equipped-kitchen']
    except:
        equipped_kitchen = default_model['equipped_kitchen']
    try:
        swimmingpool = json['data']['swimmingpool']
    except:
        swimmingpool = default_model['swimmingpool']
    try:
        furnished = json['data']['furnished']
    except:
        furnished = default_model['furnished']
    try:
        open_fire = json['data']['open-fire']
    except:
        open_fire = default_model['open-fire']
    try:
        terrace = json['data']['terrace']
    except:
        terrace = default_model['terrace']
    try:
        terrace_area = json['data']['terrace-area']
    except:
        terrace_area = default_model['terrace-area']
    try:
        building_state = json['data']['building-state']
    except:
        building_state = default_model['building-state']

    state_building = state_of_building(building_state)



    return [
        [postcode, area, rooms_number, garden, garden_area, terrace, terrace_area, land_area, open_fire, swimmingpool,
         equipped_kitchen, furnished, property[0], property[1], property[2], state_building[0],
         state_building[1], state_building[2], state_building[3], state_building[4]]]

def check_for_errors(json):
    """ checks if there are missing required values"""
    area = json['data']['area']
    property_subtype = json['data']["property-type"]
    property = property_type(property_subtype)
    rooms_number = json['data']['rooms-number']
    postcode = json['data']['zip-code']
    message = "Ooops something went wrong with the required inputs, please check: https://github.com/adamflasse/Api_deployment/blob/main/README.md for more info"
    if area == None or rooms_number == None or property == None:
        return message
    elif postcode == None or postcode < 1000 or postcode > 10000:
        return message
    else :
        return "good"

def building_default_model(building_type, area):
    if building_type == 'APARTMENT':
        appartment_dico = {"land-area": area + 20,
                       "garden": False,
                       "garden-area": 0,
                       "equipped-kitchen": True,
                       "swimmingpool": False,
                       "furnished": False,
                       "open-fire": False,
                       "terrace": True,
                       "terrace-area": 20,
                       "building-state": "GOOD"}
        return appartment_dico

    elif building_type == 'HOUSE':

        houses_dico = {"land-area": area + 75,
                   "garden": True,
                   "garden-area": 75,
                   "equipped-kitchen": True,
                   "swimmingpool": False,
                   "furnished": False,
                   "open-fire": False,
                   "terrace": False,
                   "terrace-area": 0,
                   "building-state": "GOOD"}
        return houses_dico

    else :
       other_dico = {"land-area": area,
                 "garden": False,
                 "garden-area": 0,
                 "equipped-kitchen": False,
                 "swimmingpool": False,
                 "furnished": False,
                 "open-fire": False,
                 "terrace": False,
                 "terrace-area": 0,
                 "building-state": "GOOD"}
       return other_dico




def property_type(subtype):
    """It will check what type of property it is and then return a list so we can handle the dummies """
    if subtype == "APARTMENT":
        return [1, 0, 0]
    elif subtype == "HOUSE":
        return [0, 1, 0]
    elif subtype == "OTHERS":
        return [0, 0, 1]


def state_of_building(state):
    """ Same as the function above but with the building state """

    if state == 'NEW':
        return [0, 0, 1, 0, 0]
    elif state == 'GOOD':
        return [1, 0, 0, 0, 0]
    elif state == 'TO RENOVATE':
        return [0, 0, 0, 0, 1]
    elif state == 'JUST RENOVATED':
        return [0, 1, 0, 0, 0]
    elif state == 'TO REBUILD':
        return [0, 0, 0, 1, 0]

