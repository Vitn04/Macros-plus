# Скрипт Макросов мыши (Режим: 'Standard')


import sys


def Main_Macros_Mouse(): # Функция консольного управления макросов мыши

    import time
    import os
    import keyboard
    import pyautogui as pg
    import Function
    

    Comand_field = None # - Поле ввода 
    M_k_t = 100  # - Mouse_Klick_time
    M_r = 2  # - Mouse_response
    M_s = 'Ctrl + q' # - Mouse_start
    M_st = 'esc' # - Mouse_stop

    Mouse_Klick_time = M_k_t  # - Значение продолжительности нажатий Дабл-Кликов в секунду
    Mouse_response = M_r  # - Значение задержки запуска в секунду
    Mouse_start = M_s  # - Клавиша запуска макросов мыши
    Mouse_stop = M_st  # - Клавиша выключение макросов



    while Comand_field !='end':

        if Comand_field !='end':
            os.system('cls')
            print()
            print("_____________Ваши настройки(Режим: Standard)_____________"),print()         
            print(" < Значение продолжительности нажатий в секундах:", Mouse_Klick_time // 10)
            print(" < Значение задержки запуска в секундах:", Mouse_response )
            print(" < Клавиша запуска макросов мыши:", Mouse_start )
            print(" < Клавиша выключения макросов:", Mouse_stop ),print()
            print("_____________Для просмотра информации: info_____________ "),print()
            print("<<<User_1 console.")
            Comand_field = input('Ввод: ')


        if Comand_field == 'start': # - условие запуска 
                

            def Macros_Mouse(): # - Функция Макросы мыши

                Mouse_Klick_time = M_k_t
                
                time.sleep(Mouse_response)
                while Mouse_Klick_time != 0:
                    if Mouse_Klick_time == 0:
                        break 
                    pg.doubleClick()
                    #print(Mouse_Klick_time)
                    Mouse_Klick_time -= 1

            os.system('cls')
            print()
            print("_____________Ваши настройки(Режим: Standard)_____________"),print()
            print(" < Значение продолжительности нажатий в секундах:", Mouse_Klick_time // 10)
            print(" < Значение задержки запуска в секундах:", Mouse_response )
            print(" < Клавиша запуска макросов мыши:", Mouse_start )
            print(" < Клавиша выключения макросов:", Mouse_stop ),print()
            print("_________________________________________________________"),print()

            Function.func_color_text.text_color_green("___________________________"),print()
            Function.func_color_text.text_color_green("Макросы мыши активированы!")
            Function.func_color_text.text_color_green("___________________________")

            keyboard.add_hotkey(Mouse_start, lambda: Macros_Mouse() ) # - бинд запуска макросов

            keyboard.wait(Mouse_stop) # - бинд конца макросов
            os.system('cls')

            Function.func_color_text.text_color_red("___________________________"),print()
            Function.func_color_text.text_color_red("Макросы мыши деактивированы!")
            Function.func_color_text.text_color_red("___________________________")

            time.sleep(1)
            Comand_field = 'end'


        if Comand_field == 'settings': # - условие запуска настроек макросов

            os.system('cls')

            print()
            M_k_t = int(input("Введите Значение продолжительности нажатий в секундах: "))  
            M_k_t = M_k_t * 10
            Mouse_Klick_time = M_k_t

            print()
            M_r = int(input("Введите значение задержки запуска в секундах: ")) 
            Mouse_response = M_r


            os.system('cls')
            print("настройки установлены!")
            time.sleep(2)
            os.system('cls')


        if Comand_field =='info': # условие запуска информации об командах консоли
            i = 10
            while i != -1:
                time.sleep(1.3)
                os.system('cls')  
                print()             
                print('________________info________________')
                print("- Для запуска напишите: start")
                print("- Для настройки напишите: settings")
                print("- Для выхода напишите: end")
                print('_______________(',i,')_______________')
                i -= 1

    else:
        print("командная строка закрыта.")
        sys.exit()





    

    




    