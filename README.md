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

Program reads in users account number and outputs same digits with only last 4 showing with the rest hidden by #

> Takes in the users account number

```python
account_raw = input("Please enter your account number: ")
```

>Hides all digits except the last four no matter the account number length and prints the result[^2]

```python
account_safe = "".join(['#' for x in account_raw[:-4]]) + account_raw[-4:]
account_secure = (f"Account number: {account_safe}")
print(account_secure)
```

---

3. Bank

Prompts user to input 2 amounts in cents, adds both and prints output to user in Euros and Cents readable amount

>Input 1 and 2 take in a number and change it to a int to then be added and assigned to the totalLodgement var

```python
bankIn = int(input("Lodgement Amount 1 (in cents): "))
bankIn2= int(input("Lodgement Amount 2 (in cents): "))

totalLodgement = (bankIn + bankIn2)
```

>Converts input to euros first without reamining cents using int division

```python
eurosAmount = (totalLodgement//100)
```

>The remainder operator yields the last two digits using % 100 and prints the cents after euros taken [^3]

```python
centsAmount = (totalLodgement % 100)
```

>Prints the total amount

```python
print(f"You have lodged €{eurosAmount}.{centsAmount}\nThank You!")
```

---

4. Collatz

Program to run the collatz sequence using user input

>Input of positive int 

```python
print("Please enter a number: ") 
number = int(input())
#end="" ensures numbers are laid out left to right rather than vertically
print(number, end=" ")
``` 

[^4]

>Function creation and using it on the user input

```python
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
```

[^5]

>While loop to end function when the user input gets to 1 and prints results including user input from above

```python
while (number != 1):
    number = collatz(number)
    print(number, end=" ")
print(number)
```

---

5. Weekday

>Prints one of two results depend if it is a weekday or not.

```python
from datetime import datetime
```
>Allows you to use current date/day/time in following code

>Takes the day number from weekday uses if else to determine if its a weekday (0-5) or weekend (5 and 6) [^6]

```python
weeknum = datetime.today().weekday() 

if weeknum < 5: 
    #0-5=weekdays
    print("Unfortunately, today is a weekday")
else:
    #5=Sat, 6=Sund
    print("YAY! It's the weekend!")
```

>Result depending on date as determined by device location and time [^7]

---

6. Squareroot [^8] [^9]

Program to define the root of user given number

>User input defineing var n

```py
n = int(input("Please pick a number: "))
```

>Function to apply the newton method in order to return the square root

```python
def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx
```

>Prints the user input number and the result of the function concantenated

```python
print(f"The Square Root of {n} is approx. {newtonsqrt(n)}")
```

---

7. Read E's

Program to count the number of the letter "E" in a text file, including both upper and lower case [^10] [^11]

>Creates a permanent file path

```python
FILENAME = "/Users/rebeccaquinn/Desktop/pands-problem-sheet/countfile.txt"
```

>Opens file and reads it with 'r'

```python
file = open(FILENAME, 'r') 
```

>Reads file, and counts number of letter in textfile above

```python
data = file.read()

#letter to count
letter = ("e")

#letter in bother cases
letterlower = ("e")
letterupper = ("E")

#count counts how many times the chosen letter occurs in both upper and lowercase
loweroccurences = data.count(letterlower)
upperoccurences = data.count(letterupper)

#combination of occurances of letter cases
occurences = int(loweroccurences + upperoccurences)

#prints result
print(f"There are {occurences} letter {letter}'s in the count file")
```

---

8. Plottask

Imports python packages to assist in plotting various charts and historgrams

```python
import numpy as np
import matplotlib.pyplot as plt
```

Distributuon is normal at 1000, mean is 5 and standard deviation is 2 for this historgram

```python
meanvalue = 5
standard = 2
distrib = 1000
x = np.random.normal(meanvalue, standard, distrib)
```

Arranging the histogram [^]

```python
xpoints = np.arange(0,11)

#x (xpoints) to the power of 3 using pow 
ypoints = pow(xpoints, 3,)
```

Styling the plot and historgram details [^]

```python
plt.figure(figsize=(14,7)) # size of fig 14x7
plt.style.use('seaborn-whitegrid') #grid style
plt.title("Plotting Plot")
```

Labels and further styling [^] [^]

```python
plt.hist(x, facecolor="cyan", edgecolor="white", label="X Data") # draw solid white grid lines
plt.plot(xpoints, ypoints, linewidth=5.0, color="pink", label="Y Data") 
plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=2.)
```

The commented out code saves the file and the end prints to screen without saving the result [^14]

```python
#plt.savefig("plottask.png")

plt.show()
```

---

### References

[^1]: https://www.markdownguide.org/basic-syntax/ "Markdown Cheat Sheet"

[^2]: https://stackoverflow.com/questions/40842451/how-do-i-use-the-replace-function-to-change-all-but-the-last-4-characters-of

[^3]: https://www.geeksforgeeks.org/python-operators/

[^4]: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

[^5]: https://youtu.be/lAp_5qTdOhM "Collatz Sequence Algorithm in Python @ 1:30"

[^6]: https://www.w3schools.com/python/python_datetime.asp "Date Time Import"

[^7]: https://www.niskayuna.org/sites/g/files/vyhlif4781/f/uploads/computercorner_do_you_know_what_time_it_is_and_does_your_pc_know_too.pdf

[^8]: https://medium.com/@sddkal/newton-square-root-method-in-python-270853e9185d

[^9]: http://www.andreamarino.it/python/thinkcspy/MoreAboutIteration/Newton%27sMethod.html

[^10]: https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/

[^11]: https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

[^]: https://medium.com/@arseniytyurin/how-to-make-your-histogram-shine-69e432be39ca

[^]: https://www.statology.org/matplotlib-line-thickness/

[^]: https://jakevdp.github.io/PythonDataScienceHandbook/04.11-settings-and-stylesheets.html

[^]: https://towardsdatascience.com/save-plots-matplotlib-1a16b3432d8a
