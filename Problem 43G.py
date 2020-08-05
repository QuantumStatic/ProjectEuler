from myFunctionsG import sieveErato, execute_this, combine_list
from itertools import permutations


@execute_this
def Problem_43():
    pandigital_num, Sum, primes = combine_list(
        list(permutations([x for x in range(10)]))), int(), sieveErato(18)
    for num in pandigital_num:
        for x in range(1, 8):  # len(num)-2, otherwise in the next loop, index will go out of range
            if int(str(num)[x:x+3]) % primes[x-1] != 0:
                break
        else:  # if it didn't break till now, it satisfies it
            Sum += num
    print(Sum)
