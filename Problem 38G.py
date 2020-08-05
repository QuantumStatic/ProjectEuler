# Runtime - 22 milliseconds (0.022 seconds)
from myFunctions import execute_this, remove_duplicates_from as rdf, split_stuff


@execute_this
def Problem_38():
    current_highest = int()
    for number in range(1000, 10000):
        if '9' in str(number):
            tables = tuple(number * (x+1) for x in range(10))
            concatenated_product = str()
            for y in range(10):
                concatenated_product += str(tables[y])
                if len(concatenated_product) == 9:
                    concatenated_product = rdf(concatenated_product)
                    if sum(split_stuff(concatenated_product, int)) == 45:
                        if (temp := int(concatenated_product)) > current_highest and '0' not in concatenated_product:
                            current_highest = temp
                    break
                elif len(concatenated_product) > 9:
                    break
    print(current_highest)
