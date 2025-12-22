from functools import lru_cache
import time
#Match

command: str = input("Enter a command: ").strip().lower()

match command:
    case 'start':
        print("Starting...")
    case 'stop':
        print("Stopping...")
    case 'exit' | 'quit':
        print("Exiting..")
    case 'help':
        print("There's no one to help you..you could only help yourselves..!")
    case _:
        print("Invalid command!!")

x_str, y_str  = input("Enter coordinates: ").split(sep = ',')
point: tuple[int, int] = (int(x_str), int(y_str))

match point:
    case (0, 0):
        print("You are at the origin!")
    case(x, 0):
        print(f"You are on the x-axis at {x}")
    case (0, y):
        print(f"You are on the y-axis at {y}")
    case (x, y):
        print(f"You are at ({x}, {y})")

finder: list[str] = input("Enter action: ").strip().lower().split()

match finder:
    case 'search', *images:
        print(f"Searching for image(s): {images}")
    case 'enlarge', image, amount:
        print(f"Enlarging {image} by {amount}")
    case 'upload', *images:
        print(f"Uploading image(s): {images}")
    case 'rename', old_image , new_image, if len(new_image) > 3:
        print(f"Renaming {old_image} to {new_image}")
    case unknown:
        print(f"Unknown action: {unknown}")


# @lru_cache

@lru_cache
def expensive(x:float):
    print('Calculating..')
    time.sleep(1)
    return x * x

print(expensive(2))
print(expensive(3))
print(expensive(4))
print(expensive(2))
print(expensive(4))
print(expensive(3))

while True:
    command1: list[str] =input("Command: ").strip().lower().split()

    match command1:
        case ['clear']:
            expensive.cache_clear()
            print("Cache cleared..!!")
        case ['square', number]:
            print(expensive(float(number)))
        case ['cache']:
            print(expensive.cache_info())
        case ['params']:
            print(expensive.cache_parameters())
        case ['exit'] | ['quit']:
            print("Quitting...")
            break

        case _:
            print("Unknow Command!!")
