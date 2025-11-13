# Main()

def greet(people: list[str]) -> None:
    for person in people:
        print(f'Hello! {person}')
def main() -> None:
    people: list[str] = ['Jack', 'Oggy', 'Taplu', 'Paplu']
    greet(people)
if __name__ == '__main__':
    main()

# List Comprehensions

numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 12, 10, 14]
squared: list[int] = [n**2 for n in numbers]
print(squared)

str_numbers: list[str] = [str(n) for n in numbers]
print(str_numbers)

text: str = "Hello Owls, Welcome to my nest!!"
vowels: list[str] = [v for v in text if v in 'aeiouAEIOU' ]
print(vowels)
print('Count of vowels:', len(vowels))
name: list[str] = ['Satyam', 'Harsh', 'Allu Arjun', 'Roman', 'Priyanka']
print("Length of names: ", [len(names) for names in name])
