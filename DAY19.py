#Doc strings

def square(n):
    '''Take a number n and return the square of n.'''
    return n**2

print(square.__doc__)

print(print.__doc__)

print()

#Assert

def bank_account() -> None:
    account: int = 0
    assert account >=0

    print(f"The account is created with a balance of ₹ {account}")

bank_account()

def grade(grade:int) ->str:
    assert 0<=grade<=100, f'Invalid {grade}'
    return 'passed' if grade>=70 else 'failed'

print(grade(45))
print(grade(100))
print(grade(75))

#Multiple Assignments

a,b = 12, 10
print(a)
print(b)

first,*middle,last = (12,24,36,48,60,72,84,96,108,120)
print(first)
print(middle)
print(last)

#is VS ==
class Car:

    def __init__(self, brand:str) ->None:
        self.brand = brand


car1: Car = Car('BMW')
car2: Car = Car('BMW')

print(car1 is car2)
print(car1 == car2)

print(car1.brand == car2.brand)
print(1+1 == 2)
