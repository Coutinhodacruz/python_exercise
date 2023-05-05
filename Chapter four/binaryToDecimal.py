binary_num = input("Enter a binary integer (containing only 0s and 1s): ")

decimal_num = 0
position = 1

for digit in binary_num[::-1]:
    if digit == '1':
        decimal_num += position
    position *= 2

print("The decimal equivalent of binary", binary_num, "is", decimal_num)
