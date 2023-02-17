#Week 4, Lab 1 2nd program
#This program checks a students grade and reports their result
#Author: OOS

grade = float(input("Input your grade here:"))

grade2 = round(grade)

if grade2 < 0 or grade >100:
    print("Error; Try again")

if grade2 < 40:
    print("Fail")
if grade2 >=40 and grade <=49:
    print("Pass")
if grade2 >49 and grade <=59:
    print("Merit 2")
if grade2 >59 and grade <=69:
    print("Merit 1")
if grade2 >=70 and grade < 100:
    print("Distinction")