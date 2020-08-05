# Runtime - 1 second 800 milliseconds (1.8 seconds)
from myFunctions import execute_this, sieveErato, prime_checker as isprime


@execute_this
def Problem_50():
    primes, chain, greatestPrime = sieveErato(500_000), int(), int()
    z = len(primes)
    for x in range(z - 21):
        if chain > z - x:
            break
        sumPrimes = int()
        for y in range(x, z):
            sumPrimes += primes[y]
            if sumPrimes > 1_000_000:
                break
            if isprime(sumPrimes) and y-x > chain:
                chain = y-x
                greatestPrime = sumPrimes
    print(greatestPrime)
