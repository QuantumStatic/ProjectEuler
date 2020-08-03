from myFunctionsG import execute_this, sieveErato


@execute_this
def Problem_26():

    primes, sequenceLength = tuple(reversed(sieveErato(1000))), int()

    for num in primes:
        value, pos, foundRemainders = 1, 0, [False] * num

        while foundRemainders[value] is False and value != 0:
            foundRemainders[value] = pos
            value = (value*10) % num
            pos += 1

        if pos > sequenceLength:
            if (sequenceLength := pos) >= primes[primes.index(num)+1]:
                print(num)
                break
