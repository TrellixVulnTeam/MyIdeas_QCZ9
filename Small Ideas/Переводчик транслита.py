question = input('С какой раскладки хотитое перевести?(eng/rus) ')
line = []
if question == 'eng':
    word = input('Введите слово ')
    for el in word:
        line.append(el)
    for letter in line:
        index = line.index(letter)
        if line [index] == 'q':
            line[index] = str('ц')
string = ''.join(line)
print(string )