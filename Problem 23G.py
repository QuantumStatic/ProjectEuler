from math import sqrt, floor
from myFunctionsG import prime_checker as isprime, execute_this


@execute_this
def Problem_23():

    def abundant(num):
        if isprime(num):
            return False
        factor, SumOfFactors, endPoint = 2, 1, floor(sqrt(num))+1
        while factor < endPoint:
            if not (num % factor):
                SumOfFactors += factor + num // factor
            factor += 1
        temp = sqrt(num)
        if temp.is_integer():
            SumOfFactors -= temp
        if SumOfFactors > num:
            return True
        return False

    all_nums = [x for x in range(28123)]
    abundant_numbers = tuple(filter(abundant, all_nums[12:]))
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            if (temp := abundant_numbers[i] + abundant_numbers[j]) < 28123:
                all_nums[temp] = 0
    print(sum(all_nums))
