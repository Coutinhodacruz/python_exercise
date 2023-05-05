sum = 0

for i in range(1, 30):
    if i % 3 == 0:
        print("The number is divisible by 3")
        sum += i
    else:
        print("The number is not divisible by 3")


print(sum)
