"""input integer output factorial
factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
print(factorial(int(input())))

he is using a lambda function http://www.secnetix.de/olli/Python/lambda_functions.hawk

In short it is a one-line anonymous function that returns a value. 
In the second line he hands over the value from stdin and computes the factorial. Very nice. 
IMHO lambdas aren't as readable as conventional functions in this case though.
"""



def factorial(n): #din save immediate answers Big O is exponetial
     if n<=1:
          return 1
     else:
        n2 = n * factorial(n-1)
        return n2

n= int(input())
print(factorial(n))
