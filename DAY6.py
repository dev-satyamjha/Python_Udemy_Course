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

#return

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
