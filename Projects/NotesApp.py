def display_menu() -> None:
    print('Note-Taking Application')
    print('1. Add a Note')
    print('2. View Notes')
    print('3. Delete a Note')
    print('4. Exit')
    print('-' * 30)

def add_note() -> None:
    note: str = input("Enter your note: ")
    with open('notes.txt', 'a') as f:
        f.write(f'{note}\n')
    print("Note added successfully!!")
    print('-' * 30)

def view_notes() ->None:
    try:
        with open('notes.txt', 'r') as f:
            notes:list[str] = f.readlines()

            if notes:
                print('\nYour Notes: ')
                for i, note in enumerate(notes, start=1):
                    print(f"{i}: {note.strip()}")
            else:
                print("No notes found!")

    except FileNotFoundError:
        print("No such file exists!")

def delete_notes() ->None:
    view_notes()

    try:
        with open('notes.txt') as f:
            notes: list[str] = f.readlines()

            if notes:
                note_num: int = int(input("Enter note number to delete: "))
                if(1<=note_num<=len(notes)):
                    del notes[note_num -1]
                    with open('notes.txt', 'w') as f:
                        f.writelines(notes)
                        print("Note deleted successfully!!")
                else:
                    print("Invalid note number!")

    except FileNotFoundError:
        print("No notes found..!!")

    except ValueError:
        print("Invalid input..Please enter a number!")

def main() -> None:
    while True:
        display_menu()
        choice: int = int(input("Please select an option: "))

        if choice == 1:
            add_note()
        elif choice == 2:
            view_notes()
            print('-' * 70)
        elif choice == 3:
            delete_notes()
            print('-' * 70)
        elif choice == 4:
            print("Exiting the app...")
            break
        else:
            print("Please enter a valid option..!!")

if __name__ == "__main__":
    main()
