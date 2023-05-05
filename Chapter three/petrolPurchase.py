class PetrolPurchase:

    def __init__(self, location: str, petrol_type: str, quantity: int, price_per_liter: float, discount: float):
        self._location = location
        self._petrol_type = petrol_type
        self._quantity = quantity
        self._price_per_liter = price_per_liter
        self._discount = discount

    def get_location(self) -> str:
        return self._location

    def set_location(self, location: str):
        self._location = location

    def get_petrol_type(self) -> str:
        return self._petrol_type

    def set_petrol_type(self, petrol_type: str):
        self._petrol_type = petrol_type

    def get_quantity(self) -> int:
        return self._quantity

    def set_quantity(self, quantity: int):
        self._quantity = quantity

    def get_price_per_liter(self) -> float:
        return self._price_per_liter

    def set_price_per_liter(self, price_per_liter: float):
        self._price_per_liter = price_per_liter

    def get_discount(self) -> float:
        return self._discount

    def set_discount(self, discount: float):
        self._discount = discount

    def get_purchase_amount(self) -> float:
        net_amount = self._quantity * self._price_per_liter
        discount_amount = net_amount * self._discount / 100
        return net_amount - discount_amount


class Petrol:
    def run(self):
        purchase = PetrolPurchase("Lagos ", "Regular", 20, 1.5, 5)
        print(f"Location: {purchase.get_location()}")
        print(f"Petrol type: {purchase.get_petrol_type()}")
        print(f"Quantity: {purchase.get_quantity()} L")
        print(f"Price per liter: {purchase.get_price_per_liter()} USD")
        print(f"Discount: {purchase.get_discount()}%")
        print(f"Net amount: {purchase.get_purchase_amount()} USD")


Petrol().run()
