# Дополнительный функционал к программе

import os
import time
import ctypes


class func_size_console(): # класс функций размера окна консоли

    def Info_size(): # функция информации об размере окна
        y = os.get_terminal_size().lines
        x = os.get_terminal_size().columns

        print("Ширина окна(x): ",x)
        print("Высота окна(y): ",y)
        time.sleep(5)

    def Setting_size(): # функция установки размера окна
        cmd = 'mode 70,20'
        os.system(cmd)



class func_name_console(): # класс функций смены названия консольного окна

    def Name_console(): # функция смены имени консоли
        ctypes.windll.kernel32.SetConsoleTitleA(b"Macros+")



class func_color_text(): # класс функций цветного текста

    def text_color_yellow(text): # функция желтого текста
        print("\033[33m {} \033[0m" .format(text))

    def text_color_green(text): # функция зеленого текста
        print("\033[32m {} \033[0m" .format(text))

    def text_color_red(text): # функция красного текста
        print("\033[31m {} \033[0m" .format(text))



class Privat_variables(): # класс приватных переменных

    __ProgVersion__ = "vitn.net Macros+ v1.0"