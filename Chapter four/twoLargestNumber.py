largest1 = largest2 = float('-inf')  # initialize largest1 and largest2 to negative infinity

for i in range(1, 11):
    number = float(input(f"Enter number {i}: "))
    if number > largest1:
        largest2 = largest1
        largest1 = number
    elif number > largest2:
        largest2 = number

print(f"The largest number is {largest1}")
print(f"The second largest number is {largest2}")
