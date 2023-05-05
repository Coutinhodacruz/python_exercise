
def is_perfect(number):
    sum = 1
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            sum += i
            if i != number // i:
                sum += number // i
    return sum == number



for i in range(2, 1001):
    if is_perfect(i):
        print(i, "is a perfect number.")
        print("Factors:")
        for j in range(1, i):
            if i % j == 0:
                print(j)
