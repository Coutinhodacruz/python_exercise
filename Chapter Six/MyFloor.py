def my_floor(num):
    integer = int(num)
    if integer > num:
        return integer - 1
    else:
        return integer


def my_ceil(num):
    integer = int(num)
    if integer < num:
        return integer + 1
    else:
        return integer


number = 3.14159
print(f"Floor of {number}: {my_floor(number)}")
print(f"Ceil of {number}: {my_ceil(number)}")
