from typing import Iterator

#Enumerate

people: list[str] = ['Man', 'Vs', 'Wild']
enumeration: Iterator[tuple[int, str]] = enumerate(people)
print(list(enumeration))

for i, person in enumerate(people, start = 10):
    print(f"{i+1}: {person}")

#round()

val: float = 12121212.121212
print(round(val))
print(round(val, 2))
print(round(val, 4))
print(round(val, -1))
print(round(val, -3))
print(round(val, -5))
print(round(1.5))
print(round(2.5))
print(round(12.5))
print(round(11.5))

#range()

ranges: range = range(10)
print(ranges)
print(list(ranges))
print(tuple(ranges))

my_range: range = range(12, 24, 2)
print(my_range)
print(list(my_range))
print(tuple(my_range))

for i in range(10):
    print('I love my life..')
