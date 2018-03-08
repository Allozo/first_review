import pymorphy2
import re

text = "wp.txt"

morph = pymorphy2.MorphAnalyzer()
analysis = morph.parse("hello")[0]
print(analysis)
analysis = morph.parse("привет")[0]
print(analysis)


with open(text, "r", encoding="UTF-8") as file:
    for line in file:
        if line != '\n':
            line = line.lower()                     # приводим к нижнему регистру
            line = re.sub(r'[^\w\s]', ' ', line)    # избавляемся от пробелов/ знаков препинания
            line = line.split()                     # получили простой лист слов
            size = len(line)
            for i in range(size):
                if i != size:
                    word = line[i]
                    next_word = line[i + 1]
