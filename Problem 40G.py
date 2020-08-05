# Runtime: 86 milliseconds (0.086 seconds)
from myFunctions import execute_this

@execute_this
def Problem_40():
    champernowne_string, num, pos, prod = "0.", 1, [2, 11, 101, 1001, 10001, 100001, 1000001], 1
    while True:
        champernowne_string += str(num)
        if len(champernowne_string) >= 1000002:
            break
        num += 1
    for x in pos:
        prod *= int(champernowne_string[x])
    print(prod)

