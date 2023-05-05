import math

side = float(input("Enter the length of a side of the pentagon: "))
area = (5 * side ** 2) / (4 * math.tan(math.pi / 5))

print(f"The area of the pentagon is {area:.2f}.")
