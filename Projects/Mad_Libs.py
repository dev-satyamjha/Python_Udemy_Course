print('Your story')
name: str = input("Enter name: ")
noun: str = input("Enter Boy/Girl: ")
pronoun: str = input("Enter Pronoun: ")
pronoun2: str = input("Enter him/her: ")
city: str = input("Enter city name: ")
adjective: str = input("Enter speciality of city : ")
verb: str = input("Enter an action: ")
noun2: str = input("Enter any character/group/creature/person:  ")
weapon: str = input("Enter a weapon or type nothing: ")
verb2: str = input("Enter an action: ")
verb3: str = input("Enter an action: ")

story: str = f'''
This is the story of {name}, a {noun} hailing from {city} famous for it's {adjective}.
One day, the {noun} decided to {verb} and took required steps for it.
The {noun} lands in trouble when {pronoun} finds that {pronoun} is surrounded by {pronoun2} {noun2} and thinks of a way to escape it.
The {noun} realizes the danger and chose {weapon} to deal with the situation.
The {noun} then takes out {weapon} and then {verb2} the {noun2} to {verb3}. The {noun} achieves his motive and thanks god for saving {pronoun2}.
'''

print("Resut:")
print(story)
