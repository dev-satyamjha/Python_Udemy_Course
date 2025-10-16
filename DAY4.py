import math

# Arithmetic Operators
a: int = 12
b: int = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)

#Powers
print(2**6)
print(10**3)

#Modulus
print(11 % 3)
print(8 % 5)

#Floor division
print(12//5)

#square root
print(math.sqrt(12))

#Assignment Operators
a: int = 6
a += 1
a += 1
a += 1
print(a)
a -= 10
print(a)

res: float = 1220
res += 1000
res -= 1200
res /= 123
res //= 12
res *= 123
res %= 120
res **= 5

# Union
d1: dict [str, str] = {'HEY', 'HELLO', 'HI'}
d2: dict [str, str] = {'HELLO', 'HOW', 'ARE' , 'YOU'}
d1 |= d2
print(d1)

# Comparison Operators
number: int = 32
print(number==10)
num: int = 32
print(num!= 30)
print(num>= 32)
print(num<=43)
print(number>21)
print(number<21)

num1: int = 12
print(10< num1 < 24)
print('-' * 20)

# Logical Operators
name: str = 'Harsh'
age: float = 19.5
print(name == 'Harsh' and age < 22)
a: bool = False
b: bool = True
c: bool = True
print(a or b or c)
print(a and b and c)
print(not a == False)
print(not(a and b))

#Identity Operators

i: list[int] = {1,2,3}
i1: list[int] = {1,2,3}
print(i is i)
print(i is i1)
print(i is not i1)
print(i is not i)
