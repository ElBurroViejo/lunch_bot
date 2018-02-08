import requests
import time
import pandas as pd
import get_credentials 

cred = get_credentials.credentials

google_geo_key = cred.google_places_key


params = {

                   "location" : [52.4848525,13.356632]
                  , "radius"  : 250
                  , "type" : "restaurant"
                  , "key" : google_geo_key
                    }

def create_client(params, output = "json"):


    assert "location" in params and "radius" in params and "type" in params and "key" in params

    string_list = [ "location=" +",".join(map(str,params["location"])) ]

    for key in params:
        if not key in  ["location", "key", "pagetoken"]:
            string_list.append( key + "=" + str(params[key]))


    string_list.append("key=" + params["key"])
    if "pagetoken" in params:
        string_list= [ "key=" + params["key"] , "pagetoken=" + params["pagetoken"]]


    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/"
    client = base_url + output + "?" + "&".join(string_list) 
    return client


def df_prep(func):
    """
    acquires dataframe and cleans/ purges output
    """
    data_frame = func()
    data_frame["opening_hours"] = data_frame["opening_hours"].astype(dict)
    data_frame["opening_hours"].fillna("empty", inplace = True)
    data_frame["is_open"] = data_frame["opening_hours"].apply(
            lambda x: x["open_now"] if "open_now" in x else None)
    keep_keys = ["name", "vicinity", "rating", "is_open"]

    return data_frame[keep_keys]
    
@df_prep
def execute_request():
    
    
    global_results = []
    
    while True:
            
        time.sleep(3)
        response = requests.get(create_client(params))
        json_file = response.json()
        
        global_results.extend(json_file["results"])
        if (len(global_results)) == 0:
            print (json_file)
        if "next_page_token" in json_file:
            params["pagetoken"] = json_file["next_page_token"]
        else:
            break
        
 
    return pd.DataFrame(global_results)

