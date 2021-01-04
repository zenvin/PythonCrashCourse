class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user', 'can reset CPU']
        
    def show_privileges(self):
        print(f"You have the following privileges: {self.privileges}")