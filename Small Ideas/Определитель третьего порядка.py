def paint():
    for element in opredelitel:
        print(element)

opredelitel = []
for i in range(3):
    opredelitel.append([])
    for j in range(3):
        opredelitel[i].append(0)
paint()

for x in range(3):
    for y in range(3):
        opredelitel[x][y]=input('Введите число: ')
        paint()


first_diag = int(opredelitel[0][0]) * int(opredelitel[1][1]) * int(opredelitel[2][2])
triangle1_1 = int(opredelitel[0][2]) * int(opredelitel[1][0]) * int(opredelitel[2][1])
triangle1_2 = int(opredelitel[0][1]) * int(opredelitel[1][-1]) * int(opredelitel[2][0])
result_1 = first_diag + triangle1_1 + triangle1_2
second_diag =  int(opredelitel[0][-1]) * int(opredelitel[1][1]) * int(opredelitel[2][0])
triangle2_1 = int(opredelitel[0][0]) * int(opredelitel[1][-1]) * int(opredelitel[2][1])
triangle2_2 = int(opredelitel[0][1]) * int(opredelitel[1][0]) * int(opredelitel[2][-1])
result_2 = second_diag + triangle2_1 + triangle2_2
all_result = result_1 - result_2
print("Результат: " + str(all_result))











