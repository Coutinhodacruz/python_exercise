num = int(input("Enter an integer between 0 and 1000: "))
sum = 0
while num > 0:
    sum += num % 10
    num //= 10
    print(f"The sum of the digit is: ", sum)
