from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class ScrButton(Button): 
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)

    def on_press(self):
        pass

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name='main'))
        sm.add_widget(FirstScr(name='first'))
        sm.add_widget(SecondScr(name='second'))
        sm.add_widget(ThirdScr(name='third'))
        sm.add_widget(FourthScr(name='fourth'))
        return sm

app = MyApp()
app.run()