def calculate_charges(hours_park):
    charged = 2
    if hours_park > 3:
        charged += int((hours_park - 3) + 0.99) * 0.5
    return min(charged, 10)


hours_parked_array = [2, 4.5, 7, 1.5]
total_receipt = 0

for i, hours_parked in enumerate(hours_parked_array):
    charge = calculate_charges(hours_parked)
    print(f"Customer {i + 1}: {charge:.2f}")
    total_receipt += charge

print(f"Total receipt: {total_receipt:.2f}")
