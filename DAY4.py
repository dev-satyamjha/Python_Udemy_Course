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
