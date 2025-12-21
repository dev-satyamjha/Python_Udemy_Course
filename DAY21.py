from typing import Any, Callable
from functools import wraps
import time

#Generators

def generate_billion():
    for i in range(100000000):
        yield i

billion = generate_billion()

print(next(billion))
print(next(billion))
print(next(billion))

for i in range(10):
    print(next(billion))


def power_of_two(limit:int):
    n: int = 1
    while n <= limit:
        yield n
        n *= 2

powers = power_of_two(88)
print(next(powers))
print(next(powers))
print(next(powers))
print(next(powers))

#Decorators

type Func = Callable[..., Any]

def time_this(func : Func) ->Func:
    @wraps(wrapped=func)
    def wrapper(*args: Any, **kwargs: Any) ->Any:
        start: float = time.perf_counter()
        result: Any = func(*args, **kwargs)
        end: float = time.perf_counter()
        print(f"{func.__name__} took {end - start: .4f}s")
        return result
    return wrapper

@time_this
def expensive(n:int) ->int:
    total: int = 0
    for i in range(n):
        total +=i

    return total

test1: int = expensive(200000)
print(test1)
print()


def repeat(n:int) -> Callable[[Func],Func]:
    def decorator(func:Func):
        @wraps(wrapped=func)
        def wrapper(*args:Any, **kwargs:Any) -> Any:
            result: Any = None

            for _ in range (n):
                result = func(*args, **kwargs)
            return result

        return wrapper
    return decorator

@repeat(10)
def greet() ->None:
    print("Hello, Man!")

greet()

# Wraps


def handle_errors(func: Func) -> Func:
    """__handle_errors() docstring__"""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """__wrapper() docstring__"""
        try:
            result: Any = func(*args, **kwargs)
            print(f"{func.__name__}() ran successfully.")
            return result
        except Exception as e:
            print(f"{func.__name__}() failed: {e}")

    return wrapper
@handle_errors
def greet1(name:str) ->None:
    """__greet()__ __docstring__"""
    print(f"Hello, {name}!")

greet1('Satyam')
print(greet1.__name__)
print(greet1.__doc__)
