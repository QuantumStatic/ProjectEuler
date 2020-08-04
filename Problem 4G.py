# Runtime - 83.2 milliseconds (0.0832 seconds)
from myFunctionsG import execute_this

# if there are two numbers with n digits & m digits then their product can't have more than n+m digits


@execute_this
def Problem_4():
    palindrome = int()

    for x in range(999, 316, -1):
        for y in range(x-1, 316, -1):
            num = str(x * y)
            if (num[0] == num[-1]) and (num[1] == num[-2]) and (num[2] == num[-3]) and int(num) > palindrome:
                palindrome = int(num)

    print(palindrome)
