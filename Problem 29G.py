from myFunctionsG import remove_duplicates_from as rdf, execute_this

@execute_this
def Problem_29():
    enteries = set()
    for a in range(2, 101):
        for b in range(2, 101):
            enteries.add(pow(a, b))
    print(len(enteries))
