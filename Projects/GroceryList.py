db: dict[str, int] = dict()

def announcements(msg:str) -> None:
    print(f"System: {msg}")

def add_item() -> None:
    name: str = input("Enter an item: ").strip().capitalize()
    while True:
        try:
            quantity: int = int(input("Enter quantity: ") )
            db[name] = quantity
            announcements(f"Added : {name} x {quantity}")
        except ValueError:
            print('Error, you didn\'t input a valid number' )
            continue
        if quantity < 0:
            print("Quantity can't be negative ")
            continue
        else:
            break


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
            print('-'*40)
    else:
        announcements("There are no groceries in the list..!!")



def display_options():
    print("Options: ------")
    print("1.Display Options")
    print("2.Add in List")
    print("3.Remove from List")
    print("4.Read List")
    print("5.Modify Quantity")
    print("<--------------------------------------------->")

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

def main() -> None:
    display_options()

    while True:
        user_input: str = input("Your choice: ")
        get_options(user_input)

if __name__ == "__main__":
    main()
