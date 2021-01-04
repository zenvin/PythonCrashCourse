"""A module for user, admin and privilege"""

class User:
    """A simple model of a user."""
    def __init__(self, first_name, last_name, age="", weight=""):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        
    def describe_user(self):
        if self.age and self.weight:
            print(f"{self.first_name.title()} {self.last_name.title()}, age {self.age} and weight is {self.weight}.")
        elif self.age:
            print(f"{self.first_name.title()} {self.last_name.title()}: age is {self.age}.")
        elif self.weight:
            print(f"{self.first_name.title()} {self.last_name.title()}: weight is {self.weight}.")
        else:
            print(f"{self.first_name.title()} {self.last_name.title()}")
                  
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}.")

class Admin(User):
    def __init__(self, first_name, last_name, age="", weight="" ):
        super().__init__(first_name, last_name, age="", weight="")
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print(f"You have the following privileges: {self.privileges}")

class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can reset CPU']
        
    def show_privileges(self):
        print(f"You have the following privileges: {self.privileges}")