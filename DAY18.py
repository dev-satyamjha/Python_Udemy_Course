from collections.abc import Iterator
from typing import Any

#Filter

def is_even(n: int) -> bool:
    return n % 2 == 0

numbers: list[int] = list(range(1, 20))
even: Iterator[int] = filter(is_even, numbers)
print(even)
print(list(even))
print(list(even))

def short(name: str) -> bool:
    return len(name) < 5

short_names: list[str] = ['Satyam', 'Sats', 'Bond', 'Anya', '', 'Snacks', 'Harsh', '', '']
name: Iterator[str] = filter(short, short_names)
empty: Iterator[str] = filter(None, short_names)
print(list(name))
print(list(empty))

#Map

def square(num: int) -> int:
    return num ** 2

squared: Iterator[int] = map(square, numbers)
print(list(squared))
print(list(squared))

strings: Iterator[str] = map(str, numbers )
print(list(strings))

def combine(a:Any, b: Any) ->str:
    return f'{a} {b}'

combined: Iterator[str] = map(combine, numbers, short_names)
print(list(combined))

#Sorted

nums = (1,2,3,4,5,6,7,8,9,99,10,23,12,45,61,21,70)
print(sorted(nums))
print(sorted(nums, reverse=True))

names: list[str] = ['satyam', 'Amanda', 'annie', 'Abigail', 'alexa', 'Roman', 'ben', 'Misty']
print(sorted(names))
print(sorted(names, key=str.lower))

def vowel_count(text:str) ->int:
    return sum(1 for c in text if c in 'AEIOUaeiou')

print(sorted(names, key=vowel_count, reverse=True))

#Eval
a = 12
b = 10
expr: str = 'a + b'
print(eval(expr))

james: str = '"james".upper()'
print(eval(james))

#eval

code: str = '''
name: str = 'Satyam'
age: int = 23
print(f"{name} is {age} years old")
'''

print(exec(code))

x = 5
exec('y=x+12')
print(y)
