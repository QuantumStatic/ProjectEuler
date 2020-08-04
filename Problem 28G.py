from myFunctionsG import execute_this

@execute_this
def Problem_28():

    current_number, Sum = 1, 1
    for x in range(2, 1001, 2):
        for y in range(4):
            current_number += x
            Sum += current_number
    print(Sum)