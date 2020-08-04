# Runtime - 1 microsecond (0.000001 seconds)
from myFunctionsG import execute_this


@execute_this
def Problem_6():
    num = 100
    print(abs((num*(num+1)*(2*num+1)//6) - (pow(num*(num+1)//2, 2))))