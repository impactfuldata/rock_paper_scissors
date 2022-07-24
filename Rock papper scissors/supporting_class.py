"""
Contains the supporting class for OOP Password generator.py
"""
### import modules
import string
import random

### create class
class Password:
    """
    Class for generating a password 
    """
    def __init__(self):
        """ 
        Users specify:
            whether upper case alphabets should be included
            whether lower case alphabets should be included
            whether numbers should be included
            whether special case characters should be included
            length of the password
        """
        # Users specify whether upper case alphabets should be included
        self.az_upper = []
        self.az_upper_choice = input("Do you want upper case characters in the password?: Y or N ")
        if self.az_upper_choice == "Y":
            self.az_upper = string.ascii_uppercase
        
        # Users specify whether lower case alphabets should be included
        self.az_lower = []
        self.az_lower_choice = input("Do you want lower case characters in the password?: Y or N ")
        if self.az_lower_choice == "Y":
            self.az_lower = string.ascii_lowercase
        
        # Users specify whether numbers should be included
        self.numbers = []
        self.number_choice = input("Do you want numbers in the password?: Y or N ")
        if self.number_choice == "Y":
            self.numbers = [x for x in range (0,10)]
        
        # Users specify whether special characters should be included
        self.special = []
        self.special_choice = input("Do you want special characters in the password?: Y or N ")
        if self.special_choice == "Y":  
            self.special = [special for special in '[@_!#$%^&*()<>?/|}{~:]']

        # A combined list of upper case alphabets, lower case alphabets, numbers, special characters based on user specifications
        self.master = [*self.az_upper, *self.az_lower, *self.numbers, *self.special]

        # Users specify the length of the password 
        self.length_choice = int(input("How long do you want the password to be?"))

    def gen_pwd(self):
        """ 
        Password is generated based on user specifications
        """
        # generating a password as a list
        self.pwd = []
        for x in range (0,self.length_choice):
            self.pwd_choice = random.choice(self.master)
            self.pwd.append(self.pwd_choice)

        # converting the password list into a string
        self.pwd_str = "".join([str(elem) for elem in self.pwd])

        # printing the password 
        print(self.pwd_str)