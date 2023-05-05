numbers = []
for i in range(5):
    while True:
        num = int(input("Enter a number between 1 - 30: "))
        if 1 <= num <= 30:
            numbers.append(num)
            break
        else:
            print("Invalid input. Please enter a number between 1 and 30.")

        for num in numbers:
            print("*" * num)
