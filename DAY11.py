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

#Slicing

people: list[str] = ['Satyam', 'Sung Jinwhoo', 'Anya Forger', 'Pikachu', 'Allu Arjun', 'Roman Reigns']

print(people[:4])
print(people[:2])
print(people[:4] + people[4:6])
print(people[3:6])

numbers1: list[int] = list(range(20))
print(numbers1[0:10:3])
print(numbers1[20:0:-5])
print(numbers1[::-2])

#Looping Problem

people1: list[str] = ['Satyam', 'Ben', 'Allu Arjun', 'Joginder', 'Harsh', 'Roman', 'Dhoni']
people_new: list[str] = []

for person in people1:
    if person == 'Harsh':
        people1.remove('Harsh')

    print(person)

print('----------------------------------')

for person in people1.copy():
    if person == 'Harsh':
        people1.remove('Harsh')
        continue

    print(person)

print(people1)

print('---------------------------------------------------------------')

for per in people1:
    if per == 'Harsh':
        continue
    people_new.append(per)
    print(per)

print(people_new)
