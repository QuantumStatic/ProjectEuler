# Question can be rephrased as in how many ways can I go right. If I go right, I would have to go down at some point. thinkin how many ways I can go down is the same thought process.
# Credits to @AbhimanyuBhati, for thinking in this direction before I did.
from myFunctionsG import execute_this
from math import comb


@execute_this
def Problem_15():
    number_of_sides = 20
    result = comb(number_of_sides*2, number_of_sides)
    print(result)
