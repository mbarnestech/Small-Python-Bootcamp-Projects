# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!

#DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

# YOUR CODE GOES BELOW:

# using get():

quantity = bakery_stock.get(food)

if quantity==None:
    print("We don't make that")
else:
    print(f"{quantity} left")

# Answer using if _ in _;

if food in bakery_stock:
    print(f"{bakery_stock[food]} left")
else:
    print("We don't make that")