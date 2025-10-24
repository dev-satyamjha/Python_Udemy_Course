#Step 1
from typing_extensions import List


print("---WELCOME TO EXPENSE SPLITTER---")
total_bill: float = float(input("1. Enter the total amount in bill to split: "))

#Step 2
people: list[str] = []
print("2. Add Participants (Press Enter on an empty line when you are done): ")
while True:
    input_name: str = input("Names: ").capitalize()
    if input_name.strip() == '':
        break
    elif input_name in people:
        print("Name is already present, please try with a different name...!!")
    else:
        people.append(input_name)

#Step 3
print("3. Now type the percentage you want each person to pay: ")
print('(Type "even" if you want to split the bill equally.)')
people_dict: dict[str, float] = {}
total_percent: float = 100.0
for person in people:
    percent_input: str = input(f"[{total_percent:.0%}remaining] {person.captialize():}").capitalize()

    if percent_input.strip() == '':
        percent_input = '0'
    if percent_input.strip() == 'even':
        for nested_person in people:
            people_dict[nested_person] = (1/len(people)) * total_bill
            break
    else:
      people_dict[person] = (float(percent_input)/100) * total_bill
      total_percent -= float(percent_input)

# Step 4
print('\n---Split Summary---')
for name, share in people_dict.items():
    print(f'{name.capitalize(): 10}: ₹{share: , .2f}')
print('----------------------')
