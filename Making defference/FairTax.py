TAX_RATE = 0.23

housing = float(input("Enter your house expenses: "))
food = float(input("Enter your food expenses: "))
clothing = float(input("Enter your clothing expenses: "))
transportation = float(input("Enter your transportation expenses: "))
education = float(input("Enter your education expenses: "))
health_care = float(input("Enter your health care expenses: "))
vacation = float(input("enter your vacation expenses: "))

total_expenses = housing + food + clothing + transportation + education + health_care + vacation
estimated_fair_tax = total_expenses * TAX_RATE

print("\nYour estimate fair tax is: ${:.2f}".format(estimated_fair_tax))
