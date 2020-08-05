# Runtime - 10 seconds 100 milliseconds (10.1 seconds) 
from myFunctionsG import execute_this

@execute_this
def Problem_39():
    list_of_triplets = [0]*1000
    for c in range(400):
        for b in range(c):
            for a in range(b):
                if a + b + c > 1000:
                    break
                if a**2 + b**2 == c**2:
                    list_of_triplets[a+b+c] += 1
    
    print(list_of_triplets.index(max(list_of_triplets)))

