ascii_code = int(input("Enter an ASCII code (between 0 and 127): "))

if ascii_code < 0 or ascii_code > 127:
    print("Invalid ASCII code.")
else:
    character = chr(ascii_code)
    print(f"The character corresponding to the ASCII code {ascii_code} is {character}.")
