"""Считает какой процент текста приходится на каждый символ алфавита"""

def count_char(text, char):#считает количество раз, сколько встречается данный символ в тексте
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("Ввдите имя текстового файла: ")
with open(filename, 'r') as f:#открытие файла на чтение
    text = f.read()
    for char in "abcdefghijklmnopqrstuvwxyz":#анализ кратности повторений каждого символа из алфавита
        percent = count_char(text, char) / len(text) * 100# рассчет процента
        print("{0} - {1}%".format(char, round(percent,2)))# форматированный вывод
