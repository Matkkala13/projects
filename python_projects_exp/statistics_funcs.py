
def permutator(items:list, times:int)->list:
    cop = [str(i) for i in items]
    result = []
    counter = 1

    if times == 1:
        return cop
    else:
        while counter < times:
            if result == []:
                for i in cop:
                    for n in cop:
                        result.append(i + n)
            else:
                snap = result.copy()
                result = []
                for i in snap:
                    for n in cop:
                        result.append(i + n)

            
            counter += 1
    return result

#example of the permutator
"""
numbers = list(range(0,4))
times = 3
permutation = permutator(numbers, times)
print(permutation)"""


def variator(items:list, spots:int)->list:
    
    return len(items)


"""spots = 2
variation = variator(numbers, spots)
print(variation)"""


