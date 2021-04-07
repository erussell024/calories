import os
import sys
import datetime

# Food
totalCals = 0
tmp = 0
numOf = 1
eggSand = 690
whey = 110
spicySand = 540
strip = 410
fry= 600
cashewBar = 160
mixedVeggie = 200 # With some butter
beer = 150
dirtyChai = 310
cheese = 80
crackers = 17.5 # 1 cracker
burrito = 1000
egg = 70

food = [tmp, eggSand, whey, spicySand, strip, fry, cashewBar, mixedVeggie, beer, dirtyChai, crackers, burrito, egg]
foodToday = []

calDict = {
    "": "",
    "Egg Sandwich": food[1],
    "Whey": food[2],
    "Spicy Chicken Deluxe": food[3],
    "4ct Strip": food[4],
    "Large Fry": food[5],
    "Cashew Bar": food[6],
    "Mixed Veggie w/butter": food[7],
    "Beer": food[8],
    "Dirty Chai": food[9],
    "Cracker": food[10],
    "Burrito": food[11],
    "Egg": food[12]
}

ingredientDict = {
    "Egg Sandwhich": "2x eggs | 4x bacon | 1x cheese | 1x cinnamon rasin bagel"
}

# Overwrites files of the same date | look for way to add 
# numOf to the file
def writeFile(food):
    now = datetime.datetime.now()
    date = now.strftime("%m-%d-%Y")
    f=open("/storage/emulated/0/Python/Calories/{}_Calories.txt".format(date), "w")
    f.write(str("Calories: {}".format(totalCals)))
    f.write("\n")
    for item in food:
       f.write("%s\n" % item)
    print("Output written to /storage/emulated/0/Python/Calories/calories.txt")
    
def menu():
    choice = input("""
Choose item: 
0.  Calorie List
1.  Egg Sandwich
2.  Whey
3.  Spicy Chicken Deluxe
4.  4ct Strip
5.  Large Fry
6.  Cashew Bar
7.  Mixed Veggies w/butter
8.  Beer
9.  Dirty Chai
10. Crackers & Cheese
11. Burrito
12. Egg
'n' To exit
> """)
    return choice
     
while True:
    print("\nCalories: ", totalCals)
    choice = menu()
    
    # Exit condition
    if choice == 'n':
        break
               
    # Multiples of an option 
    elif choice == '2' or choice == '6' or choice == '8' or choice == '10' or choice == '12':
        numOf = int(input("How many: "))
        if choice == '2':
            totalCals += (numOf * whey)
        if choice == '6':
            totalCals += (numOf * cashewBar)
        if choice == '8':
            totalCals += (numOf * beer)
        if choice == '10':
            numCheese = int(input("How many cheese: "))
            totalCals += ((numOf * crackers) + (numCheese * cheese))
        if choice == '12':
            totalCals += (numOf * egg)
        foodToday.append(list(calDict.keys())[int(choice)])
		
    # Display Calorie List
    elif choice == '0':
        print("\nCalorie List: \n")
        print("Food".center(10), "Calories".rjust(23))
        print("-".ljust(34, "-"))
        for key, value in calDict.items():
            print(key.ljust(25), "|", value, "\n-".ljust(35, "-"))
        print()

    # All other options
    else:
        totalCals += food[int(choice)]
        foodToday.append(list(calDict.keys())[int(choice)])
		
writeFile(foodToday)