numbers = [4, 7, 2, 9]

def firstRepeated(l):
    num_set = set()

    for i in l:
        if i in num_set:
            return i
        else:
            num_set.add(i)
    return None

print(firstRepeated(numbers))