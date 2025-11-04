from typing import TextIO

#User Input
name: str = input("Enter your name to get it converted into ascii: ").strip().capitalize()
print(name)
ascii= [ord(n) for n in name]
print (f"The name's ascii value is : {ascii}")

print('----------------------------------')
#try&except
print("Sum of two numbers: ")
while True:
    try:
        m: str = input("Enter first number: ")
        n: str = input("Enter second number:")
        print(f"Sum of numbers : {int(m) + int(n)}")
        break
    except ValueError:
        print("Input in the form of digits only!!")

print('----------------------------------')

try:
    result: float = 1/0
    print(result)
except ZeroDivisionError:
    print("You cannot divide with zero, try any other number")

print('----------------------------------')

try:
    conversion: int = int("ten")
    print(conversion)
except ValueError as e:
    print(f"Error message: {e}")

print('----------------------------------')

try:
    a: float = float('six')
    print(12/a)

except ValueError as v:
    print(f"Error: {v}")
except ZeroDivisionError:
    print("Please do not divide by zero!!")

print('----------------------------------')

#finally
inp : str = 'One'

try:
    conv: int = int(inp)
    print(conv)

except ValueError :
    print(f"'{inp}' is not in digit format, Please input in digits only..!!")
finally:
    print("I don't care what's happening here, I'll run !")

print('----------------------------------')

path: str = 'text.txt'
file: TextIO | None = None

try:
    file = open(path, 'r')
    print('The file is opened!!')
    print('Content: ', file.read())

except FileNotFoundError as f:
    print(f"The file you were trying to open is not present : {f}")

finally:
    if file is not None:
        file.close()
        print("File is closed!")

print('----------------------------------')
