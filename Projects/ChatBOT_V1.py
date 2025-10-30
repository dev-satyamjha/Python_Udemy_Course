from datetime import datetime

def contains(terms: list[str] , contents: str):
    matches: list[bool] = []
    for term in terms:
        matches.append(term in contents.lower())

    return any(matches)

def response(text: str):
    text = text.lower()

    if contains(['hello', 'hi'], text):
        return 'Hello Bright Mind, how may i help?'
    elif contains(['how are you','are you', 'what\'s up', 'doin','going', 'kaise ho'], text):
        return 'All good and you?'
    elif contains(['time', 'clock', 'samay', 'hour', 'minute'], text):
        return f'It is {datetime.now().strftime("%I:%M:%S:%p")}'
    elif contains(['taarik', 'dinank', 'date'], text):
        return f"The date is : {datetime.now().strftime('%d-%m-%Y')}"
    elif contains(['mahina', 'month'], text):
        return f"The month is: {datetime.now().strftime('%B')}"
    elif contains(['year', 'saal', 'ispi'], text):
        return f"The current year is: {datetime.now().strftime('%Y')}"
    elif contains(['creator', 'who', 'name', 'owner'], text):
        return 'Satyam'
    elif contains(['country','nation', 'desh', 'state', 'place'], text):
        return 'The great nation \'INDIA\''
    elif contains(['language', 'bhasha', 'dialect', 'communication',], text):
        return 'The mother of all language : \'Sanskrit\''
    elif contains(['bye', 'goodbye', 'see you', 'later'], text):
        return 'Sorry to see you go, hope to talk soon!'
    elif contains(['day', 'din', 'today'], text):
        return f"Today is:'{datetime.now().strftime('%A')}'"
    else:
        return("Sorry, I can't help with that!!")

while True:
    user_input: str = input('You: ')
    print(f"Bot: {response(user_input)}")
    if 'bye' in user_input.lower():
        break
