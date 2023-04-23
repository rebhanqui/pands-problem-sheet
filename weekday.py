#author: rebecca quinn
#program that tells if weekday or weekend

from datetime import datetime
#allows you to use current date/day/time in following code


#takes the day number from weekday
weeknum = datetime.today().weekday()

if weeknum < 5: 
    #0-5=weekdays
    print("Unfortunately, today is a weekday")
else:
    #5=Sat, 6=Sund
    print("YAY! It's the weekend!")