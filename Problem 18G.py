# this question couldn't ever be completed if not for Rishi Sekhar (@gayshot27).
# Runtime - 15 microseconds (0.000015 seconds)
from myFunctionsG import execute_this


@execute_this
def Problem_18():

    nums = '''
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
    '''.split('\n')

    rows, numbers = len(nums) - 2, list()
    for x in range(1, rows+1):
        numbers.extend(nums[x].split())
    del nums

    numbers, triangle = list(map(int, numbers)), list()

    for x in range(rows):
        triangle.append(numbers[:x+1])  # breaks into rows of the triangle
        numbers = numbers[x+1:]  # Removing the first element of the list

    for row in triangle[-2::-1]:  # Always choosing the second last row of triangle
        nextrow = triangle[-1]
        for x in range(len(row)):
            # Adding the larger element directly below it.
            row[x] += max(nextrow[x], nextrow[x + 1])
        triangle.pop()

    print(triangle[0][0])
