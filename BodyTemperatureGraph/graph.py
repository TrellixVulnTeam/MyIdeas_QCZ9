'''

Идея следующая: вы заболели, каждый день черещ фиксированный промежуток времени вы меряете температуру, заносите
данные в два массива (температура, время), программа строит график роста температуры и сохраняет его в файл

'''

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import datetime
import os

def get_data():
    temps = []
    times = []
    date = input("Введите сегодняшнюю дату: \n")
    while True:
        temp = float(input("Введите температуру в формате 00.0:  (или 0 для завершения ввода данных)\n"))
        if temp == 0:
            break
        temps.append(temp)
        time = str(input("Введите время в формате '00:00':\n"))
        # приводим строку к формату datetime
        time = datetime.strptime(time, "%H:%M")
        times.append(time)
    return temps, times, date

def draw(temps, times, date):
    plt.figure(figsize=(10, 6))
    # рисую линию
    plt.plot(times, temps, linewidth=2, color="red")
    # для наглядности ставлю точки
    plt.scatter(times, temps)
    # здаю пределы температуры тела по y
    plt.ylim(35.0, 42.0)
    # задаю деления по оси y

    plt.gca().yaxis.set_major_locator(ticker.MultipleLocator(1))
    plt.gca().yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
    # делаю красивее отметки на оси x
    plt.gcf().autofmt_xdate()
    # это нужно, чтобы правильно отформатировать время на оси x
    formatter = mdates.DateFormatter('%H:%M')
    plt.gca().xaxis.set_major_formatter(formatter)
    plt.xlabel("Время")
    plt.ylabel("Температура")
    plt.title("Температура вашего тела", color="Green")
    # сохраняю файл
    plt.savefig(os.getcwd() + "/results/" + date + ".png")
    plt.show()

temps, times, date = get_data()

draw(temps, times, date)




