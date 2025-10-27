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

#Parameters
def greet(name: str, language: str):
    if language == 'IN':
        print(f"Namaste, {name}!!")
    elif language == 'EN':
        print(f"Cheers, {name}!!")
    else :
        print(f"Hello, {name}!!")

greet('Satyam', 'IN')
greet('Roman', 'EN')
greet('Patron', 'IT')

def loop(times:int, text: str):
    for i in range(times):
        print(f"{text} : {i+1}")
loop(1, 'A')
loop(2, 'B')
loop(3, 'C')
