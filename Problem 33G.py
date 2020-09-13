# Runtime - 21.5 milliseconds (0.215 seconds)
from myFunctionsG import prime_checker as isPrime, split_stuff, combine_list, execute_this

@execute_this
def Problem_33():
    def fraction_reducer(numerator, denominator):
        if isPrime(denominator):
            return(numerator, denominator)
        if isPrime(numerator):
            if denominator % numerator == 0:
                return(numerator // numerator, denominator // numerator)
            else:
                return(numerator, denominator)
        end_point, divisor = numerator + 1, 2
        while divisor < end_point and numerator != 1:
            if numerator % divisor == 0 and denominator % divisor == 0:
                numerator = numerator // divisor
                denominator = denominator // divisor
            else:
                divisor += 1
        return (numerator, denominator)


    def same_digit_remover(numerator, denominator):
        if numerator == 1:
            return None
        if (numerator % 10 == 0 and denominator % 10 != 0) or (denominator % 10 == 0 and numerator % 10 != 0):
            return None
        if numerator % 10 == 0 and denominator % 10 == 0:
            return None
        numerator, denominator = list(split_stuff(str(numerator))), list(split_stuff(str(denominator)))
        for a in numerator:
            for b in denominator:
                if a == b:
                    numerator.remove(a)
                    denominator.remove(b)
                    return(int(combine_list(numerator)), int(combine_list(denominator)))
        return None


    fraction, product_n, product_d = list(), 1, 1
    for b in range(11, 100):
        for a in range(10, b):
            if same_digit_remover(a, b) is not None:
                true_numerator, true_denominator = fraction_reducer(a, b)
                numerator_by_shortcut, denominator_by_shortcut = same_digit_remover(a, b)
                numerator_by_shortcut, denominator_by_shortcut = fraction_reducer(numerator_by_shortcut, denominator_by_shortcut)
                if true_denominator == denominator_by_shortcut and true_numerator == numerator_by_shortcut:
                    fraction.append(str(true_numerator) + str(true_denominator))

    for iterator in fraction:
        product_d *= int(iterator[1])
        product_n *= int(iterator[0])

    print(fraction_reducer(product_n, product_d))
