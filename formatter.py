from typing import Final

VERSION: Final[str] = '1.0'

def format_title(title: str):
    words: list[str] = []
    for word in title.split():
        words.append(word.capitalize())
    return ' '.join(words)

if __name__ == '__main__':
    st = 'Say my name loud..!'
    print(format_title(st))
