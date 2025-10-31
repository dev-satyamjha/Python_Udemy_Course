# *args *kwargs
def greet(*person: str, greeting: str = 'Hey!'):
    print(person)
    for people in person:
        print(f"{greeting}{people}")
greet('Satyam', 'Allu Arjun', 'Roman')

def setup(Version : str , **kwargs):
    print('Version:', Version )
    print('Settings:', kwargs)

    if 'volume' in kwargs.keys():
        print(f"Volume set to: {kwargs.get('volume')}")
setup(Version='5.0', volume=15, System = 'Stereo', Brand = 'JBL' )

name: list[str] = ['Satyam', 'Keerthy', 'Priyanka', 'Niveditha', 'Roman']
settings: dict[str, float|str] = {'volume': 15, 'Brand':'JBL'}
print(*name, sep = ', ', end ='.\n')

def setup1(Version : str , **kwargs):
    print('Version:', Version )
    print('Settings:', kwargs)

    if 'volume' in kwargs.keys():
        print(f"Volume set to: {kwargs.get('volume')}")
setup1(Version='2.0', **settings )

#Positional , Keywords Arguments(* & /)

def add(first:int, second: int , /) -> None:
    print(first+second)

add(1, 2)

def greet1(names: list[str], * , greeting: str ):
    for name in names:
        print(f"{greeting} {name}")
greet1(['Satyam', 'James', 'Meowth'], greeting= 'Hello...')

def calc(a:float, b: float, /, *, operation: str) -> None:
    if operation == 'add':
        print(a + b)
    elif operation == 'subtract':
        print(a - b)
    elif operation == 'multiply':
        print(a * b)
    elif operation == 'divide':
        print(a/b)
    else:
        print('Can\'t Calculate it buddy..!!')
calc(9,6, operation='multiply')

def calc1(a: int, /, b:int, *, c:int) -> None:
    print(sum([a,b,c]))
calc1(23, b=34, c=56)
