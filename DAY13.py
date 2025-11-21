# Instance Attributes

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

#__str__ vs __repr__

class Computer:
    def __init__(self, brand: str, price: int) -> None:
        self.price = price
        self.brand = brand

    def __str__(self) -> str:
        return f"Brand: {self.brand} and Price: {self.price}"

    def __repr__(self) -> str:
        return f"Computer(Brand : {self.brand} and its Price is {self.price}"

linux: Computer = Computer('HP', 55000)
print(linux)
print(repr(linux))

# __eq__

class Account:
    def __init__(self, account_num: int, name: str, balance: int ):

        self.account_num = account_num
        self.balance = balance
        self.name = name

    def __eq__(self, other: 'Account') -> bool:
        return self.balance == other.balance

satyam: Account = Account(121212, 'Satyam', 100000)
harsh: Account = Account(110306, 'Harsh', 100000)

print(id(satyam))
print(id(harsh))
print(satyam == harsh)
