#3rd program as part of Lab 3.1
#This program reads in two numbers, divides them and gives the result as an integer and a remainder
#Author: OOS

first_number = int(input("Input your first number: "))
second_number = int(input("Input your second number: "))
answer = first_number / second_number
remainder = first_number % second_number
print("{} divided by {} is {} with a {} remainder".format(first_number,second_number,answer,remainder)) # Taken directly from Lab 3.1 notes