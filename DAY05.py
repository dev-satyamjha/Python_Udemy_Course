#If, Else and Elif Statements
import time
age = int(input("Enter age: "))
name= str(input("Enter your name: ")).strip().capitalize()
if name == "Satyam" and age >= 18:
    print(f"I already told that you can vote {name}!!")
elif age >= 18:
    print("You are eligible to vote..!")
elif name == "Satyam":
    print(f"I already told that you can vote {name}!!")
else:
    print(f"You can vote after {18 - age} years(s)")
print('-----------------------------------------')

#If else Shortened

condition: bool = True
result: str = 'Yes' if condition else 'No'
print(result)
print('----------------------------------')

age = int(input("Enter your age: "))
message: str = 'You can get married!!' if age>= 21 else (f"Wait for {21 - age} years to get married...!!")
print(message)
print('----------------------------------')

n = int(input("Enter a number: "))
print('Even Number' if n%2==0 else 'Odd Number!!' )
print('----------------------------------')

state : bool = True
print('I will pass') if state else print('I will fail for sure!!')
print('----------------------------------')

#Loops
#for loop
people: list[str] = ['Satyam', 'Dhoni', 'Allu Arjun', 'Roman Reigns']
for person in people:
    print(f"{person} is the best one around here!!")
print('----------------------------------')

for i in range(5):
    print(f'Hello, World!!')
print('----------------------------------')

for _ in range(2):
    print(f'You can do it!!')
print('----------------------------------')

#While Loop

i: int = 3
while i>0:
    i -= 1
    print(i)
print('----------------------------------')

connected: bool = True
i: int = 3
while connected:
    if i == 0:
        connected = False
        print("OFFLINE!!")
    else:
        print('ONLINE....!!')
        i-= 1
        time.sleep(1)
print('----------------------------------')

while True:
    new = str(input("Enter a name: "))

    if new.strip().capitalize() == 'Exit':
        break
    else:
        print(f"The name is: {new}")
print('----------------------------------')

l1: list[str] = ['Puppy', 'Satyam','Allu Arjun', 'Vampire']
for p1 in l1:
    if p1 == 'Vampire':
        print('Oh no...Vampire!! Run as fast as you can......')
        break
    else:
        print(f"Oh Hello Cutieee {p1}!!")
print('----------------------------------')

#Continue
num: list[int] = [1, 3, 5, 7, 9, 11, 12, 13, 15]
for n in num:
    if n%2 == 0:
        print(f"{n}:An even number is encountered!!")
        continue
    print(f"{n} is an odd number.")
print('----------------------------------')

#Continue

num: int = 10
while num>0:
    print(f"Current Number is : {num}")
    num -= 1
    if num == 5:
        print("We have completed the half path...!!")
        continue
    elif num == 0:
        print("Counting Ends!!")
        break
print('----------------------------------')

# else loop
names: list[str]= ['India', 'Satyam', 'Army', 'Allu Arjun', 'Keerthy', 'Priyanka']
for n1 in names:
    print(n1)
else:
    print("Everyone's name is printed!!")
print('----------------------------------')

i4: int = 0
while i4 < 10:
    i4 += 1
    print(f"Current number is: {i4}")
else:
    print("Loop wasn't interrupted")
print('----------------------------------')

i5: int = 0
while i5 > 10:
    i5 += 1
    print(f"Current number is: {i5}")
else:
    print("Loop was interrupted")
print('----------------------------------')

emp : list[str] = []
for e in emp:
    print(e)
else:
    print("List is empty!!")
print('----------------------------------')

while True:                             # Infinite Loop
    inp = str(input("Enter a name: "))
    print(f"The name is: {inp}")
