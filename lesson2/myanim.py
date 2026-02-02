# Простая анимация виджета

from kivy.animation import Animation
from kivy.clock import Clock # это объект, а не класс
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App


class MyApp(App):
    def build(self):
        anim = Animation(x=10, duration=1) + Animation(y=150, duration=1) + Animation(y=50, duration=1)
        vbox = BoxLayout(orientation='vertical')
        self.animButton = Button(text='Анимация', background_color=(0, 1, 0, .5))
        vbox.add_widget(self.animButton)
        anim.on_progress = self.change
        anim.start(self.animButton)
        return vbox
    
    def change(self, *args):
        print(f'\nВыполняется анимация')


MyApp().run()

'''
anim = Animation(x=10, duration=1) + Animation(y=150, duration=1) # выполнение друг за другом
anim.on_start = self.change # выполнение метода change при старте анимации  
anim.on_complete = self.change # выполнение метода change после остановки анимации
anim.on_progress = self.change # выполнение метода change в процессе работы анимации (при кадом шаге)
anim.start(widget) # старт анимации

def change(self, *args):
	print(f'\nВыполняется анимация')
'''
