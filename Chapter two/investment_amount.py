final_value = float(input("Enter the desired final account value: $"))
interest_rate = float(input("Enter the annual interest rate in percent: "))
years = int(input("Enter the number of years: "))

interest_rate_decimal = interest_rate / 100
initial_deposit = final_value / ((1 + interest_rate_decimal) ** years)
print(f"The initial deposit amount needed is ${round(initial_deposit, 2)}. ")