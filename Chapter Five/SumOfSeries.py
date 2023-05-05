print("{:<10}{}".format("n", "Sum"))
for n in range(1, 101):
    sum = 0
    for i in range(1, n+1):
        sum += i
    print("{:<10}{}".format(n, sum))
