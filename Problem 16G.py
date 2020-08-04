# Runtime - 21.5 microseconds (0.0000215 seconds)
from myFunctionsG import execute_this, split_stuff as split


@execute_this
def Problem_16():
    number = split(pow(2, 1000))
    print(sum(number))
