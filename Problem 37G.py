# Runtime - 1 second 500 milliseconds (1.5 seconds)
from myFunctionsG import prime_checker as isprime, execute_this


@execute_this
def Problem_37():

    total_truncable_prime, number, Sum = 0, 11, 0

    def digit_removing_left(number):
        try:
            return (int(str(number)[1:]))
        except:
            return None

    def digit_removing_right(number):
        return(int(str(number)[:len(str(number))-1]))

    while total_truncable_prime < 11:
        temp_number = number
        if isprime(number):
            for x in range(len(str(number))-1):
                temp_number = digit_removing_left(temp_number)
                if temp_number is None or not isprime(temp_number):
                    break
            else:
                temp_number = number
                for x in range(len(str(number))-1):
                    temp_number = digit_removing_right(temp_number)
                    if not isprime(temp_number):
                        break
                else:
                    Sum += number
                    total_truncable_prime += 1
        number += 2
    
    print(Sum)
