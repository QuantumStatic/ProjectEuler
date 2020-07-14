# Added comments after discussing with @AbhimanyuBhati
from math import sqrt, ceil
from myFunctionsG import execute_this


@execute_this
def Problem_12():
    n, number_of_factors = 1, int()
    while number_of_factors <= 250:
        number_of_factors, factor, n_triangular_number = 0, 1, (n * n + n) // 2
        endPoint = ceil(sqrt(n_triangular_number))
        while factor < endPoint:
            if n_triangular_number % factor == 0:  # I am doing this because, sieve of eratothenes says that, root of a number is the midpoint, that seperates its factors into 2 equal halves
                number_of_factors += 1
            factor += 1
        n += 1
    print(n_triangular_number)
