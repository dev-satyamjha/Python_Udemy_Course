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
