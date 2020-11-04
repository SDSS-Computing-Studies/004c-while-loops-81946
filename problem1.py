##### Problem 1
#python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied
"""
import math
name=''
password= ''
x=0

while name != "admin" and x!=3:
    name = (input("Enter username: ")).strip()
    if name == "admin":
        while password != "12345" and x!=3:
            password = (input("Enter password: ")).strip()
            if password == "12345":
                print("Access granted")
                break
            else:
                print("Access denied")
                x=x+1
    if x==3:
        print("You have no more tried")
           







