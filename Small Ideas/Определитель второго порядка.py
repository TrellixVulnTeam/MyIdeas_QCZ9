
def paint():
    for element in opredelitel:
        print(element)

opredelitel = []
for i in range(2):
    opredelitel.append([])
    for j in range(2):
        opredelitel[i].append(0)
paint()
for x in range(2):
    for y in range(2):
        opredelitel[x][y]=input('Введите число: ')
        paint()
diag_1 = int(opredelitel[0][0]) * int(opredelitel[1][-1])
diag_2 = int(opredelitel[1][0]) * int(opredelitel[0][-1])
result = diag_1 - diag_2
print("Результат: " + str(result))

