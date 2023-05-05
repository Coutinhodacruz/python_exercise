num = int(input("Enter a four digit integer: "))

revs_number = 0

while num > 0:

    remainder = num % 10
    revs_number = (revs_number * 10) + remainder
    num = num // 10

print("The reverse number is : {}".format(revs_number))
