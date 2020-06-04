with open('pi_million_digits.txt') as file:
    lines = file.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
date = input('Введите дату своего рождения без пробелов : ')
if date in pi_string:
    print('Your birthday is in the first million of pi digits')
else:
    print('Your birthday is not in the first million of pi digits')

