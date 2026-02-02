from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

class RootWidget(BoxLayout):
    counter = NumericProperty(0)

class MyApp(App):
    pass

if __name__ == "__main__":
    MyApp().run()
