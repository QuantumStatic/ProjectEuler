from myFunctionsG import execute_it


@execute_it
def Problem_6():
    num = 100
    print(abs((num*(num+1)*(2*num+1)//6) - (pow(num*(num+1)//2, 2))))
