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
