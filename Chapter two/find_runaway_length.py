import math

v = float(input("Enter the take-off speed (m/s): "))
a = float(input("Enter the acceleration (m/s~2): "))

min_runway_length = (v ** 2) / (2 * a)

print(f"The minimum runway length needed is {math.ceil(min_runway_length)} meters.")
