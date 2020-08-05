# Runtime - 630 milliseconds (0.630 seconds)
from myFunctions import list_substractor, sieveErato, prime_checker as isprime, remove_duplicates_from, execute_this
from collections import deque


@execute_this
def Problem_35():
    def number_rotator(number):
        number = deque(number)
        number.rotate(-1)
        return(''.join(number))

    list_of_normal_primes, circular_primes = list_substractor(sieveErato(1000000), sieveErato(10)), {2,3,5,7}

    for normal_prime in list_of_normal_primes:
        check_num, circular_prime_checker = str(normal_prime), 0
        for x in range(len(check_num)-1):
            check_num = number_rotator(check_num)
            if isprime(int(check_num)):
                circular_prime_checker += 1
                continue
            break
        if circular_prime_checker == len(str(normal_prime))-1:
            circular_primes.add(normal_prime)

    print(len(circular_primes))
