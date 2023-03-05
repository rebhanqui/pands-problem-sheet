# pands-problem-sheet

Course: KDATG_L08_Y1
Author: Rebecca Hannah Quinn
Student Number: G00425671

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

5.

---

6.

---

### References

[^1]: https://www.markdownguide.org/basic-syntax/ "Markdown Cheat Sheet"

[^2]: https://vlegalwaymayo.atu.ie/pluginfile.php/857748/mod_label/intro/lab%202.2%20First%20Programs.pdf?time=1675120017388 "First Programs"

[^3]: https://stackoverflow.com/questions/46189874/python-find-the-dollar-and-cent "How to get Dollar Cent - User: YOHAN DE ROSE"

[^4]: https://stackoverflow.com/questions/15238120/keep-trailing-zeroes-in-python "How to keep trailing Zeros - User: eyquem"

[^5]: https://youtu.be/lAp_5qTdOhM "Collatz Sequence Algorithm in Python @ 1:30"