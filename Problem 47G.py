# Runtime - 265 milliseconds (0.265 seconds)
from myFunctions import prime_factoriser as pf, execute_this, remove_duplicates_from as rdf
from math import factorial


@execute_this
def Problem_47():

    nums_to_find, factors_to_find = 4, 4

    def consecChecker(listIn, *alreadyChecked):
        conseCounter, gold, length = int(), list(), len(listIn)
        for x in range(length):
            if listIn[x] in alreadyChecked or distinctCount(pf(listIn[x])) == factors_to_find:
                conseCounter += 1
                gold.append(listIn[x])
                if conseCounter == nums_to_find:
                    return (gold)
                continue
            if length - x - 1 < nums_to_find:
                return None
            conseCounter = 0
            gold.clear()

    def distinctCount(listIn):
        return len(rdf(listIn))

    num, result = factorial(factors_to_find)+nums_to_find, list()
    while True:
        if distinctCount(pf(num)) == factors_to_find:
            left, right = distinctCount(pf(num - 1)), distinctCount(pf(num + 1))
            if left != factors_to_find and right != factors_to_find:
                num += 2 * (nums_to_find - 1)
                continue
            if left == factors_to_find and right == factors_to_find and (result:= consecChecker(tuple(x for x in range(num-nums_to_find+1, num+nums_to_find)), num-1, num, num+1)) is not None:
                print(result)
                break
            if left == factors_to_find and (result:= consecChecker(tuple(x for x in range(num-nums_to_find+1, num+1)), num-1, num)) is not None:
                print(result)
                break
            if right == factors_to_find and (result:= consecChecker(tuple(x for x in range(num, num+nums_to_find)), num, num+1)) is not None:
                print(result)
                break
        num += 2 * (nums_to_find - 1)
