#Step 1
print("---WELCOME TO EXPENSE SPLITTER---")
while True:
    total_input = input("1. Enter the total amount in bill to split: ").strip()

    if total_input == "":
        print("You didn’t enter any amount... Try again.")
        continue
    if total_input.isdigit():
        total_bill = float(total_input)
        break
    else:
        print("Please enter a valid number...")

#Step 2
people: list[str] = []
print("2. Add Participants (Type 'Done' when names are entered): ")
while True:
    input_name: str = input("Names: ").capitalize()
    if input_name.strip() == '':
        print("No participant is added..Please add one!!")
        continue
    elif input_name in people:
        print("Name is already present, please try with a different name...!!")
    elif input_name.capitalize() == 'Done':
        break
    else:
        people.append(input_name)

#Step 3
print("3. Now type the percentage you want each person to pay: ")
print('(Type "even" if you want to split the bill equally.)')
people_dict: dict[str, float] = {}
total_percent: float = 100.0
for person in people:
    while True:
        percent_input: str = input(f"[{total_percent:.0f}% remaining] {person.capitalize()}: ").capitalize()
        if percent_input.strip() == '':
            print("You didn't enter any value..Try again(Enter 0 if you don't want to split): ")
            continue
        elif percent_input == 'Even':
            for nested_person in people:
                people_dict[nested_person] = (1/len(people)) * total_bill
            total_percent = '0'
            break
        if not percent_input.isdigit():
            print("Enter a valid percentage >= 0")
            continue
        percent_value = float(percent_input)
        if percent_value > 100:
            print("Enter a valid percentage <= 100...")
            continue
        if percent_value > total_percent:
            print(f"You have exceeded the total split share in bill...You only have {total_percent:.2f}% left!!")
            continue
        people_dict[person] = (percent_value / 100) * total_bill
        total_percent -= percent_value
        break

    if percent_input == "Even":
        break

total_split_amount = sum(people_dict.values())
amount_left = total_bill - total_split_amount

# Step 4
print('\n---Split Summary---')
for name, share in people_dict.items():
    print(f'{name.capitalize():10}: ₹{share:,.2f}')
print('----------------------')
print(f'Total amount splitted:  {total_split_amount}')
print(f'Amount still left:      {amount_left}')
print('------------------------------')
