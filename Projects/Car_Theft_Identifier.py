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

    def remove_stolen_plate(self, plate: str) -> bool:
        p = plate.upper().strip()
        if p in self.stolen_plates:
            self.stolen_plates.remove(p)
            return True
        return False

    def is_stolen(self, plate:str) -> bool:
        return plate.upper() in self.stolen_plates

def main():
    registry: StolenCar = StolenCar()
    registry.add_stolen_plates(['HYD999', 'BR6969', 'JH6969', 'DEL505', 'ERR404', 'SYS112', 'PUN601', 'GUJ100'])

    print('-----Welcome to Car Theft Identifier-----')
    print("Type 'remove <plate>' to remove a stolen plate")
    while True:
        plate: str = input('Enter car number plate: ').strip()
        if plate.lower().startswith('remove '):
            target = plate.split(maxsplit=1)[1].strip()
            try:
                Car(target)
            except ValueError as e:
                print(e)
                continue
            if registry.remove_stolen_plate(target):
                print(f'🗑️ Removed {target.upper()} from stolen registry.')
            else:
                print(f'🚫 {target.upper()} was not in the stolen registry.')
            continue
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
