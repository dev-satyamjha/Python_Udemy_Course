import string
import re

class PasswordValidator:
    def __init__(self) -> None:
        self.common_passwords: set[str] =self.load_common_passwords()

    @staticmethod
    def load_common_passwords() -> set[str]:
        with open('CommonPasswords.txt', 'r') as file: #Credits : danielmiessler(GitHub)
            return{line.strip() for line in file if line}

    def is_common(self, password: str) -> bool:
        return password in self.common_passwords

    def repeated(self, pw:str, len: int = 3) ->bool:
        return re.search(rf"(.)\1{{{len-1},}}", pw) is not None

    def rate(self, password: str) ->str:
        RED = "\033[31m"
        RESET = "\033[0m"
        if self.is_common(password):
            return f"{RED}poor{RESET}"

        score: int = 0
        if any(c.isupper() for c in password):
            score +=1
        if any(c in string.punctuation for c in password):
            score += 1
        if any(c.isdigit() for c in password):
            score += 1
        if len(password) >= 10:
            score +=1
        if self.repeated(password, 3):
            score -= 1

        if score == 4:
            return "secure"
        if score == 3:
            return "strong"
        if score == 2:
            return "medium"
        else:
            return "weak"

    def missing_requirements(self, password:str):
        missing =[]

        if not any(c.isupper() for c in password):
            missing.append("Add an uppercase letter[A-Z]")
        if not any(c in string.punctuation for c in password):
            missing.append("Add a special character[@#!$%]")
        if not any(c.isdigit() for c in password):
            missing.append("Add a digit[0-9]")
        if len(password) < 10:
            missing.append("Add more characters")
        return missing

def main() -> None:
    GREEN = "\033[32m"
    ORANGE = "\033[38;5;214m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    RESET = "\033[0m"

    validator: PasswordValidator = PasswordValidator()
    print("Welcome to Password Quality Checker...")

    while True:
        password: str = input("Please Enter a password to check:").strip()
        rating: str = validator.rate(password)

        if rating == 'secure':
            print(f'Password level: {ORANGE}secure{RESET} ')
        else:
            if rating == 'strong':
                print(f'Password level: {GREEN}strong{RESET} ')
            elif rating == 'medium':
                print(f'Password level: {YELLOW}medium{RESET} ')
            else:
                print(f'Password level: {RED}weak{RESET} ')

            missing = validator.missing_requirements(password)
            if missing:
                print('You should: ')
            for requirement in missing:
                print(f"•{requirement} to make your password secure")


if __name__ == '__main__':
    main()
