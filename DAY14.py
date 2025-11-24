from datetime import date

class Worker:
    def __init__(self, name: str):
        self.name = name

    def work(self):
        print(f"{self.name} is doing a work..")

    def relax(self):
        print(f"{self.name} is relaxing..")

Suhasini: Worker = Worker('Suhasini')
Suhasini.work()
Suhasini.relax()

# @staticmethod

class Calculator:
    def __init__(self, version: str):
        self.version = version

    @staticmethod
    def add(*numbers: float):
        return sum(numbers)

    def info(self):
        print(f"Calculator version: {self.version}")

calc: Calculator = Calculator('Pro Model')

calc.add(12.10,9)
print(calc.add(12,10,9))

#@classmethod

class User:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def birth_year(cls, name : str, year: int) -> 'User':
        current_year: int = date.today().year
        return cls(name, current_year - year)



    def info(self) ->None:
        print(f"The name is {self.name} and age is {self.age}.")

Satyam : User = User.birth_year('Satyam', 2002)
Satyam.info()
