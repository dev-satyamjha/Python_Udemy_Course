from decimal import Decimal, getcontext

# Truthy

numbers1 : list[int] = []
numbers2 : list[int] = [1]

if numbers1:
    for number in numbers1:
        print(number)
else:
    print("No Numbers:....")

if numbers2:
    for number in numbers2:
        print(number)
else:
    print("No Numbers:....")

pi = 3.14
name = 'Silen'
elements = [0,1,2,3,4]
users={'Ben' : 0}
unique = {None, 0}

#Falsy

zero_float = 0
empty_sr = ''
empty_dict = {}
emp_list = []
emp_set = set()
none_type = None

print(bool(pi))
print(bool(zero_float))
print(bool(unique))
print(bool(none_type))

#Float problem

a = Decimal('0.1')
b = Decimal('0.2')
c = Decimal('0.3')

print((a+b) == c)

getcontext().prec = 4

d = Decimal('0.1000100')
e = Decimal('0.1000123')
print(d == e)
print(d+e)
print((d+e)== Decimal('0.2'))
print(float(d) + 12)

#Scopes

def greet(name:str) -> None:
    greeting: str = 'Hey! Hello..'         #Defined under function(local scope)
    print(f"{greeting}, how are you..{name}?!")

name: str = 'Satyam' #Global Scope

def run() -> None:
    greet(name)

run()

#Global

x: int = 12

def test_x() -> None:
    global x
    x = 123

test_x()
print(x)
