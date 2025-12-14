#Doc strings

def square(n):
    '''Take a number n and return the square of n.'''
    return n**2

print(square.__doc__)

print(print.__doc__)

print()

#Assert

def bank_account() -> None:
    account: int = 0
    assert account >=0

    print(f"The account is created with a balance of ₹ {account}")

bank_account()

def grade(grade:int) ->str:
    assert 0<=grade<=100, f'Invalid {grade}'
    return 'passed' if grade>=70 else 'failed'

print(grade(45))
print(grade(100))
print(grade(75))
