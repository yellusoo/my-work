#This program is the final or fourth program of Lab 3.2
#This program takes input of a currency amount and outputs the absolute amount in cent.
#Author: OOS

amount = float(input("Enter amount here:"))
abs_amount = abs(amount)
cent_amount = int(abs_amount * 100)
print("That amount in cents is {}".format(cent_amount))