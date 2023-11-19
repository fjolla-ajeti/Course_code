#Task 1

#Create a class method named validate, which should be called from the __init__ method to validate parameter email, passed to the constructor. The logic inside the validate method could be to check if the passed email parameter is a valid email string.

#Email validations:

#Valid email address format 
#Wiki: Email address

import re

class EmailValidator:
    def __init__(self,email):
        self.validate(email)
        self.email=email
    
    @classmethod
    def validate(cls,email):
        if not re.match(r'^[\w\.-]+@[a-zA-Z\d\.-]+\.[a-zA-Z]{2,}$', email):
            raise ValueError("Invalid email address:{}".format(email))
        else:
            print("Valid email address:{}".format(email))


try:
    email_validator=EmailValidator("john.doe@example.com")
except ValueError as e:
    print(e)

try:
    invalid_email_validator=EmailValidator("invalid_email")
except ValueError as e:
    print(e)