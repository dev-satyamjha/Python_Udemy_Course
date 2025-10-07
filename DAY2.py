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
