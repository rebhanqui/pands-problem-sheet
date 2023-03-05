# pands-problem-sheet

```text
{
    "Course": "KDATG_L08_Y1",
    "Author": "Rebecca Hannah Quinn",
    "Student Number": G00425671
}
```

[1]

A collection of Weekly Tasks set in the PANDS Module

## List of Contents

1. **Hello World**

`print("helloworld")`

`# is this thing on?`

>Prints the text *hellowworld* when called in terminal via - `python helloworld.py`

---

2. **Accounts**

>Program that reads in 10 digits and outputs same digits with only last 4 showing and first 6 replaced with X's


`account_raw = input("Please enter your 10 digit account number: ")`
>Takes in the users account number

`account_secure = (f"Account number: XXXXXX{account_raw[-4:]}")`
`print(account_secure)`
>Confirms last 4 digits of account while hiding the first 6 digits via index and prints the result
---

3. **Bank**

>This program prompts user to input 2 amounts, adds both and prints output to user

`bankIn = int(input("Lodgement Amount 1: "))
bankIn2= int(input("Lodgement Amount 2: "))`
>Input 1 and 2 take in a number and change it to a int to then be added [2]

#add both int numbers
totalLodgement = (bankIn + bankIn2)

# converts input to euro and cents with the decimal point
# ref: https://stackoverflow.com/questions/46189874/python-find-the-dollar-and-cent USR: YOHAN DE ROSE
euroCents = (totalLodgement/100)

#euro and cent amount output to user with trailing zero kept so cent amounts with '0' in them stay visible
# '%.2f' ref5: https://stackoverflow.com/questions/15238120/keep-trailing-zeroes-in-python USR: eyquem
print(f"You have lodged €{('%.2f' % euroCents)}\nThank You!")
---

4.

---

5.

---

6.

---

### References

[1]: https://www.markdownguide.org/basic-syntax/ "Markdown Cheat Sheet"

[2]: https://vlegalwaymayo.atu.ie/pluginfile.php/857748/mod_label/intro/lab%202.2%20First%20Programs.pdf?time=1675120017388 "First Programs"