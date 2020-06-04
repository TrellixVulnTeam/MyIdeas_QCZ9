# -*- coding: utf-8 -*-

import keyboard

def change_language():
    keyboard.press_and_release("Shift+Alt")

while True:
    keyboard.wait("Alt")
    change_language()




