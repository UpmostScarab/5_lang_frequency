import re
from collections import Counter
MOST_COMMON_WORDS_COUNT = 10

def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return ' '.join(text_file.read().splitlines())


def get_most_frequent_words(text):
    words = re.findall(r'\w+',text.lower())
    return Counter(words)


if __name__ == '__main__':
    text = load_data(input('Введите путь к файлу с текстом: '))
    print(get_most_frequent_words(text).most_common(MOST_COMMON_WORDS_COUNT))
