from uuid import uuid4, UUID

# Inheritance

class Animal:
    def __init__(self, name:str) -> None:
        self.name = name
    def eat(self):
        print(f'{self.name} is eating..')
    def sleep(self):
        print(f"{self.name} is sleeping!!")

class Cat(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def meow(self):
        print(f"{self.name} is meoowing..!!")
Pins: Cat = Cat('Pins')

Pins.eat()
Pins.sleep()
Pins.meow()

dog: Animal = Animal('Harry')

dog.eat()
dog.sleep()

# super()

class Computer:
    def __init__(self, brand: str, price: int) -> None:
        self.brand = brand
        self.price = price

    def power_on(self):
        print(f"{self.brand} is turning on...")
    def charge(self):
        print(f"{self.brand} is charging...")
    def shut_down(self):
        print(f"{self.brand} is shutting down...")

class Linux(Computer):
    def __init__(self, price: int) -> None:
        super().__init__('Linux', price)
    def update(self):
        print(f"Your {self.brand} is updating...")
    def security(self):
        print(f"{self.brand} is asking for password...")

linux: Linux = Linux(20000)
linux.power_on()
linux.update()
linux.security()
linux.shut_down()

#Name mangling

class Account:
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount: int):
        self.__balance += amount
        print(f"₹{amount} is deposited in bank.")
    def display(self):
        print(f"Cuurent balance is: ₹{self.__balance}")

class Savings(Account):
    def __init__(self, owner: str) -> None:
        super().__init__(owner,0)

        self.__balance = 0

    def deposit_into_savings(self, amount: int):
        self.__balance += amount
        print(f"₹{amount} deposited into savings.")

    def savings_balance(self):
        print(f"Savings account balance: ₹{self.__balance}")

account: Savings = Savings('Satyam')
account.deposit(100000)
account.deposit_into_savings(10000)

account.display()
account.savings_balance()

account.deposit(10000)

account.display()
account.savings_balance()

class Product:
    def __init__(self, name: str):
        self.name = name
        self.__unique_id = self.create_unique_id()

    def create_unique_id(self) -> UUID:
        print(f"Product {self.name} has been created..!")
        return uuid4()

    def compare_product(self, other: 'Product') -> bool:
        print(f"{self.name} = {self.__unique_id}")
        print(f"{other.name} = {other.__unique_id}")
        return self.__unique_id == other.__unique_id

cup: Product = Product('Cup')
hat: Product = Product('Hat')
print(cup.compare_product(hat))
print(cup.compare_product(cup))
