# Runtime - 3.3 milliseconds (0.0033 seconds)
from myFunctions import execute_this

@execute_this
def Problem_42():
    with open("Problem_42.txt") as set_of_names:
        names = set_of_names.read().split(','), 
    triang_num, word_count=list(), int()

    names = names[0]
    for x in range(len(names)):
        names[x] = names[x][1:len(names[x])-1]

    for x in range(1, 25):
        triang_num.append(int(0.5*x*(x+1)))

    for x in range(len(names)):
        Sum = int()
        for y in names[x]:
            Sum += ord(y)-64
        if Sum in triang_num:
            word_count += 1

    print(word_count)
