#This is the second program of Lab 3.3
#This program inputs a string and removes spaces, then converts string to lower case
#Author: OOS

raw_string = str(input("Please write a word here:"))
normalise_string = raw_string.strip().lower()
print("The word is {} in proper English".format(normalise_string))

print("The length of your input is {}".format(len(raw_string)))
print("The length of the output is {}".format(len(normalise_string)))
print("THe string length has been reduced from {} to {} characters".format(len(raw_string),len(normalise_string)))