# if you have a pentagonal number at pos x and another pentagonal number at y(>x), then their difference is 1/2*(y-x)*{3(y+x)-1}
# if you have a pentagonal number at pos x and another pentagonal number at y(>x), then their sum is 1/2*{3(x2+y2)-(x+y)}
# Runtime - 1 second 250 milliseconds (1.250 seconds)
from myFunctions import execute_this
from math import sqrt


@execute_this
def Problem_44():

    def ispentagonal(num):
        result = (1/6)*(sqrt(24*num+1)+1)
        if result == int(result):
            return True
        return False


    upper_limit = 2

    while True:
        upper_limit_pent_num = (upper_limit*(3*upper_limit-1))//2
        for lower_limit in range(upper_limit-1, 0, -1):
            lower_limit_pent_num = (lower_limit*(3*lower_limit-1))//2
            if ispentagonal(lower_limit_pent_num+upper_limit_pent_num) and ispentagonal(upper_limit_pent_num-lower_limit_pent_num):
                print(upper_limit_pent_num - lower_limit_pent_num)
                break
        else:
            upper_limit += 1
            continue
        break
        
