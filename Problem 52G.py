from myFunctionsG import execute_this


@execute_this
def main():
    factorisations = {2: (), 3: (), 4: (2,), 5: (), 6: (2, 3)}
    failed_elder_numbers = set()

    def match_digits(num1, num2):
        hash_sum = 0
        for digit in str(num1):
            hash_sum += pow(int(digit), 2)
        for digit in str(num2):
            hash_sum -= pow(int(digit), 2)
        return hash_sum == 0

    def check_matches(num):
        nonlocal factorisations
        nonlocal failed_elder_numbers

        if num in failed_elder_numbers:
            return False

        x = 2
        while x <= 6:
            if num*x not in failed_elder_numbers and not match_digits(num, num * x):
                for wasted_nums in factorisations[x]:
                    failed_elder_numbers.add(wasted_nums*num)
                return False

            x += 1

        return True

    num = 1
    while True:
        if check_matches(num):
            print(num)
            break
        num += 1
