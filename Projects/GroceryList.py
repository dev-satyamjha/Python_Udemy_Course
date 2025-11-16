db: dict[str, int] = dict()

def announcements(msg:str) -> None:
    print(f"System: {msg}")

def add_item() -> None:
    consecutive_items = 0
    while True:
        name: str = input("Enter an item: ").strip().capitalize()
        if name == "":
            consecutive_items +=1
            if consecutive_items == 2:
                announcements("Returning to Main Menu... ")
                return
            continue


        while True:
            quantity = (input("Enter quantity: ") ).strip()
            if quantity == "":
                print("Quantity cannot be empty. Please enter a number.")
                continue

            try:
                Quantity = int(quantity)

            except ValueError:
                print('Error, you didn\'t input a valid number' )
                continue

            if Quantity < 0:
                print("Quantity can't be negative ")
                continue
            else:
                break
        db[name] = Quantity
        announcements(f"Added : {name} x {quantity}")


def remove_item() -> None:
    name: str = input("Enter an item: ").strip().capitalize()
    try:
        db.pop(name)
        announcements("Successfully removed the item")
    except KeyError:
        print("Name is not present in grocery list!!")

def read_list() -> None:
    if db:
        print("<--------------------------------------------->")
        for k, v in db.items():
            print(f"{k.capitalize()}: {v}")
            print('-'*20)
    else:
        announcements("There are no groceries in the list..!!")


def modify_quantity() -> None:
    name: str = input("Enter item to modify: ").strip().capitalize()
    if name not in db:
        print("Item not present in list")
        return
    current = db[name]
    print(f"Current quantity for selected item: {current}")
    while True:
        new = input("Enter the new quantity: ").strip()

        try:
            new_qty = int(new)

        except ValueError:
            print("Please enter a valid number!")
            continue

        if new_qty < 0:
           print("Items can't be negative!")
           continue
        else:
           break
    db[name] = new_qty
    announcements(f"Updated Qunatity: {new_qty}")


def display_options():
    print("Options: ------")
    print("1.Display Options")
    print("2.Add in List")
    print("3.Remove from List")
    print("4.Read List")
    print("5.Modify Quantity")
    print("6.Quit")
    print("Press Enter twice under Option 2 to return to Main Menu")
    print("------")

def get_options(option:str):
    try:
        converted: int = int(option)
    except ValueError:
        announcements("Please Enter a valid option")
        return

    if converted == 1:
        display_options()
    elif converted == 2:
        add_item()
    elif converted == 3:
        remove_item()
    elif converted == 4:
        read_list()
    elif converted == 5:
        modify_quantity()
    elif converted == 6:
        announcements("Serve you soon!")
        raise SystemExit
    else:
        announcements("No such option exists..Enter any option between 1 to 6")
def main() -> None:
    display_options()

    while True:
        user_input: str = input("Your choice: ")
        get_options(user_input)

if __name__ == "__main__":
    main()
