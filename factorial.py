"""input integer output factorial
factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
print(factorial(int(input())))

he is using a lambda function http://www.secnetix.de/olli/Python/lambda_functions.hawk

In short it is a one-line anonymous function that returns a value. 
In the second line he hands over the value from stdin and computes the factorial. Very nice. 
IMHO lambdas aren't as readable as conventional functions in this case though.
"""
import math
import os
import random
import re
import sys



def factorial(n): #din save immediate answers Big O is exponetial
     if n<=1:
          return 1
     else:
        n2 = n * factorial(n-1)
        return n2





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
