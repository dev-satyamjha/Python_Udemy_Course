#Modules
from random import *
from secrets import *
import formatter
import faker
from math import sqrt as s, log as l, cos as c, sin as i

print(s(150))
print(i(90))
print(l(10))
print(c(180))
print('----------------------------------')

#*impots --> This is just an example of how you can import all functionality of math module
#from math import *
# print(sqrt(25))
# print(log(10))
# print(cos(90))

#*modules

print(choice([12,10,8]))
print(randint(10,20))
print('----------------------------------')

#Custom Modules

print('Version: ', formatter.VERSION)
user_input = input("Enter the Title: ")
print(f"Title: {formatter.format_title(user_input)}")
print('----------------------------------')

#Pip --> It is used to install external libraries using pip install 'library'
#It can't be run directly, either create a virtual env or use UV to run a single file

fake = faker.Faker()
print(fake.name())
print(fake.email())
print(fake.address())
print('----------------------------------')
