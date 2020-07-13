from math import sqrt
from myFunctionsG import execute_this


@execute_this
def Problem_9():
    diff = 0.009
    for x in range(1, 295):
        for y in range(1, 1000):
            z = round(sqrt(x**2+y**2), 2)
            if abs(x+y+z-1000) < diff and abs(x-y) > 2 and abs(y-z) > 2 and abs(z-x) > 2:
                print(int(x * y * z))
                break
        else:
            continue
        break
