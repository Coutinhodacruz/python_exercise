num = int(input("Enter a number: "))

total = 0
count = 0

while total < num:
    count += 1
    val = int(input("Enter integer value #" + str(count) + ": "))
    total += val

print("The sum of the entered integers is", total)
