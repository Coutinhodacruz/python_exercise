today = int(input("Enter today's day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6): "))
days = int(input("Enter the number of days after today for a future day: "))

# Calculate the future day of the week
future_day = (today + days) % 7

# Define a list of weekdays
weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# Display the future day of the week
print("Today is", weekdays[today], "and the future day is", weekdays[future_day])
