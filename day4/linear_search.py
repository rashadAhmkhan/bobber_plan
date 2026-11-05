numbers = [3]
target = 17

def linearSearch(l,t):
    found = False
    for i in range(len(l)):
        if l[i] == t:
            found = True
            break

    if found:
        return i
    else:
        return -1



def binarySearch(l,t):
    low = 0
    high = len(l)-1

    
    while low <= high:
        mid = (high + low) // 2
            
        if l[mid] == t:         #numbers = [3, 5, 8, 12, 14, 17, 21]
            return mid
        elif l[mid] > t:
            high = mid-1
        elif l[mid] < t:
            low = mid+1

    return -1

print(binarySearch([], 4))

print(binarySearch([4], 4))

print(binarySearch([4], 7))

print(binarySearch([3, 5, 8], 3))

print(binarySearch([3, 5, 8], 8))

print(binarySearch([3, 5, 8], 6))