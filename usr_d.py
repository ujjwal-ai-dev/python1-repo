'''9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.'''

class user:
    def __init__(self,first_name,last_name,DOB,gender):
        self.first_name = first_name
        self.last_name = last_name
        self.DOB = DOB 
        self.gender = gender
        self.login_attempt = 0
    def describe_user(self):
        print(f"User details:\n\tfirst name: {self.first_name}\n\tlast_name: {self.last_name}\n\tDOB: {self.DOB}\n\t Gender: {self.gender}")
    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
    def Login_attempt(self):
        self.login_attempt += 1
    def no_login(self):
        print("no. of login: "+ str(self.login_attempt))
    def reset_login_attempt(self):
        self.login_attempt = 0


user1 = user('Ujjwal','Gupta','02/09/2001','Male')
user1.describe_user()
user1.greet_user()
user1.Login_attempt()
user1.no_login()
user1.Login_attempt()
user1.no_login()
user1.reset_login_attempt()
user1.no_login()

