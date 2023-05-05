base_length = int(input("Enter the length of the base of the triangle (1-10): "))

if base_length < 1 or base_length > 10:
    print("Invalid base length")
else:
    for i in range(1, base_length+1):
        print("*" * i)
