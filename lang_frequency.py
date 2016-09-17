import re
from collections import Counter

def load_data(filepath):
    with open(filepath, 'r') as text_file:
        return ' '.join(text_file.read().splitlines())


def get_most_frequent_words(text):
    words = re.findall(r'\w+',text.lower())
    return Counter(words)


if __name__ == '__main__':
    text = load_data(input('Введите путь к файлу с текстом: '))
    print(get_most_frequent_words(text).most_common(10))
