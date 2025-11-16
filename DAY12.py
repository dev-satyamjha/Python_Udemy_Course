#OOP

#Classes & Objects
class Lamp:
    def __init__(self, brand: str) -> None:
        self.brand = brand
        self.state = 'OFF'

    def turn_on(self) -> None:
        self.state = 'ON'
        print(f"{self.brand}: ON")

    def turn_off(self) -> None:
        self.state = 'OFF'
        print(f"{self.brand}: OFF")

LG: Lamp = Lamp('LG')
Samsung: Lamp = Lamp('Samsung')
LAVA: Lamp = Lamp('LAVA')
Motorola: Lamp = Lamp('Motorola')

LG.turn_on()
LG.turn_off()
Samsung.turn_on()
Samsung.turn_off()
LAVA.turn_on()
Motorola.turn_on()


print("LG", LG.state)
print("Samsung", Samsung.state)
print("LAVA", LAVA.state)
print("Motorola", Motorola.state)

#init

class BankAccount:
    def __init__(self, owner: str, balance: int, age: int, branch: str) -> None:
        self.owner = owner
        self.balance = balance
        self.age = age
        self.branch = branch
        print(f"Opening Bank Account for '{self.owner}' with a balance of ₹ {self.balance} in {self.branch} Branch at the age of {self.age}")

    def deposits(self, amount: int):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Amount: ₹{amount} ; Updated Balance: ₹{self.balance}")
        elif amount == 0:
            print(f"You haven't deposited a single penny and so the your balance remains same ₹{self.balance}")
        else:
            print(f"{self.owner} ; enter amount, don't act like bakrupt!!")

    def display_balance(self):
        print(f"{self.owner}, Your current Bank Balance is: ₹{self.balance}")



Satyam_Account: BankAccount = BankAccount('Satyam', 100000, 22, 'Adityapur' )
Aanya_Account: BankAccount = BankAccount('Aanya', 100000, 21, 'Adityapur')
Harsh_Account: BankAccount = BankAccount('Harsh', 10000, 19, 'Adityapur')
AA_Account: BankAccount = BankAccount('Allu Arjun', 10000000, 42, 'Hyderabad')

Satyam_Account.deposits(1000000)
Satyam_Account.display_balance()
print('-'*57)
Aanya_Account.deposits(1000000)
Aanya_Account.display_balance()
print('-'*57)
Harsh_Account.deposits(0)
Harsh_Account.display_balance()
print('-'*57)
AA_Account.deposits(-12)
AA_Account.display_balance()
print('-'*57)
