size = 10

# print the top half of the square
for i in range(1, size + 1):
    row = ""

    # print the left triangle
    for j in range(1, i + 1):
        row += "*"

    # print the middle gap
    for j in range(1, size - i + 1):
        row += " "

    # print the right triangle
    for j in range(1, i + 1):
        row += "*"

    # print the row
    print(row, end="")

    # print vertical separator
    if i == size:
        print("  " * (size - 1), end="")
    else:
        print(" ", end="")

# print the bottom half of the square
for i in range(size, 0, -1):
    row = ""

    # print the left triangle
    for j in range(1, i + 1):
        row += "*"

    # print the middle gap
    for j in range(1, size - i + 1):
        row += " "

    # print the right triangle
    for j in range(1, i + 1):
        row += "*"

    # print the row
    print(row, end="")

    # print newline or end of output
    if i == 1:
        print()
    else:
        print(" ", end="")
