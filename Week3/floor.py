#This program is the third of Lab 3.2
#This program rounds a floating number downwards
#Author: OOS

import math
number = float(input("Input a decimal number: "))
floor_number = math.floor(number)
print("{} rounded down is {}".format(number, floor_number))