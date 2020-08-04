# Runtime - 85 milliseconds (0.085 seconds)
from myFunctionsG import prime_checker as isprime, execute_this, sieveErato


@execute_this
def Problem_7():
    Noprimes, num = len(sieveErato(25000)), 25001

    while Noprimes <= 10001:
        num += 2
        if isprime(num):
            Noprimes += 1
    print(num)