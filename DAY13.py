# Instance Attributes

class Car:
    def __init__(self, brand: str, name: str, price: int):
        self.brand = brand
        self.name = name
        self.price = price
    def info(self):
        print(f"{self.brand}'s {self.name} costs ₹{self.price}")

Hyundai: Car = Car('Hyundai', 'EV', 1200000)
TATA: Car = Car('TATA', 'NEXON', 300000)
Mercedes: Car = Car ('Mercedes', 'Benz', 20000000)

Hyundai.info()
TATA.info()
Mercedes.info()
