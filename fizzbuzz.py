#1.FizzBuzz
#Given a number n, for each integer i in the range from 1 to n inclusive, print one value per line as follows:
#If i is a multiple of both 3 and 5, print FizzBuzz
#if i is a multiple of 3 but not 5, print Fizz
#if i is a multiple of 5 not 4, print Buzz
#if i is not a multiple of 3 or 5, print the value of i
"""FizzBuzz in action. dont care double run
Print in ascending order set{1,2,... n}"""
#0<n<2 x 10^5

def fizzBuzz(n):
    for x in range(1, n+1): 
	#alternate while(x<n+1) x+=1. continue doesnt work.
	
        if x % 3 == 0 and x % 5 == 0 :
            print("FizzBuzz")
        if x % 3 == 0 and x % 5 !=0 :
            print("Fizz")
        if x % 5 == 0 and x % 3 != 0 :
            print("Buzz")
        if x % 3 != 0 and x % 5 != 0 :
            print(x)
            
    return 0

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)

