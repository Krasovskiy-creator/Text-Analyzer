# https://colab.research.google.com/drive/1M--JHUZWHshJ3XD3KsIECg-NV4OPodYo#scrollTo=jHy6D_pl3MX1
import pandas as pd
import string
import nltk
nltk.download('punkt')
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
import csv
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

text = input("Введите текст: ")

# Удалить знаки препинания и привести текст к нижнему регистру
text = text.translate(str.maketrans("", "", string.punctuation))
text = text.lower()

# Разбить текст на токены
tokens = word_tokenize(text)

# Удалить запятые и прочие знаки препинания из списка токенов
tokens = [token for token in tokens if token.isalnum()]

# Создать биграммы и триграммы
bigrams = list(ngrams(tokens, 2))

# Создать список только для биграммов
bigrams_list = [bigram for bigram in bigrams if len(bigram) == 2]

# Посчитать количество биграммов
bigram_freq = FreqDist(bigrams_list)


# Получить топ-10 наиболее часто встречающихся биграмм
top_bigrams = bigram_freq.most_common(10)

# Отсортировать биграммы по количеству
sorted_bigrams = sorted(bigram_freq.items(), key=lambda x: x[1], reverse=True)

# Получить названия биграмм и их частоты в отдельные списки
bigram_names = [bigram[0][0] + " " + bigram[0][1] for bigram in top_bigrams]
bigram_counts = [bigram[1] for bigram in top_bigrams]

# Создать диаграмму
plt.bar(bigram_names, bigram_counts)
plt.title("Top 10 Bigrams")
plt.xlabel("Bigram")
plt.ylabel("Frequency")
plt.xticks(rotation=45)

# Отобразить диаграмму

# Вывести статистику по тексту
print("Количество символов:", num_chars)
print("Количество слов:", num_words)
print("Плотность слова:", word_density)

plt.show()

# Создать DataFrame из результатов
df = pd.DataFrame(list(bigram_freq.items()), columns=["Биграммы", "Количество"])


# Вывести первые 10 строк DataFrame
df.head(10)

# Сохранить результаты в файл
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Биграммы", "Количество"])
    for bigram, count in bigram_freq.items():
        writer.writerow([bigram[0] + " " + bigram[1], count])
