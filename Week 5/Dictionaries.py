# Messing with Dictionaries Week 5 Lecture 2
#Author: OOS

car = {
    "makes" : "ford",
    "model" :"mondeo",
    "year" : "2005",
    "owner" : {
        "name": "Oisin",
        "driver_number" : "2243"},
    "price" : "10000"
}
#for key in car:
   # print(key, "has value", car[key])#

for key, value in car.items():
    print( key + "has a value of" + value)
