# I've been stuck on this problems for quite some while. This is particular implementation is based on a different code by @gayshot27.
# Runtime - 1 second 500 milliseconds (1.5 seconds)
from myFunctionsG import execute_this
from random import choice


@execute_this
def Problem_31():
    denominations, count = (1, 2, 5, 10, 20, 50, 100, 200), int()

    def MethodFinder(currentConstruction, currentDenomination):
        if currentConstruction == 200:
            nonlocal count
            count += 1
            return

    for x in range(currentDenomination, 7):
        if currentConstruction + denominations[x] > 200:
            return
        MethodFinder(currentConstruction + denominations[x], x)

    MethodFinder(0, 0)
    print(count + 1)
