# initialize the counter and largest variables
counter = 0
largest = float('-inf')

# loop through 10 numbers
while counter < 10:
    # get input from user
    number = int(input("Enter a number: "))
    # check if the number is the largest so far
    if number > largest:
        largest = number
    # increment the counter
    counter += 1

# print the largest number
print("The largest number is:", largest)
