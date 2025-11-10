#Functions
def loop():
    for i in range(5):
        print(f"Looping till {i+1}")
loop()
loop()
print("----------")

def greet():
    print("Hey, Jai Shree Ram!!")
for i in range(3):
    greet()

#Pass
def jump():
    pass

test: bool = False
if test:
    pass
else:
    print("Test is not happening tommorow!!")

#Parameters and Arguments
def greet1(name: str, language: str):
    if language == 'IN':
        print(f"Namaste, {name}!!")
    elif language == 'EN':
        print(f"Cheers, {name}!!")
    else :
        print(f"Hello, {name}!!")

greet1('Satyam', 'IN')
greet1('Roman', 'EN')
greet1('Patron', 'IT')

def loop1(times:int, text: str):
    for i in range(times):
        print(f"{text} : {i+1}")
loop1(1, 'A')
loop1(2, 'B')
loop1(3, 'C')

def greet2(name: str, greeting: str = 'Hey!'):  #default param
    print(f"{greeting} {name}, how are you?")
greet2('Indently')

def add(label: str , a: int, b: int):
    print(f"{label}: {a + b}")
add('My sum is', 45, 90)

#Return

def add1(a:float, b:float) -> float:
    return a + b

print(add1(1 , 2))
print(add1(87 , 67))

def person(name:str) -> str:
    return name.capitalize()
print(person('satyam'))
print(person('ROMAN'))

print('----------------------------------')

def search(user:str, db:dict[str, int]) -> int | None :
    print(f"Seraching for {user}...")
    if user in db.keys():
        print(f"{user} is found...!")
    else:
        print(f"{user} is not found...!")
    return db.get(user)

db: dict[str, int] = {'Satyam' : 12, 'Allu Arjun': 8, 'Roman' : 7, 'Keerthy': 20}
print(search('Satyam', db))
print(search('Allu Arjun', db))
print(search('Keerthy', db))
print(search('Undertaker', db))

print('----------------------------------')

#Recursion

import time
connection: bool = False
def connect(tries : int = 3) -> None:
    if tries != 0 :
        print("Attempting to Connect...")
        time.sleep(1)
        if connection :
            print('Wohoo..We are connected!!')
        else:
            print("Uh oh! Failed to connect")
            connect(tries - 1)
    else:
        print("Maximum limit reached..!")

connect()

print('----------------------------------')

n = int(input("Enter a number: "))
def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)
for i in range (n):
    print(fibonacci(i))

print('----------------------------------')
