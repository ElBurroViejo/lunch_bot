import requests
import time
import pandas as pd
import get_credentials 

cred = get_credentials.credentials

google_geo_key = cred.google_places_key


params = {

                   "location" : [52.4848525,13.356632]
                  , "radius"  : 600
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


def execute_request():
    
    
    global_results = []
    
    while True:
        print(len(global_results))
        time.sleep(5)
        response = requests.get(create_client(params))
        json_file = response.json()
        
        global_results.extend(json_file["results"])
        if "next_page_token" in json_file:
            params["pagetoken"] = json_file["next_page_token"]
        else:
            break
    print(len(global_results)) 
    return global_results
test =  execute_request()

#print (create_client(params))
#a = (requests.get(create_client(params)))
#
#json_file = a.json()["results"]
#df = pd.DataFrame(json_file)