from typing import TextIO
path: str = 'text.txt'
file: TextIO | None = None

try:
    file = open(path, 'r')
    print('The file is opened!!')
    print('Content: ', file.read())

except FileNotFoundError as f:
    print(f"The file you were trying to open is not present : {f}")

finally:
    print("File is closed!")

print('----------------------------------')
