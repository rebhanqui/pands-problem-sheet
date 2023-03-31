# bank.py 
#prompts user to input 2 amounts, adds both and prints output to user
# Author: Rebecca Quinn

#input 1 and 2 take in a number and change it to a int to then be added on line 11
# ref6: https://vlegalwaymayo.atu.ie/pluginfile.php/857748/mod_label/intro/lab%202.2%20First%20Programs.pdf?time=1675120017388
bankIn = int(input("Lodgement Amount 1: "))
bankIn2= int(input("Lodgement Amount 2: "))

#add both int numbers
totalLodgement = (bankIn + bankIn2)

# converts input to euro and cents with the decimal point
# ref: https://stackoverflow.com/questions/46189874/python-find-the-dollar-and-cent USR: YOHAN DE ROSE
euroCents = (totalLodgement/100)

#euro and cent amount output to user with trailing zero kept so cent amounts with '0' in them stay visible
# '%.2f' ref5: https://stackoverflow.com/questions/15238120/keep-trailing-zeroes-in-python USR: eyquem
print(f"You have lodged €{('%.2f' % euroCents)}\nThank You!")

