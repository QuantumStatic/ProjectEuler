from myFunctionsG import execute_this, combine_list
from itertools import permutations


@execute_this
def Problem_24():
    perm = list(permutations([x for x in range(10)]))
    perm.sort()
    print(combine_list(perm[999999]))
