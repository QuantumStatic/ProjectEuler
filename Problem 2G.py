from myFunctionsG import execute_this
from math import sqrt, floor


@execute_this
def Problem_2():

    def fib(n):
        return floor(pow((1 + sqrt(5)) / 2, n) / sqrt(5) + 0.5)

    num, Answer = 1, int()
    while (n:= fib(num)) < 4000000:
        if n % 2 == 0:
            Answer += n
        num += 1

    print(Answer)
