from typing import Iterator

#Enumerate

people: list[str] = ['Man', 'Vs', 'Wild']
enumeration: Iterator[tuple[int, str]] = enumerate(people)
print(list(enumeration))

for i, person in enumerate(people, start = 10):
    print(f"{i+1}: {person}")
