#Runtime - 730 milliseconds (0.730 seconds)
from myFunctions import prime_checker, execute_this, combine_list
from itertools import permutations

@execute_this
def Problem_41():
    
    length,largest = 2,0
    while length < 10:
        pan_dig_numbers = combine_list(list(permutations([x for x in range(1, length+1)])))
        pan_dig_numbers.sort()
        results = prime_checker(pan_dig_numbers)
        results.reverse()
        pan_dig_numbers.reverse()
        for x in range(len(results)):
            if results[x]:
                if pan_dig_numbers[x] > largest:
                    largest = pan_dig_numbers[x]
                break
        length += 1
    
    print(largest)
