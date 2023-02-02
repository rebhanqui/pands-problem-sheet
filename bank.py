# bank.py 
#prompts user to input 2 amounts, adds both and prints output to user
# Author: Rebecca Hannah Quinn

#input 1
bankIn = int(input("Lodgement Amount 1: "))

#input 2
bankIn2= int(input("Lodgement Amount 2: "))

#add both int numbers
totalLodgement = (bankIn + bankIn2)

# ALL BELOW ARE ATTEMPTING TO PRINT INPUT NUMBERS AS EURO AND CENTS

# ref: https://stackoverflow.com/questions/46189874/python-find-the-dollar-and-cent USR: YOHAN DE ROSE
# euroCents = (totalLodgement/100)

# ref3: https://stackoverflow.com/questions/70080676/how-do-i-print-cents-as-decimals
# sum = euroCents / 100.0

# ref2: https://stackoverflow.com/questions/33861401/convert-cents-to-euro USR: PAN GALATIC
# def price(euroCents):
    # return (euro / 100.0)

# ref4: https://stackabuse.com/format-number-as-currency-string-in-python/ AUTH: DANIEL PIMEH
# import babel.numbers
# babel.numbers.format_currency(euroCents, "EUR", locale='en_US')

# converts input to euro and cents
euroCents = (totalLodgement)/100

#euro and cent amount output to user
# '%.2f' ref5: https://stackoverflow.com/questions/15238120/keep-trailing-zeroes-in-python USR: eyquem
print(f"You have lodged €{('%.2f' % euroCents)}\nThank You!")

# LOCALE CHECK - GO BACK LATER
#avail_loc = babel.localedata.locale_identifiers()
#print(avail_loc)
