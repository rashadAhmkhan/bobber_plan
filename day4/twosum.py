numbers = [1, 2, 3]
target = 10

def twoSum(l, t):
    complement = {}
    counter = 0

    for value in l:

        req = t-value

        if req in complement:              
            return complement[req], counter
        
        else:
            complement[value] = counter
            counter += 1



print(twoSum(numbers,target))