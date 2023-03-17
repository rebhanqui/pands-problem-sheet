#REF 1: http://www.andreamarino.it/python/thinkcspy/MoreAboutIteration/Newton%27sMethod.html
# defining numbers as whatever is input by user
numbers = int(input("Please pick a number: "))

#function to apply the newton method of getting the square root
def newtonSqrt(numbers):
    approx = 0.5 * numbers
    better = 0.5 * (approx + numbers/approx)
    
    while better != approx:
        approx = better
    better = 0.5 * (approx + numbers/approx)

    return approx
#allows result of input calculate by .5 to be further calculated to get the sqrt

print(f"The Square Root of {numbers} is approx. {newtonSqrt(numbers)}")
#prints th euser input number and the result of the function

    
    

#repeats process until users selects