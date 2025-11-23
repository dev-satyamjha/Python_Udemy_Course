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
