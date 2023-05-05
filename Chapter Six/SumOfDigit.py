def sum_digits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10
    return sum


input_str = input("Enter a four-digit integer: ")
num = int(input_str)
result = sum_digits(num)
print("The sum of the digits is:", result)
