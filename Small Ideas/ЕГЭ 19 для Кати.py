'''
На доске написано число 8. Раз в минуту Вася дописывает на доску одно число: либо вдвое большее
какого-то из чисел на доске, либо равное сумме каких-то двух чисел.
а) Может ли в какой-то момент на доске быть число 2020?
б) Может ли в какой-то момент сумма всех чисел равняться 72?
в) Через какое наименьшее время на доске может появиться число 832?

'''

import random
import time

def double(a):
    return a * 2

def count_sum(a, b):
    return a + b


def check_2020(nums):
    if 2020 in nums:
        return True

def check_72(nums):
    if sum(nums) == 72:
        return True

def check_832(nums):
    if 832 in nums:
        return True


nums = [8]

steps = 0

steps_for_832 = []

count = 1

res_2020 = None
res_72 = None
res_832 = None

def switch(nums):
    choice = random.randint(0, 1)
    if choice == 0:
        print("\nБыло выбрано удвоение")
        a = nums[random.randint(0, len(nums) - 1)]
        nums.append(double(a))
        print("Добавлено число ", str(double(a)))
        print("Все числа на доске: ",  str(nums))
        global steps
        steps += 1
    elif choice == 1:
        print("\nБыла выбрана сумма")
        if len(nums) >= 2:
            a = nums[random.randint(0, len(nums) - 1)]
            print("a = ", a)
            copy = nums.copy()
            copy.remove(a)
            b = copy[random.randint(0, len(copy) - 1)]
            print("b = ", b)
            nums.append(count_sum(a, b))
            print("Была выбранна сумма. Добавлено число ",  str(count_sum(a, b)))
            print("Все числа на доске: ", str(nums))
        else:
            print("Чисел слишком мало")

        steps += 1

while True:
    if max(nums) < 10000:
        switch(nums)
        if (check_2020(nums)):
            res_2020 = "Возможно появление числа 2020"
        if (check_72(nums)):
            res_72 = "Сумма чисел может быть равна 72"
        if check_832(nums):
            res_832 = "Число 832 появилось спустя " + str(steps) + " шагов"
            steps_for_832.append(steps)
    else:
        if count == 1000: # регулирует число раз, сколько доходит до 10000 и сбрасывается
            break
        count += 1
        nums = [8]
        steps = 0
        print("\n==================Начнем заново==================")
        print("Попытка " + str(count))
        time.sleep(1)
        switch(nums)
        if (check_2020(nums)):
            res_2020 = "Возможно появление числа 2020\n"
        if (check_72(nums)):
            res_72 = "Сумма чисел может быть равна 72\n"
        if check_832(nums):
            res_832 = "Число 832 появилось спустя " + str(steps) + " шагов"
            steps_for_832.append(steps)

# пишем результаты
if (res_2020 is not None):
    print(res_2020)
if (res_72 is not None):
    print(res_72)
if (steps_for_832 is not []):
    print("Наименьшее число шагов, за которое появилось число 832 равно ", min(steps_for_832))

with open("C:/Users/ACER/Desktop/results.txt", "a") as f:
    if (res_2020 is not None):
        f.write(res_2020)
        f.write("123")
    if (res_72 is not None):
        f.write(res_72)
    if (min(steps_for_832) != 0):
        f.write("\nНаименьшее число шагов, за которое появилось число 832, равно " + str(min(steps_for_832)))
    f.write("\n===========================\n\n")
    f.close()