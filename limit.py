import math
import sys
'''
Made a program that calculates the limit of a prespecified function through recursion, it was made on a whim so please excuse any errors

    I somehow came up with a convergence at 29081.85... which i know not to be correct, since we're 
    allways adding another 30 metric tonnes of radioactive material, but at one point, the first material 
    that is added would have decayed almost completely, not mathematically, but material is descrete, and we 
    assume it to be gone by 10 life (99.9 of all material will then be gone https://gyazo.com/12db08e609335745f7dcac29296c3b46) 
    so at one point it should converge at SOMETHING.
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
    