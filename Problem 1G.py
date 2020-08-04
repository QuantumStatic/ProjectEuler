# Improvemnts suggested by @aarnavg17
# Runtime - 1.1 microseconds (0.0000011 seconds)
from myFunctionsG import execute_this


@execute_this
def Problem_1():
    FinalSum, endPoint, firstNum, lastNum = int(), 999, 3, int()

    temp = endPoint
    while temp:
        if temp % firstNum == 0:
            lastNum = temp
            break
        temp -= 1
    else:
        lastNum = 0
    FinalSum += lastNum * (firstNum + lastNum) // (2 * firstNum)

    firstNum, temp = 5, endPoint
    while temp:
        if temp % firstNum == 0:
            lastNum = temp
            break
        temp -= 1
    else:
        lastNum = 0
    FinalSum += lastNum * (firstNum + lastNum) // (2 * firstNum)

    firstNum, temp = 15, endPoint
    while temp:
        if temp % firstNum == 0:
            lastNum = temp
            break
        temp -= 1
    else:
        lastNum = 0
    FinalSum -= lastNum * (firstNum + lastNum) // (2 * firstNum)

    print(FinalSum)
