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
