#If, Else and Elif Statements

age = int(input("Enter age: "))
name= str(input("Enter your name: ")).strip().capitalize()
if age >=18:
    print("You are eligibile to vote!!")
elif name == "Satyam":
    print(f"I already told that you can vote {name}!!")
else:
    print(f"You can vote after {18 - age} years(s)")
