# Runtime - 66 milliseconds (0.066 seconds)
from myFunctionsG import execute_this, split_stuff
from math import factorial

@execute_this
def Problem_34():

    def factorialSum(number):
        return sum(map(factorial, split_stuff(number)))

    number, Sum = 3, 0
    while number < 40586:
        if factorialSum(number) == number:
            Sum += number
        number += 1
    print(Sum)