import webbrowser
import keyboard
import pyautogui
import shutil





"""
Делает скриншоты веб-страниц и закидывает в папку
"""


#закрыть вкладку cntl+w

for i in range(1,2):
    url = "http://cdot-nntu.ru/basebook/Osnovi_algoritm/files/assets/basic-html/index.html#page{}".format(i)
    #page = webbrowser.open_new_tab(url)
    screen = pyautogui.screenshot()
    keyboard.press_and_release("Ctrl+W")
    screen.save(r"C:\CREESTL\УНИВЕР\Алгоритмы и структуры данных\Учебник Капранова\page{}".format(i))




