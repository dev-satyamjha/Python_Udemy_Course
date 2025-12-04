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

#slice()

my_slice: slice = slice(2,None,3)
nums: list[int] = [1, 2, 3, 4, 6, 7, 8, 12, 14]
words: str = 'Satyam is the coolest man on earth'
print(nums[my_slice])
print(words[my_slice])

rev: slice = slice(None, None, -1)
num: list[int] = [1, 5, 7, 9, 11, 13]
print(num[rev])
