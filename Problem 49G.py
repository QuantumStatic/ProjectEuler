# Runtime - 115 milliseconds (0.115 seconds)
from myFunctions import prime_checker as prime, combine_list as combine, execute_this
from itertools import permutations, combinations_with_replacement


@execute_this
def problem_49():

    def trioFinder(arg):
        for a in range(len(arg) - 2):
            for c in range(a + 2, len(arg)):
                if (arg[a] + arg[c]) // 2 in arg[a+1:c]:
                    print(arg[a], (arg[a] + arg[c]) // 2, arg[c])
                    return

    checked = list()
    for x in combinations_with_replacement(combine([str(x) for x in range(1, 10)]), 4):
        reqdNums = list()
        for y in permutations(combine(x)):
            permutedCandidate = int(combine(y))
            if permutedCandidate not in checked and prime(permutedCandidate):
                reqdNums.append(permutedCandidate)
                checked.append(permutedCandidate)
        if len(reqdNums) > 2:
            reqdNums.sort()
            trioFinder(tuple(reqdNums))
