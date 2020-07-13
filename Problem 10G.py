from myFunctionsG import sieveEratoAlt, execute_this


@execute_this
def Problem_10():
    print(sum(sieveEratoAlt(2_000_000))+2)
