from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

class MyFirstWidget(Widget):
    pass


class IdExamplesApp(App):
    def build(self):
        return MyFirstWidget()

if __name__ == "__main__":
    IdExamplesApp().run()
