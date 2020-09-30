#! python3

"""
Count by 2's and display all the numbers, 1 on each line.
Continue until the current value is 20
(2 marks)
Inputs:
none

Outputs:
Example:
2
4
6
8
10
...
"""
import time
import random

count = 2

while True:
    print(count)
    delay = random.random() + 1
    count = count + 2
    if count > 20:
        break

print('\n' "Thats 20!")