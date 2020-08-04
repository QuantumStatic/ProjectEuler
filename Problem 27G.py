#Runtime - 250 milliseconds (0.250 seconds)
from myFunctionsG import execute_this, prime_checker as isprime, sieveEratoAlt as generatePrimes


@execute_this
def Problem_27():

    bestResult = {"MaximumPrimes": int(), "Product": int()}

    def quadraticiterator(a, b):
        num = 0
        while True:
            yield (num ** 2 + a * num + b)
            num += 1

    for a in generatePrimes(1000):
        for b in generatePrimes(1000):
            primesFound = 0
            for x in quadraticiterator(a, b):
                if isprime(x):
                    primesFound += 1
                else:
                    break

            if primesFound > bestResult["MaximumPrimes"]:
                bestResult["MaximumPrimes"], bestResult["Product"] = primesFound, a*b

            primesFound = 0
            for x in quadraticiterator(-a, b):
                if isprime(x):
                    primesFound += 1
                else:
                    break

            if primesFound > bestResult["MaximumPrimes"]:
                bestResult["MaximumPrimes"], bestResult["Product"] = primesFound, -a*b

    print(bestResult)
