numbers = [0,1,2,0,3,4,0,6,7]

def shiftzeroes(l):
    ls = []
    zero_count = 0

    for num in l:
        if num != 0:
            ls.append(num)
        else:
            zero_count += 1

    while zero_count > 0:
        ls.append(0)
        zero_count -= 1

    return ls

print(shiftzeroes(numbers))