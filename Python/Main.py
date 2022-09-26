# Скрипт обьединения и запуска единой программы Macros+ (main)


import Function


def Start_console(): # функция запуска начальной консоли

    import Mouse_Macros as Macros_low
    import Mouse_Macros_ultra as Macros_ultra
    import Function as __privat__
    import os
    import sys
    

    Main_fild_check = 1

    while Main_fild_check != 0: 
        if Main_fild_check != 0:
            os.system("cls")
            print()
            print("_____________________________Macros+(Menu)__________________________"),print("")
            print("            Добро пожаловать в консольную программу Macros+"),print()
            print("   Выберите желаймый режим макросов:")
            Function.func_color_text.text_color_yellow("<< Напишите \'Macros\' или \'1\' для запуска стандартных Макросов.")
            Function.func_color_text.text_color_yellow("<< Напишите \'Macros_ultra\' или \'2\' для запуска Макрос-ultra.")
            print("____________________________________________________________________")
            print("Версия программы:", __privat__.Privat_variables.__ProgVersion__),print()


            Main_fild = input("<<User_1 ввод: ")

            if Main_fild == 'Macros' or Main_fild == '1':
                Macros_low.Main_Macros_Mouse()

            if Main_fild == 'Macros_ultra' or Main_fild == '2':
                Macros_ultra.Main_Macros_Mouse_ultra()
                
            if Main_fild == 'end':
                sys.exit()



if __name__ == '__main__':
    Function.func_size_console.Setting_size()
    Function.func_name_console.Name_console()
    Start_console()
    


            




