class Car:
    def __init__(self, model: str, year: str, price: float):
        self.model = model
        self.year = year
        if price > 0:
            self.price = price
        else:
            self.price = 0.0

    def set_model(self, model: str):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year: str):
        self.year = year

    def get_year(self) -> str:
        return self.year

    def set_price(self, price: float):
        if price > 0:
            self.price = price

    def get_price(self):
        return self.price


class carApplication:
    def run(self):
        car1 = Car("Toyota camry", "2021", 40000)
        car2 = Car("Benz", "2022", 900000)

        print("Car 1 price ", car1.get_price())
        print("Car 2 price ", car2.get_price())

        car1.set_price(car1.get_price() * 0.95)
        car2.set_price(car2.get_price() * 0.03)

        print("Car 1 price after 5% discount:", car1.get_price())
        print("Car 2 price after 7% discount:", car2.get_price())



app = carApplication()
app.run()
