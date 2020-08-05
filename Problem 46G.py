#Runtime - 500 milliseconds (0.5 seconds)
from myFunctions import execute_this, sieveErato
from math import sqrt


@execute_this
def Problem_46():
    num = 51
    while True:
        primes = sieveErato(num)
        if num == primes.pop():
            num += 2
            continue
        for prime in reversed(primes):
            shouldbeSquare = num - prime
            if sqrt(shouldbeSquare/2).is_integer():
                break
        else:
            print(num)
            break
        num += 2
