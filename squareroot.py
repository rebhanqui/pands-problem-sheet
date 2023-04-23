#defining number variable as whatever is input by user
#Author Rebecca Quinn

#user input defineing var n
n = int(input("Please pick a number: "))

#function to apply the newton method of getting the square root
def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return approx
#allows result of input calculate by .5 to be further calculated to get the sqrt

print(f"The Square Root of {n} is approx. {newtonsqrt(n)}")
#prints the user input number and the result of the function concantenated