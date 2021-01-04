"""A class that can be used to represent a restaurant"""

class Restaurant: 
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"The {self.restaurant_name.title()} restaurant specializes in {self.cuisine_type.title()} cuisine.")
    
    def open_restaurant(self):
        print(f"The {self.restaurant_name.title()} is open for business.")
        
    def set_number_served(self):
        print(f"Now serving {self.number_served} guests!")\
    
    def increment_number_served(self, additional_served):
        self.number_served += additional_served

class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'coconut pineapple']
    
    def list_flavors(self):
        print(f"We have these flavors: {self.flavors}.")