from collections import Counter
import re

def punctuation_and_avg_word_length(text: str) -> None:

    punctuation_marks: list[str] = ['.', '!', '?', ':', ';','*','"',"'", '^', '&']
    punctuation_count: dict[str, int] = {
        mark: text.count(mark) for mark in punctuation_marks
    }

    words: list[str] = re.findall(r'\b\w+\b', text)
    total_words: int = len(words)
    total_characters: int = sum(len(word) for word in words)

    avg_word_length: float = (
        total_characters / total_words if total_words > 0 else 0
    )

    print('\nPunctuation count:')
    for mark, count in punctuation_count.items():
        print(f'{mark} : {count}')

    print(f'\nAverage word length: {avg_word_length:.2f}')

def analyze(filename:str) ->None:
    with open('sample.txt', 'r') as f:
        text: str = f.read()

        words: list[str] = re.findall(r'\b\w+\b', text.lower())
        word_counts: int = len(words)
        comma_counts: int = text.count(',')
        char_count_of_ws: int = len(text)
        whitespaces: int = sum(c.isspace() for c in text)
        top_words: list[tuple[str, int]] = Counter(words).most_common(3)

        print('-' * 30)
        print(f'Word count: {word_counts}')
        print(f'Commas used: {comma_counts}')
        print(f'Character count (incl. whitespaces): {char_count_of_ws}')
        print(f'Whitespace characters: {whitespaces}')
        print('')
        print('Top 3 most used words:')

        for word, count in top_words:
            print(f'> {word}: {count}')
        print('-' * 30)

        punctuation_and_avg_word_length(text)

def main():
    analyze('sample.txt')

if __name__=='__main__':
    main()
