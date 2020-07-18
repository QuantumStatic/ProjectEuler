# previous version wasn't that fast. After discussion with @aarnavg17, decided to use a dictionary
from myFunctionsG import execute_this


@execute_this
def Problem_14():
    register = {1: 0, 2: 1}

    def collatz(num):
        if num in register.keys():
            return (register[num])

        register[num] = (2 + collatz((3*num + 1) //2)) if num % 2 else (1 + collatz(num // 2))

        return (register[num])

    longestChain, biggestNum = int(), int()
    for n in range(3, 1_000_000):
        if (currChain:=collatz(n)) > longestChain:
            longestChain = currChain
            biggestNum = n

    print(biggestNum)
