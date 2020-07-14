from math import factorial
from myFunctionsG import execute_this, split_stuff as split


@execute_this
def Problem_20():
    print(sum(split(factorial(100))))
