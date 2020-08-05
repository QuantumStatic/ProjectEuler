# Runtime - 810 milliseconds (0.810 seconds)
from myFunctions import execute_this


@execute_this
def Problem_36():
    def palindrome_finder(number):
        return (number == int(''.join(reversed(str(number)))))

    palindromes, Sum = (x for x in range(1, 1000000) if palindrome_finder(x)), 0

    for palindrome in palindromes:
        if palindrome_finder(int(bin(palindrome)[2:])):
            Sum += palindrome

    print(Sum)
