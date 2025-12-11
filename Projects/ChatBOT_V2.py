from datetime import datetime

def contains(terms: list[str], content: str) -> bool:
    matches: list[bool]= []
    for term in terms:
        matches.append(term in content.lower())
    return any(matches)

class ChatBot:
    def __init__(self, name:str) -> None:
        self.name = name
        self.history: list[str] = []

    def response(self, text: str):
        text = text.lower()

        if contains(['tommorow', 'tomm', 'tomorow', 'tmrw', 'tomorow\'s', 'tommorow\'s'], text) and contains(['weather', 'climate','wethr', 'wthr', 'climet'], self.history[-1]):
            return 'Tommorow looks chilled with 9°C temperature.'

        if contains(['usecase', 'reason of invention', 'main', 'used for', 'work'], text):
            return 'I\'m just a basic ChatBot for timepass.'

        elif contains(['created','creator','maker', 'maalik','inventor'], text):
            return 'My creator\'s name is Satyam.'

        elif contains(['origin','region','country', 'from'], text) and contains(['created','creator','maker', 'maalik','inventor'], self.history[-1]):
            return 'My creator is from India.'

        elif contains(['best country', 'best desh', 'best place', 'which country is best', 'which country best', 'which country'], text):
            return 'The best country is India.'

        elif contains(['famous', 'special', 'especiality'], text) and contains(['best country', 'best desh', 'best place'], self.history[-1]):
            return 'It is damous for it\'s spices.'

        elif contains(['food', 'khana', 'street food', 'dish', 'dishes'], text):
            return 'The best type of foods are available in India.'

        elif contains(['time', 'samay', 'hour', 'tym', 'waqt'], text):
            return f'The time is {datetime.now().strftime("%H:%M:%S")}'

        elif contains(['12 hrs', '12 hour format', '12', 'format', 'am', 'pm'], text) and contains(['time', 'samay', 'hour', 'tym', 'waqt'], self.history[-1]):
            return f'{datetime.now().strftime("%I:%M:%S:%p")}'

        elif contains (['date','taarikh', 'taarik','dinank'], text):
            return f'Today\'s date is {datetime.now().strftime('%d %b')}'

        elif contains (['full', 'format', 'date', 'year', 'whole', 'saal'], text) and contains(['date','taarikh', 'taarik','dinank'], self.history[-1]):
            return f'{datetime.now().strftime('%d %B, %Y')}'

        elif contains(['day', 'today', 'din', 'aaj kya hai', 'which day'], text) and contains(['date','taarikh', 'taarik','dinank','full', 'format', 'date', 'year', 'whole', 'saal'], self.history[-1]):
            return f'Today is {datetime.now().strftime("%A")}'

        elif contains(['weather', 'climate', 'wethr', 'mausam'], text):
            return 'It\'s currently chilling with 15°C with no signs of rain.'

        elif contains(['help', 'commands', 'guide', 'instructions'], text):
            return ('I got you: help/commands/guide for help, weather/climate(current climate), tommorow weather/climate, hello/hi,'
                    'what time it is, bye/goodbye/see you')

        elif contains(['hello', 'hey','hlw','hi'], text):
            return 'Hello there, how may i help you?'

        elif contains(['goodbye', 'bye', 'see ya', 'see you', 'exit', 'i\'m done'], text):
            return 'Goodbye, take good care of yours!'

        return 'Sorry, I can\'t answer that now!'

    def remember(self, text:str) -> None:
        self.history.append(text.lower())
        if len(self.history) > 2:
            self.history.pop(0)

    def run(self) :
        print("Type help/commands for instructions.\nType 'bye'/'goodbye' to exit.")
        while True:
            user_input: str = input('You: ')
            bot_reply: str = self.response(user_input)
            print(f"{self.name}: {bot_reply}")

            if contains(['goodbye', 'bye', 'see ya', 'see you', 'exit', 'i\'m done'], user_input):
                break

            self.remember(user_input)

def main():
    bot:ChatBot = ChatBot('Anokhi')
    bot.run()

if __name__ == '__main__':
    main()
