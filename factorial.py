# Python 3 program to find
# factorial of given number
import math

# math's implementation of factorial, probably better than mine!
def factorial_steroids(n):
    return(math.factorial(n))

# My implementation of factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
