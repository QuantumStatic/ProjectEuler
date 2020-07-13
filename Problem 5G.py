from myFunctionsG import execute_it, LCM, check_list_containment, prime_factoriser as pf


@execute_it
def Problem_5():

    curr_lcm = 2520
    final_num, curr_factors = 20, pf(curr_lcm)

    for num in range(2, final_num+1):
        if check_list_containment(curr_factors, pf(num), method2=True) is False:
            curr_lcm = LCM(curr_lcm, num)
            curr_factors = pf(curr_lcm)

    print(curr_lcm)
