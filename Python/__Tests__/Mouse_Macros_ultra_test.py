
import sys
import mouse
from time import sleep, time
import os


i = 50

def Mouse_Macros_ultra_func():
      
    while True:
        if mouse.is_pressed(button='left'):
            while True:   
                sleep(0.01)
                mouse.double_click(button='left')
            
                if i == 40:
                    sys.exit()


def Macros_ultra_test():
    ss = 300   # - (ss = 1000 в sleep(0.1) - это 20 сек)
    while ss != 0:
        if ss !=0:
            sleep(0.01)
            mouse.double_click()
            ss -= 1
        
        if ss == 0:
            print("Конец ultra режима")
            break
        





while i != 0:
    sleep(0.5)
    print(i)
    i -= 1

    if i == 35:
       Macros_ultra_test()

else:
    sleep(5)


