from myFunctions import prime_checker as isprime, execute_this, sieveErato


@execute_this
def Problem_7():
    Noprimes, num = len(sieveErato(20_000)), 20_001

    while Noprimes <= 10_001:
        num += 2
        if isprime(num):
            Noprimes += 1
    print(num)
