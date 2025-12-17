from collections.abc import Iterator
#Lambda

numbers: list[int] = [2,4,12,24,34]
squared: Iterator[int] = map(lambda x: x**2, numbers)
print(list(squared))

chars: list[str] = ['Hero', 'Villian', 'Satyam', 'Allu Arjun', 'Nobody']

mapped: Iterator[str] = map(lambda n,c:f'{c}: {n**2}', numbers, chars)
print(list(mapped))
