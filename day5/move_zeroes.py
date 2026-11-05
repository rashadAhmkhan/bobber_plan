numbers = [0,1,2,0,3,4,0,6,7]

def countZeroes(l):
    count = 0
    for num in l:
        if num == 0:
            count += 1

    return count

def moveZeroes(l):
    count = countZeroes(l)
    while count > 0:
        l.remove(0)
        l.append(0)

        count -= 1

    return l

print(moveZeroes(numbers))