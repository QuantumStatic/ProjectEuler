# Runtime - 215 milliseconds (0.215 seconds)
from myFunctionsG import sieveEratoAlt, execute_this


@execute_this
def Problem_10():
    print(sum(sieveEratoAlt(2000000))+2)
