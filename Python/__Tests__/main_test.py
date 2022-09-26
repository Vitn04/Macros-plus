from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from random import randint

Window.size = (300,100) # - размер окна
Window.clearcolor = (255/255, 186/255, 3/255, 1) # - цвет окна в формате RGB
Window.title = "Macros++" # - Название окна 

class MyApp(App):

    def __init__(self):
        super().__init__()
        self.label = Label(text='Моя программа\nВсе работает!')

    def btn_pressed(self, *args):
        self.label.color = (randint(0,255)/255,randint(0,255)/255,randint(0,255)/255, 1)

    def build(self):
        box = BoxLayout()
        btn = Button(text='нажми на меня!')
        btn.bind(on_press=self.btn_pressed)   
        box.add_widget(self.label)
        box.add_widget(btn)
     
        return box
    
if __name__ == "__main__":
    MyApp().run()