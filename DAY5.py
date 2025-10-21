#If, Else and Elif Statements

age = int(input("Enter age: "))
name= str(input("Enter your name: ")).strip().capitalize()
if age >=18:
    print("You are eligibile to vote!!")
elif name == "Satyam":
    print(f"I already told that you can vote {name}!!")
else:
    print(f"You can vote after {18 - age} years(s)")

#If else Shortened

condition: bool = True
result: str = 'Yes' if condition else 'No'
print(result)

age = int(input("Enter your age: "))
message: str = 'You can get married!!' if age>= 21 else (f"Wait for {21 - age} years to get married...!!")
print(message)

n = int(input("Enter a number: "))
print('Even Number' if n%2==0 else 'Odd Number!!' )

state : bool = True
print('I will pass') if state else print('I will fail for sure!!')
