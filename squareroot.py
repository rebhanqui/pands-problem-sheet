#REF 1: https://www.cuemath.com/algebra/squares-and-square-roots/
numbers = int(input("Please pick a number: "))


def newtonSqrt(numbers):
    approx = 0.5 * numbers
    better = 0.5 * (approx + numbers/approx)
    
    while better != approx:
        approx = better
    better = 0.5 * (approx + numbers/approx)

    return approx

print(f"The Square Root of {numbers} is approx. {newtonSqrt(numbers)}")


    
    

#repeats process until users selects