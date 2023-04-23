# bank.py 
#prompts user to input 2 amounts, adds both and prints output to user
# Author: Rebecca Quinn

#input 1 and 2 take in a number and change it to a int to then be added on line 11

bankIn = int(input("Lodgement Amount 1: "))
bankIn2= int(input("Lodgement Amount 2: "))

#add both int numbers
totalLodgement = (bankIn + bankIn2)

# converts input to euro and cents with the decimal point using int division
eurosAmount = (totalLodgement//100)

#the remainder operator yields the last two digits using % 100 and prints the cents after euros taken
centsAmount = (totalLodgement % 100)

#euro and cent amount output to user with trailing zero kept so cent amounts with '0' in them stay visible
# '%.2f' 
print(f"You have lodged €{eurosAmount}.{centsAmount}\nThank You!")

