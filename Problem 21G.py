from math import ceil, sqrt
from myFunctionsG import prime_checker as prime, execute_this


@execute_this
def Problem_21():

    def sum_of_factors(num):
        factor, SumOfFactors, endPoint = 2, 1, ceil(sqrt(num))
        while factor <= endPoint:
            if not (num % factor):
                SumOfFactors += (factor + num // factor)
            factor += 1
        temp = sqrt(num)
        if temp.is_integer():
            SumOfFactors -= temp
        if SumOfFactors != num:
            return (SumOfFactors)
        return False

    def isAmicable(num):
        try:
            return (register[register[num]] == num)
        except:
            try:
                register[register[num]] = sum_of_factors(register[num])
                return (register[register[num]] == num)
            except:
                register[num] = sum_of_factors(num)
                register[register[num]] = sum_of_factors(register[num])
                return (register[register[num]] == num)

    Sum, number, register = 0, 3, dict()
    while number < 10000:
        if not prime(number) and isAmicable(number):
            Sum += number
        number += 1
    print(Sum)
