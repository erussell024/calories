import os, sys, datetime, csv
import pandas as pd

cals, p, f, c = 0, 0, 0, 0
foodList = []
calDict = {}

# Read in CSV - Desktop
#csvList = pd.read_csv(r'C:\Users\eruss\Desktop\git\calories\Food.txt', header=0)

# Read in CSV - Mobile
csvList = pd.read_csv(r'/storage/emulated/0/Python/Food.txt', header=0)

# Populate calDict[index] = cals where index = num for user choice
# calDict[index] = food, cals, p, f, c
for index, row in csvList.iterrows():
    calDict[str(index)] = [row[0], row[1], row[2], row[3], row[4]]

def menu():
    choice = str(input("""
Choose item: 
> """))
    return choice

while True:
    print(csvList)
    print("\nCalories: ", cals)
    choice = menu()

    # Exit condition
    if choice == 'q':
        break
    # Add misc calories               
    elif choice == 'a':
        misc = int(input("Enter misc calories: "))
        cals += misc
    # All other options
    else:
        cals += calDict.get(str(choice))[1]
        p += calDict.get(str(choice))[2]
        f += calDict.get(str(choice))[3]
        c += calDict.get(str(choice))[4]
        foodList.append(calDict.get(str(choice))[0])

# Write to file
# Overwrites files of the same date
def writeFile(foodList):
    now = datetime.datetime.now()
    date = now.strftime("%m-%d-%Y")

    # File location for Desktop
    #file = open(r"C:\Users\eruss\Desktop\git\calories\{}_Calories.txt".format(date), "w")

    # File location for mobile
    file=open("/storage/emulated/0/Python/Calories/{}_Calories.txt".format(date), "w")

    file.write(str("Calories: {}\n".format(cals)))
    file.write(str("Protein: {}\n".format(p)))
    file.write(str("Fat: {}\n".format(f)))
    file.write(str("Carbs: {}\n".format(c)))
    for item in foodList:
       file.write("%s\n" % item)
    print("\nOutput written to /storage/emulated/0/Python/Calories/")

writeFile(foodList)