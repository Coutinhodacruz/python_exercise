def isPalindrome(number):

    str_num = str(number)


    return str_num == str_num[::-1]


num = int(input("Enter a number: "))
if isPalindrome(num):
    print(num, "is a palindrome number.")
else:
    print(num, "is not a palindrome number.")
