class Car:
    def __init__(self, number_plate: str):
        if len(number_plate) != 6:
            raise ValueError('Invalid Number Plate')

        self.number_plate = number_plate

class StolenCar:
    def __init__(self):
        self.stolen_plates: set[str] = set()

    def add_stolen_plates(self, plates: list[str]):
        for plate in plates:
            self.stolen_plates.add(plate.upper())

    def is_stolen(self, plate:str) -> bool:
        return plate.upper() in self.stolen_plates

def main():
    registry: StolenCar = StolenCar()
    registry.add_stolen_plates(['HYD999', 'BR6969', 'JH6969', 'DEL505', 'ERR404', 'SYS112', 'PUN601', 'GUJ100'])

    print('-----Welcome to Car Theft Identifier-----')
    print("Type 'remove <plate>' to remove a stolen plate")
    while True:
        plate: str = input('Enter car number plate: ').strip()

        try:
            car: Car = Car(plate)
        except ValueError as e:
            print(e)
            continue
        if registry.is_stolen(car.number_plate):
            print(f'⚠️ Car with plate "{car.number_plate}" is: STOLEN!')
        else:
            print(f'✅ Car with plate "{car.number_plate}" is: NOT STOLEN')


if __name__ == '__main__':
    main()
