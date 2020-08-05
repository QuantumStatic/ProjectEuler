#Runtime - 9.5 milliseconds (0.0095 seconds)
from myFunctions import execute_this


@execute_this
def Problem_48():
    finalSum = int()
    for num in range(1000):
        finalSum += pow(num + 1, num + 1)
    print(''.join(reversed(str(finalSum)[:-11:-1])))
