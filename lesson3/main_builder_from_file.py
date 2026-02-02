from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

class MyWidget(Widget):
    title = StringProperty("Hello")

class MyApp(App):
    def build(self):
        Builder.load_file("any_ui.kv")
        return MyWidget()

MyApp().run()
