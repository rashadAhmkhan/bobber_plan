numbers = [2,4,5,7]
target = 11

i = 0
j = len(numbers) - 1

while i <= j:
    sum = numbers[i] + numbers[j]

    if sum == target:
        print(i+1 , j+1)
        break
    elif sum < target:
        i += 1
    else:
        j -= 1

