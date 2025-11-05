from typing import Final
import random

Lower_limit: Final[int]= 10
Upper_limt: Final[int] = 120
random_num: int = random.randint(Lower_limit, Upper_limt)
attempts: int = 0

def Kemu(msg: str) -> None:
    print(f"Kemu: {msg}")

Kemu("Are you a good guesser?")
Kemu(f"Guess a number between {Lower_limit} & {Upper_limt}: ")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts+=1
    except Exception as e:
        print(f"Error: {e} , You can guess numbers only here..!!")
        continue

    if user_guess < random_num:
        print("Your guessed number is lower than what it actually is ")
    elif user_guess > random_num:
        print("Your guessed number is higher than what it actually is ")
    else:
        if attempts == 1:
            print(f"BullsEye, You guessed it correctly in just {attempts} attempt only!!")
        else:
            print(f"You guessed it correctly in {attempts} attempts!!")
        print("Time for another round: ")

        random_num: int = random.randint(Lower_limit, Upper_limt)
        attempts = 0
        continue
