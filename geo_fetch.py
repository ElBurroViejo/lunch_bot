import requests

import get_credentials 

cred = get_credentials.credentials

google_geo_key = cred.google_places_key


params = {

                   "location" : [-33.8670522,151.1957362]
                  , "radius"  : 300
                  , "type" : "restaurant"
                  , "key" : google_geo_key
                    }

def create_client(params, output = "json"):


    
    assert "location" in params and "radius" in params and "type" in params and "key" in params

    string_list = [ "location=" +",".join(map(str,params["location"])) ]

    for key in params:
        if key != "location" and "key" != key:
            string_list.append( key + "=" + str(params[key]))


    string_list.append("key=" + params["key"])

    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/"
    client = base_url + output + "?" + "&".join(string_list) 
    return client

print (create_client(params))
a = (requests.get(create_client(params)))
