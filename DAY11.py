# Main()

def greet(people: list[str]) -> None:
    for person in people:
        print(f'Hello! {person}')
def main() -> None:
    people: list[str] = ['Jack', 'Oggy', 'Taplu', 'Paplu']
    greet(people)
if __name__ == '__main__':
    main()
