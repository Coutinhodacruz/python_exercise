number = input("Enter a five-digit integer: ")

if len(number) != 5:
    print("Error: Entered number is not five digits long")
else:
    if number == number[::-1]:
        print("The number is a palindrome")
    else:
        print("The number is not a palindrome")
