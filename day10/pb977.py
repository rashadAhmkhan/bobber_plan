nums = [-4,-1,0,3,10]

sq_nums = [num**2 for num in nums]

i = 0
j = len(nums)-1

result = []

while i <= j:
    if sq_nums[i] > sq_nums[j]:
        result.append(sq_nums[i])
        i += 1
    else:
        result.append(sq_nums[j])
        j -= 1
        

result.reverse()
print(result)