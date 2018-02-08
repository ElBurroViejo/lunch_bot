import geo_fetch


class Restaurant():
    
    def __init__(self, prow):
        
        self.name = prow.name
        self.vicinity = prow.vicinity
        self.rating = prow.rating
        self.is_open = prow.is_open
        

def initialize_restaurants():
    
    restaurant_df = geo_fetch.execute_request

    restaurant_list = [Restaurant(row) for row in restaurant_df.itertuples()]
    
    return restaurant_list 
    