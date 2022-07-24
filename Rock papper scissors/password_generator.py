"""
Allows users to generate a random password based on their specifications
"""

### import modules
from supporting_class import Password

### asking users whether they want to generate a password 
while True: 
    want_pwd = input("If you don't want to generate a password, enter: N ")

    if want_pwd == "N":
        break

### get user specifications for the password and then generate it 
    else:
        user_pwd = Password()

        user_pwd.gen_pwd()