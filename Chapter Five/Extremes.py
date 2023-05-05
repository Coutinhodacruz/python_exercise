num_values = int(input("How Many values would like to to input: "))

if num_values < 2:
    print("Error: Please input at least 2 values: ")
    exit()

min_val = 0
max_val = 0

for i in range(num_values):
    val = inty(input("Enter value #{}: ".format(i + 1)))
    if min_val is None or val < min_val:
        min_val = val
    if max_val is None or val > max_val:
        max_val = val

sum_of_extremes = min_val + max_val
print("The minimum value is:", min_val)
print("The maximum value is:", max_val)
print("The sum of the minimum and maximum values is:", sum_of_extremes)
