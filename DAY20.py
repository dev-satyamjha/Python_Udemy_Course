from collections.abc import Iterator
from enum import Enum
#Lambda

numbers: list[int] = [2,4,12,24,34]
squared: Iterator[int] = map(lambda x: x**2, numbers)
print(list(squared))

chars: list[str] = ['Hero', 'Villian', 'Satyam', 'Allu Arjun', 'Nobody']

mapped: Iterator[str] = map(lambda n,c:f'{c}: {n**2}', numbers, chars)
print(list(mapped))

#Walrus Operator

password: str = '@indentlyisawesome!'
if (length := len(password)) > 15:
    print(f"Password length ({length}) is good")
else:
    print(f"Password length{length} is bad!")

text: str = "Don't you think that i am awesome!?"

data ={'words': (words := text.split()), 'word_count' : len(words)}

print(data['words'])
print(data['word_count'])


while (line := input('You: ')).lower()!= 'quit':
    print(f"Echo: {line}")
else:
    print('Quitting...')

#Enums

class Color(Enum):
    RED = 'red'
    GREEN = 'green'

def create_square(color: Color):
    if color == Color.RED:
        print("Red square created..!!")
    elif color == Color.GREEN:
        print("Green square created..!!")
    else:
        print(f"Square color {color} not available..")

create_square(Color.RED)
create_square(Color.GREEN)
create_square(color= 'Blue')
print(Color.RED.name)
print(Color.RED.value)
print(list(Color))
