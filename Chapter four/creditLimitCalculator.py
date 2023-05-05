class Customer:
    def __init__(self, account_num, balance, charges, credits, limit):
        self.account_num = account_num
        self.balance = balance
        self.charges = charges
        self.credits = credits
        self.limit = limit

    def get_new_balance(self):
        return self.balance + self.charges - self.credits

    def credit_limit_exceeded(self):
        return self.get_new_balance() > self.limit


# Test the class
customer1 = Customer(1001, 1500, 800, 200, 2000)
customer2 = Customer(1002, 500, 1000, 200, 1000)

for customer in [customer1, customer2]:
    print(f"Customer account number: {customer.account_num}")
    print(f"New balance: {customer.get_new_balance()}")

    if customer.credit_limit_exceeded():
        print("Credit limit exceeded")
    else:
        print("Credit limit not exceeded")

    print()
