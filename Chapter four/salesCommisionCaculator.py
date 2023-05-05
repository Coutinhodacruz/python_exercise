SALES_COMMISSION_RATE = 0.09
BASE_SALARY = 200.0
ITEM_VALUES = [239.99, 129.75, 99.95, 350.89]

# Input the salesperson's items sold for the week
item1 = float(input("Enter the value of item 1 sold by the salesperson: "))
item2 = float(input("Enter the value of item 2 sold by the salesperson: "))
item3 = float(input("Enter the value of item 3 sold by the salesperson: "))
item4 = float(input("Enter the value of item 4 sold by the salesperson: "))

# Calculate the salesperson's total sales and earnings
total_sales = item1 + item2 + item3 + item4
commission = total_sales * SALES_COMMISSION_RATE
earnings = BASE_SALARY + commission

# Display the salesperson's earnings
print("The salesperson's total sales for the week is:", total_sales)
print("The salesperson's earnings for the week is:", earnings)
