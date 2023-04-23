#creates function to run collatz sequence
#Author: Rebecca Quinn

def collatz(number):
#takes positive int and divides by two until odd number
    if (number % 2 == 0):
        return number // 2
#if odd number then multiple by 3 and add 1
    elif (number % 2 == 1):
        return number * 3 + 1
    else :
        print("ERROR")
        return None
#user input of positive int   
print("Enter a number. ")
number = int(input())
print(number)
#end when result gets to 1
while (number != 1):
    number = collatz(number)
    print(number)
print(number)
    
      
        

