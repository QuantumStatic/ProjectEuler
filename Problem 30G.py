from myFunctionsG import execute_this, split_stuff, combine_list

@execute_this
def Problem_30():
    fifth_powers = tuple(pow(x, 5) for x in range(10))

    def buffer_hedger(number):
        if number == 0:
            return (0, None)
        splitNum = list(split_stuff(number))
        maxNum = max(splitNum)
        splitNum.remove(maxNum)
        return(maxNum, combine_list(splitNum))

    def checker(number):
        buffer, temp_number = number, number
        nonlocal fifth_powers
        while temp_number >= 0 and buffer is not None:
            max_number, buffer = buffer_hedger(buffer)
            temp_number -= fifth_powers[max_number]
        if buffer is None and temp_number == 0:
            return (number)
        return(False)

    number, Sum = 2, 0
    while number <= 5*9**5:
        value = checker(number)
        if value is not False:
            Sum += value
        number += 1
    
    print(Sum)