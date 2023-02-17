#Following Lecture 1 of Week 4
#Messing around with if, elif statements
#Author: OOS

grade = 45

if(grade < 40):
    print("you have a fail")
if grade >= 40 and grade <=50 :
    print("You have a D")

c = 34
if isinstance (c, int) and c == 1:
    print (f"c is {c}")
else:
 print (f"c is equal to {c}")

 d = 4
if d<0:
    print(f"D is less than 0")
elif d>15:
    print("d is positive")
else:
    if d>0 and d<10:
        print("D is between 0 and 15")
