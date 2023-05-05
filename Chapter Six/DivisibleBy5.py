def is_divisible(number):
    return number % 5 == 0



input_str = input("Enter 10 integers (separated by spaces): ")
integers = list(map(int, input_str.split()))

print("Divisible by 5:")
for num in integers:
    if is_divisible(num):
        print(num)
