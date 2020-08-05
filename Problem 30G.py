# Runtime - 1 Second 30 milliseconds (1.030 seconds)
from myFunctionsG import execute_this, split_stuff


@execute_this
def Problem_30():

    def powerSum(number):
        return sum(map(lambda x: x ** 5, split_stuff(number)))

    number, Sum = 5**5, 0
    while number <= 5*9**5:
        if number == powerSum(number):
            Sum += number
        number += 1
    print(Sum)
