import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

answer = int(input("What is the sum of " + str(num1) + " and " + str(num2) + "?"))
if answer == num1 + num2:
    print("Correct")
else:
    print("Incorrect")

num3 = random.randint(0, 99)
num4 = random.randint(0, 99)

answer = float(input("What is the division of " + str(num3) + " and " + str(num4) + "?"))
if answer == num3 // num4:
    print("Correct")
else:
    print("Incorrect")
