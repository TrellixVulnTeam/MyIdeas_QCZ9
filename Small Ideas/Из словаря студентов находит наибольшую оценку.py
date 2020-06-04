students = []

size = int(input('Введите количество студентов: '))
for i in range(size):
    students.append([])
    students[i].append ( input('Введите фамилию студента: '))
    students[i].append ( int(input('Введите оценку студента: ')))

def find_max (students):
    max_number = students[0][1]
    for i in range(len(students)):
        if students[i][1] > max_number:
            max_number = students[i][1]
    return max_number


for student in students:
    print(student)
print('Самая высокая оценка равна ' + find_max(students))