# Instance Attributes

from ast import Num
from pickletools import float8


class Car:
    year: int = 2022

    def __init__(self, brand: str, name: str, price: int):
        self.brand = brand
        self.name = name
        self.price = price
    def info(self):
        print(f"{self.brand}'s {self.name} costs ₹{self.price} that was launched in {self.year}")

Hyundai: Car = Car('Hyundai', 'EV', 1200000)
TATA: Car = Car('TATA', 'NEXON', 300000)
Mercedes: Car = Car ('Mercedes', 'Benz', 20000000)

Hyundai.info()
TATA.info()
Mercedes.info()

#Class Attributes

Car.year = 2002

Hyundai.info()
TATA.info()
Mercedes.info()

#Dunder Methods

class Number:
    def __init__(self, n: int):
        self.n = n

    def __add__(self, other: 'Number') -> float:
        return self.n + other.n

    def __mul__(self, other: 'Number') -> float:
        return self.n * other.n

print(Number(10) + Number(20))
print(Number(10) * Number(20))
