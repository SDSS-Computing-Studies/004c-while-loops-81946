#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""

name= ""
password= ""

while name != "admin":
    name = (input("Enter username: ")).strip()
    if name == "admin":
        while password != "12345":
            password = (input("Enter password: ")).strip()
            if password == "12345":
                print("Access granted")
                break
            else:
                print("Access denied")
    
        
    



#name = ""

#while name != "Marvin the Martian":
   # name = input("Who is your favorite cartoon character?")
    #if name != "Marvin the Martian":
      #  print("  You can't be serious.")