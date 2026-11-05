numbers = [0,1,0,3,12]

posFilled = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        print("PosFilled; ",posFilled)
        numbers[posFilled] = numbers[i]
        posFilled += 1

while posFilled <= len(numbers)-1:
    numbers[posFilled] = 0
    posFilled += 1

print(numbers)
