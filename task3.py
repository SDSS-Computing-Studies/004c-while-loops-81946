#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""
import math

while b==x:
    num= input("Enter a number")
    q= int(num)
    b= q/2
    a= float(num)
    x= a/2
    if b==x:
        print("That is an even integer")
    else:
        print("That is not an even integer")

