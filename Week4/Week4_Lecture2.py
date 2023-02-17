#This program follows Lecture 2 of Week 4
#This program tests while statements
#Author: OOS

count = 0
while (count<10):
    print ("Count is", count)
    count = count + 1

print ("Count is ending at", count)

count = 10
while (count >= 0):
    print("Countdown", count)
    count -= 1
print("Boom")


#Sentinel Control Loop - Doing something until something happens

value = input("Input Q to quit")
while value != "Q":
    print("Press Q ")
    value = input("Input Q:")
print ("All done")
