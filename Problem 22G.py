#Runtime - 8 milliseconds (0.008 seconds)
from myFunctionsG import execute_this


@execute_this
def Problem_22():
    with open("Problem_22.txt") as file:
        name = file.read().split(',')
    final_sum = int()
    for x in range(len(name)):
        name[x] = name[x][1:len(name[x])-1]
    name.sort()
    for x in range(len(name)):
        curr_sum = int()
        for y in name[x]:
            curr_sum += ord(y)-64
        final_sum += curr_sum*(x+1)
    print(final_sum)
