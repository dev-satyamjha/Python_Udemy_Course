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
