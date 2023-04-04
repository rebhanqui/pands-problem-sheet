# Pands Problem Sheet - HDIP in Data Analytics 2023

| Info | Details |
| -------- | -------- |
| Course: | KDATG_L08_Y1 |
| Author: | Rebecca Hannah Quinn |
| Student Number: | G00425671 |

[^1]

A collection of Weekly Tasks set in the PANDS Module

## List of Contents

1. Hello World

`print("helloworld")`

`# is this thing on?`

>Prints the text *hellowworld* when called in terminal via - `python helloworld.py`

---

2. Accounts

>Program that reads in 10 digits and outputs same digits with only last 4 showing and first 6 replaced with X's


`account_raw = input("Please enter your 10 digit account number: ")`
>Takes in the users account number

```python

account_secure = (f"Account number: XXXXXX{account_raw[-4:]}")
print(account_secure)

```
>Confirms last 4 digits of account while hiding the first 6 digits via index and prints the result
---

3. Bank

>This program prompts user to input 2 amounts, adds both and prints output to user

```python

bankIn = int(input("Lodgement Amount 1: "))
bankIn2= int(input("Lodgement Amount 2: "))

```

>Input 1 and 2 take in a number and change it to a int to then be added [^2]

`totalLodgement = (bankIn + bankIn2)`
>Add both int numbers

`euroCents = (totalLodgement/100)`
>Converts input to euro and cents with the decimal point [^3]

`print(f"You have lodged €{('%.2f' % euroCents)}\nThank You!")`
>Euro and cent amount output to user with trailing zero kept so cent amounts with '0' in them stay visible [^4]
---

4. Collatz


`def collatz(number):`
>Creates function to run following collatz sequence [^5] 

`if (number % 2 == 0):`
    `return number // 2`
>Takes positive int and divides by two until odd number 


```python

elif (number % 2 == 1):
    return number * 3 + 1
else :
    print("ERROR")
    return None

```

>When encountering an odd number then program multiplies by 3 and adds 1 

```python

print("Enter a number. ")
number = int(input())
print(number)

```

>User input of int 

```python

while (number != 1):
   number = collatz(number)
   print(number)
print(number)

```

>Ends when result gets to 1

---

5. Weekday

>Prints one of two results depend if it is a weekday or not.

```python

print("Yes, unfortunately today is a weekday")
print("It is the weekend, yay!")

```

>By using import date the code can tell what the current day is without import. [^6]

```python

import datetime

```

>By giving the function perameters, if its not monday Friday (0-5) then it is the weekend

```python

while datetime == range(0, 5):

```

---

6. Squareroot

```python

numbers = int(input("Please pick a number: "))

```

>A function to find the square root of any number input by user
>The function below applies the newton method of getting the square root

```python

def newtonSqrt(numbers): 
    approx = 0.5 * numbers
    better = 0.5 * (approx + numbers/approx)
    
    while better != approx:
        approx = better
    better = 0.5 * (approx + numbers/approx)

    return approx

```

>The numbers variable is the parameter to facilitate the square root calculation
While function allows the input eventually be multiplied by .5 to be further calculated to get the square root

---

7. Read E's



---

8. Plottask



---

### References

[^1]: https://www.markdownguide.org/basic-syntax/ "Markdown Cheat Sheet"

[^2]: https://vlegalwaymayo.atu.ie/pluginfile.php/857748/mod_label/intro/lab%202.2%20First%20Programs.pdf?time=1675120017388 "First Programs"

[^3]: https://stackoverflow.com/questions/46189874/python-find-the-dollar-and-cent "How to get Dollar Cent - User: YOHAN DE ROSE"

[^4]: https://stackoverflow.com/questions/15238120/keep-trailing-zeroes-in-python "How to keep trailing Zeros - User: eyquem"

[^5]: https://youtu.be/lAp_5qTdOhM "Collatz Sequence Algorithm in Python @ 1:30"

[^6]: https://www.w3schools.com/python/python_datetime.asp "Date Time Import"
