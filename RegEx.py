
'''#PROJECT BASED ON RegEx mobile num
mob pass 
password cap small didgit special char atleast 8
mail @gmail.com  


    
class validation:
    def __init__(self):
        self.mobile_pattern=
        r"^[6-9][0-9]{9}"
    def mobile(self):'''

import re
name=input("Enter your name: ")
if re.fullmatch(r'[A-Za-z ]+', name):
    print("Name is valid")
else:
    print("Name is invalid")
mobile=input("Enter a mobile number: ")
if re.fullmatch(r'^[6-9][0-9]{9}',mobile):
    print(" Mobile number is valid")
else:
    print("Mobile number is not Invalid")
password=input("Enter a password: ")
if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[@#$%^&*!]).{8,}$', password):
    print("Password is valid")
else:
    print("Password is invalid")
mail=input("Enter an email: ")
if re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', mail):
    print("Email is valid")
else:
    print("Email is invalid")
    
    
    
