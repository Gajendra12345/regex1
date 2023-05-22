#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      in
#
# Created:     03-05-2023
# Copyright:   (c) in 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import re

def validate_name(name):
    pattern = r"^[A-Za-z\s]+$"
    return re.match(pattern, name)

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email)

def main():
    name = input("Enter your name: ")
    if validate_name(name):
        email = input("Enter your email: ")
        if validate_email(email):
            print("Name and email are valid.")
        else:
            print("Invalid email.")
    else:
        print("Invalid name.")

if __name__ == '__main__':
    main()


