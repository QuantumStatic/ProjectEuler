from myFunctionsG import execute_this, prime_checker as isprime
from math import sqrt, ceil


@execute_this
def Problem_3():

    initNum = ceil(sqrt(600851475143))
    for x in range(initNum, 1, -2):
        if 600851475143 % x == 0 and isprime(x) is True:
            print(x)
            break
