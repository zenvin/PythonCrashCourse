from user import User

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