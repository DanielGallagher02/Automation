# Question 2
# By: Daniel Gallagher
# Due Date: 04/04/2022

#Part A
from getpass import getpass
import time

#Checking the password and seeing if it meets the password requirements
#Display a message if it does not meet the requirements

def isValidPassword(passwordIn):
    special_chars = {'-', '_', '.', '!', '@', '#', '$', '^', '&', '(', ')', '%', '/'}
    valid = True

    #Checking to see if any word in password 
    #contains any special characters
    if not any(char in special_chars for char in passwordIn):
        print("The Password does not contain any special characters")
        valid = False

    #Checking to see if any word in password
    #contains a number
    if not any(char.isdigit() for char in passwordIn):
        print("The Password does not contain at least 1 number")  
        valid = False

    #Checking to see if any word in the password
    #has a capital letter
    if not any(char.isupper() for char in passwordIn):
        print("The Password does not contain at least 1 capital letter")
        valid = False

    if valid:
        return valid 

#Declaring counter
counter = 0

while(counter != 3):
    #A program where the user must enter a first name, last name, username
    # email ID and password 
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    username = input("Enter your username: ")
    emailID = input("Enter your emailID: ")

    #Hiding the input from the user using getpass
    password = getpass("Enter your password: ")

    #Adding a counter for every time password in entered
    counter += 1

    #If the counter is equal to 3
    if counter == 3:
        #User is blocked for 2 minutes
        time.sleep(120)

    if(isValidPassword(password)):
        print("Password is valid")       
        #Saving the password to the notepad file 
        with open('Passwords.txt', 'w') as f:
            f.write(password + '\n')  
    else:
        print("Invalid Password")       











