import math
import sys
'''
Made a program that calculates the limit of a prespecified function through recursion, it was made on a whim so please excuse any errors

    Since we know the amount of radioactive material, given x amount is added every [arbitrary unit of time], follows this formula:
    x(k^1 + k^2 + k^3 + ... + k^n), where k is 2^-1/22.3 since half life is 22.3 years, and matter is added every 1 year.
'''

def function(n):
    function = 30000*pow(2,-n/22.3)

    return function


def limit(n, value):

    n += 1

    function_value = function(n)
    
    value += function_value

    # prints value every 50 iteration
    if n % 50 == 0:
        print(f'n = {n}: {value}')

    # once iteration 900 is hit, we return
    if n == 900:
        return value

    return limit(n, value)


def main():

    # manually setting the recursion limit does not work, as such, 900 is used, which is good enough.
    sys.setrecursionlimit(1000)

    n = 0

    function_print = "30000*2^(-n/22.3)"

    print("Initial function:", function_print)
    
    # n = 0 in the summation happens from the getgo.
    limit_value = limit(n, function(n)) 

    print(f'limit: {limit_value}')
    

if __name__ == '__main__':
    main()
    