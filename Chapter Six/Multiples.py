
def is_multiple(number1, number2):
    return number2 % number1 == 0


pairs = [
    [2, 6],
    [3, 10],
    [5, 25],
    [7, 49],
]

for pair in pairs:
    num1, num2 = pair
    print(f"{num2} is{' ' if is_multiple(num1, num2) else ' not '}a multiple of {num1}")
