import random
import sys
import time

class SlotMachine:
    def __init__(self, credits: int) -> None:
        self.credits = credits
        self.symbol: dict[str, int] = {'🍒': 1, '🍊': 2, '🍋': 5}

    def spin(self, bet: int) -> None:
        if bet <= 0:
            print("Bet must be greater than 0...")
            return

        if self.credits >= bet:
            self.update_credits(-bet)

        else:
            print("Not enough credits...")
            return

        result: list[str] = []
        for _ in range(3):
            time.sleep(0.2)
            landed: str = random.choice(seq= list(self.symbol))
            print(landed, end= '', flush=True)
            result.append(landed)

        print()

        winnings: int = self.calculate_winnings(result, bet)
        print(f"Credits Won: {winnings}")

        self.credits += winnings
        if self.credits == 0:
            print("Game over..!")
            sys.exit()

        else:
            print(f"Credits remaining: {self.credits}")
            print('-'*30)

    def calculate_winnings(self, result : list[str], bet: int):
        previous: str = result[0]
        winnings: list[int] = []

        for symbol in result:
            if symbol == previous:
                winnings.append(self.symbol[symbol])
            else:
                winnings.clear()
                break

        return sum(winnings) * bet


    def update_credits(self, amount: int):
        self.credits += amount


    def play(self):
        print(f"Starting Credits: {self.credits}")
        print('-' * 30)

        while True:
            try:
                bet: int = int(input('Bet: '))
                self.spin(bet)
            except ValueError:
                print("Please Enter a valid number: ")


def main() -> None:
    pokies: SlotMachine = SlotMachine(200)
    pokies.play()

if __name__ == '__main__':
    main()
