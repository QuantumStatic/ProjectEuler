# Runtime 33 milliseconds (0.033 seconds)
from math import sqrt, floor
from myFunctionsG import execute_this


@execute_this
def Problem_25():

    register, number = {0: 0, 1: 1, 2: 1}, 1

    def fib(n):
        try:
            return register[n]
        except:
            register[n] = fib(n-1)+fib(n-2)
        return register[n]

    while len(str(fib(number))) < 1000:
        number += 1

    print(number)
