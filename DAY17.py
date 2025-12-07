from typing import Any
from typing_extensions import Callable

#all()

output: list[int] = [1,1,1,0,0,0]
print(all(output))

string: list[str] = ['Past', '', 'Gone', 'Fight']
print(all(string))

words: list[str] = ['System', 'Battery', 'Vehicle', 'Wife']
if all(words):
    print("The word list is not empty.")
else:
    print("The list is non-empty.")

print(all([]))

#any()

print(any(output))

script : list[str] = ['System', 'Battery', 'Vehicle', '']
if any(script):
    print("Script is getting prepared..")
else:
    print("Script hasn't started yet...!")

print(any([]))

# isinstance

var: Any = 10.23

if isinstance(var, int):
    print("It's an integer..")
elif isinstance(var, str):
    print("It's a string...")
elif isinstance(var, (list, tuple)):
    print("It's a list/tuple..")
else:
    print(f"{var} is a {type(var)}")

class Animal:
    def sleep(self) -> None:
        print("Sleepy...Sleepy..")
class Horse(Animal):
    def run(self) -> None:
        print("Horse is running..")
class Owl(Animal):
    def awake(self) -> None:
        print("I am awake..")

animal = Animal()
horse = Horse()
owl = Owl()

print(isinstance(animal, Animal))
print(isinstance(horse, Animal))
print(isinstance(owl, Animal))
print(isinstance(animal, (Horse, Owl)))

def num(n):

    if isinstance(n, (float, int)):
        print(f"{n} is a number")
    else:
        raise TypeError(f"{n} {type(n)} is not a valid number")
num(2.3)
num(12)
#num('Satyam') : This would raise error

#callable

number: int = 12
name: str = 'Satyam'

def greet(name: str):
    print(f"{name} says hello..!!")

greet('Satyam')

print(callable(number))
print(callable(greet))

def func() -> None:
    print("Func() called!")

objects: list[int | str | Callable[[], None]] = [12, 'Satyam', func]

for obj in objects:
    if callable(obj):
        obj()
    else:
        print(f"{type(obj).__name__} is not callable")
