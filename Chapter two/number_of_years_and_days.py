minutes = int(input("Enter the number of minutes: "))
hours = minutes // 60
days = hours // 24
years = days // 365
remaining_days = days % 365
print(f"{minutes} minutes is approximately {years} years and {remaining_days} days")
