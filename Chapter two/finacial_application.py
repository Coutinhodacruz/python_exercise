subtotal = float(input("Enter the subtotal: "))
gratuity_rate = float(input("Enter the gratuity rate as percentage: "))
gratuity = subtotal * (gratuity_rate / 100)
total = subtotal + gratuity
print(f"Gratuity: ${gratuity : 2f}")
print(f"Total: ${total: 2f}")
