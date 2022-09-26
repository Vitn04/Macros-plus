# Скрипт Макросов мыши (режим: 'ultra')




def Main_Macros_Mouse_ultra(): # Функция консольного управления макросов мыши (Ultra)
  
    import sys
    import mouse
    import os
    import time
    import keyboard
    import pyautogui as pg
    import Function
    

    Comand_field = None # - Поле ввода 
    M_k_t = 300  # - Mouse_Klick_time
    M_r = 2  # - Mouse_response
    M_s = 'Ctrl + q' # - Mouse_start
    M_st = 'esc' # - Mouse_stop
    U_s = 'u1 (10 сек)' # - Показатель Режима Macros Ultra

    Mouse_Klick_time = M_k_t  # - Значение продолжительности нажатий Кликов в милисекунду
    Mouse_response = M_r  # - Значение задержки запуска в секунду
    Mouse_start = M_s  # - Клавиша запуска макросов мыши
    Mouse_stop = M_st  # - Клавиша выключение и выхода макросов



    while Comand_field !='end':

        if Comand_field !='end':
            os.system('cls')
            print()
            print("_______________Ваши настройки(Режим: Ultra)_______________"),print()
            print(" < Режим Ultra макросов:", U_s )
            print(" < Значение задержки запуска в секундах:", Mouse_response )
            print(" < Клавиша запуска макросов мыши:", Mouse_start )
            print(" < Клавиша выключения макросов:", Mouse_stop ),print()
            print("_____________Для просмотра информации: info_____________ "),print()
            print("<<<User_1 console.")
            Comand_field = input('Ввод: ')



        if Comand_field == 'start': # - условие запуска 

            def Macros_Mouse_ultra(): # - Макросы мыши (Ultra)
                
                time.sleep(Mouse_response)
                Mouse_Klick_time = M_k_t
                
                while Mouse_Klick_time != 0:
                    if Mouse_Klick_time !=0:
                        time.sleep(0.01)
                        mouse.double_click()
                        Mouse_Klick_time -= 1
            
                        if Mouse_Klick_time == 0:
                            break


            os.system('cls')
            print()
            print("_______________Ваши настройки(Режим: Ultra)_______________"),print()
            print(" < Режим Ultra макросов:", U_s )
            print(" < Значение задержки запуска в секундах:", Mouse_response )
            print(" < Клавиша запуска макросов мыши:", Mouse_start )
            print(" < Клавиша выключения макросов:", Mouse_stop ),print()
            print("_________________________________________________________ "),print()
            
            Function.func_color_text.text_color_green("___________________________"),print()
            Function.func_color_text.text_color_green("Макросы мыши активированы!")
            Function.func_color_text.text_color_green("___________________________")
            
            keyboard.add_hotkey(Mouse_start, lambda: Macros_Mouse_ultra() ) # - бинд запуска макросов

            keyboard.wait(Mouse_stop) # - бинд конца макросов
            os.system('cls')

            Function.func_color_text.text_color_red("___________________________"),print()
            Function.func_color_text.text_color_red("Макросы мыши деактивированы!")
            Function.func_color_text.text_color_red("___________________________")

            time.sleep(1)
            Comand_field = 'end'


        if Comand_field == 'settings': # - условие запуска настроек макросов (Ultra)

            os.system('cls')
            print()
            print("Введите желаймый режим:\n<< \'u1\' - ultra-1 (10 сек)\n<< \'u2\' - ultra hard-2 (20 сек) ") 
            Comand_field = input("Введите желаймый режим: ")

                        
            if Comand_field == 'u1':
                M_k_t = 300
                Mouse_Klick_time = M_k_t
                U_s = 'u1 (10 сек)'
                os.system('cls')

                                        
            if Comand_field == 'u2':
                M_k_t = 750
                Mouse_Klick_time = M_k_t
                U_s = 'u2 (20 сек)'
                os.system('cls')


            print()
            M_r = int(input("Введите значение задержки запуска в секундах: ")) 
            Mouse_response = M_r


            os.system('cls')
            print()
            print("настройки установлены!")
            time.sleep(2)
            os.system('cls')
            
                    

        if Comand_field =='info': # условие запуска информации об командах консоли
            i = 10
            while i != -1:
                time.sleep(1.3)
                os.system('cls')
                print()               
                print('_____________info(ultra)_____________')
                print("- Для запуска напишите: start")
                print("- Для настройки напишите: settings")
                print("- Для выхода напишите: end")
                print('_______________(',i,')_______________')
                i -= 1

    else:
        print("командная строка закрыта.")
        sys.exit()





    

    




    