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
