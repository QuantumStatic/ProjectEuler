#Runtime - 116 milliseconds (0.116 seconds)
from myFunctions import execute_this, split_stuff, remove_duplicates_from
from math import ceil, floor


@execute_this
def Problem_32():
    def digit_checker(a, b, c):
        a, b, c, all_characters = str(a), str(b), str(c), list()
        all_characters.extend(split_stuff(a))
        all_characters.extend(split_stuff(b))
        all_characters.extend(split_stuff(c))
        all_characters = remove_duplicates_from(all_characters)
        try:
            all_characters.remove('0')
        finally:
            return len(all_characters)

    products = set()

    for a in range(100, 3500):
        for b in range(4, ceil(10000 / a)):
            if digit_checker(a, b, floor(a*b)) == 9:
                products.add(floor(a*b))

    print (sum(products))
