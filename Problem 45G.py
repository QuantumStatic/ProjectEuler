# Runtime - 13.5 milliseconds (0.0135 seconds)
from myFunctions import execute_this
from math import sqrt

@execute_this
def Problem_45():

    def quadratic_solver(a, b, c):
        return ((-b + sqrt(b**2 - 4*a*c)) / (2 * a), (-b - sqrt(b**2 - 4*a*c)) / (2 * a))
    
    def ispentagonal(num):
        result = (1 / 6) * (sqrt(24 * num + 1) + 1)
        return (result.is_integer())

    def istriangular(num):
        root1, root2 = quadratic_solver(1, 1, -2*(num))
        root = max(root1, root2)
        return (root.is_integer())

    numbers = 144

    while True:
        hex_num, numbers = numbers*(2*numbers-1), numbers + 1
        if ispentagonal(hex_num) and istriangular(hex_num):
            print(hex_num)
            break
