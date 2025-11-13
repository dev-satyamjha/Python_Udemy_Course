import json

def exchange_rates() -> dict[str, float]:
    with open('currencies.json', 'r') as file:
        return json.load(file)

def instructions():
    print('1. Type <amount> <currency> to convert. e.g.(80INR)')
    print('2. Type LIST to list available currencies.')
    print('3. Type QUIT to exit.')

def convert(user_input: str, rates: dict[str, float]):
    currency_codes: list[str] = list(rates.keys())
    input_currency: str = user_input[-3:]

    if input_currency not in currency_codes:
        print(f"Input currency '{input_currency}' is invalid!!")
        return
    try:
        input_amount = float(user_input[:-3])
    except ValueError:
        print(f"{user_input} is an invalid input..Try writing like '80INR'")
        return

    base_conversion : float = input_amount/ rates[input_currency]
    print(f"{round(input_amount, 2):> 16} {input_currency}")
    print('-'*20)
    for currency_code in currency_codes:
        converted_amount : float = base_conversion*rates[currency_code]
        print(f'= {round(converted_amount, 2):>14} {currency_code}')
    print('-'*20)


def main() -> None:
    instructions()
    exchange_rate: dict[str,float] = exchange_rates()

    while True:
        user_input: str = input('Convert: ').strip().upper()
        if user_input == 'LIST':
            print(f"Available Currencies to convert: {', '.join(exchange_rate.keys())}")
            continue
        elif user_input == 'QUIT':
            print("BYE..BYE!!")
            break
        convert(user_input, exchange_rate)
if __name__ == '__main__':
    main()
