import random

num1 = random.randint(0, 99)
num2 = random.randint(0, 99)

answer = int(input("What is the multiplication of " + str(num1) + " and " + str(num2) + " ?"))

if answer == num1 * num2:
    print("Correct")
else:
    print("Incorrect")
