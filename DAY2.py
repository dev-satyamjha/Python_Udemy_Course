# Type Hints
name: str = "Satyam"
age: int = 22
print(f"My name is {name} and my age is {age}.")

# Data Types

# Integers

age: int = 22
bal: int = 1000000
balls_left: int = 6
lucky_number: int = 12
principle_amount: int = 1000001
print(f"My age is {age} and my luck shines with number{lucky_number} ")
print(f"The left amount is {principle_amount - bal}")

# Trick
BILLION: int = 100_000_000_000
print(BILLION + 100)

# Floats
balance: float = 234567.90
roi: float = 7.8
interest: float = (balance * roi) / 100
print(interest)

# Round Concept in Floats
a: float = 0.1
b: float = 0.2
sum: float = round(a + b, 1)
print(sum == 0.3)

# Strings

text: str = "Hello, I am Satyam"
text2: str = "\"Hello! Feels good to be back\""  # Escaping double quotes
text3: str = 'I\'m you\'re best friend'  # Escaping single quotes

# String Concatenation
name: str = "Satyam"
action: str = " is salying"
sentence: str = name + action
print(sentence)

# multi line strings

quote: str = '''
 I am not a good guy,
 I am not a bad guy,
 I am the guy!
 '''
print(quote)

#booleans

is_awake: bool = True
is_snake: bool = False

print(is_snake)

print (True+False) # Bools addition

print (int(True)) # Display Bool's value

#type conversions

print(10+20) #normal addition
print(str(10) + '20') #string addition
print (float(10.5)) #float casting
print (int(10.9)) #int casting
