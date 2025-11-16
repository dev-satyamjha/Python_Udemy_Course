from collections import Counter
from time import sleep

class Car:
    def __init__(self, brand: str , name: str, model: str, color: str, launched_year: int ) -> None:
        self.brand = brand
        self.name = name
        self.model = model
        self.color = color
        self.launched_year = launched_year
    def drive(self, distance: int, speed: int):
        print(f'{self.brand}\'s {self.name} {self.model} of {self.color} color started journey')
        for i in range(1, distance+1,):
            sleep(60/speed)
            print(f'KM: {i}')
        print(f'{self.brand}\'s {self.name} {self.model} of {self.color} color completed it\'s journey')

def create_cars(cars: list[Car]) -> None:
    brand: str = input("Enter Car's Brand: ")
    name: str = input("Enter Car's Name: ")
    model: str = input("Enter Car's Model: ")
    color: str = input("Enter Car's Color: ")
    launched_year: int = int(input("Enter Car's Launched Year: "))

    try:
        amount = int(input("Enter total amount vehicles to be used: "))

        for i in range(amount):
            cars.append(Car(brand,name, model,color,launched_year))
        print("Cars Created..!!")
    except ValueError:
        print("Please enter amount in digits!")

def display_stock(cars: list[Car]) -> None:
    car_tuples: list[tuple[str,str,str,str,int]] = [(car.name, car.brand, car.model, car.color, car.launched_year) for car in cars]
    counter: Counter[tuple[str,str,str,str,int]] = Counter(car_tuples)

    if not counter:
            print("No cars in stock.")
            return

    for (brand, name, model, color, launched_year), count in counter.items():
        print(f"{brand}'s {name} {model} of {color} color launched in {launched_year} is '{count}' in stock.")

def main():
    cars: list[Car] = []

    print("Type 'Create' to create cars and 'display' to display cars")
    while True:
        user_input : str = input("Type: ").strip().capitalize()

        if user_input == 'Create':
            create_cars(cars)
        elif user_input == 'Display':
            display_stock(cars)
        else:
            print("Invalid Input")

if __name__ == '__main__':
    main()
