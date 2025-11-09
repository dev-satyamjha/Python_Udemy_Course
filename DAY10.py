from decimal import Decimal

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

a = Decimal(0.1)
b = Decimal(0.2)
c = Decimal(0.3)

print(a)
