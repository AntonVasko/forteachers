from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty

KV = """
<MyWidget>:
    orientation: 'vertical'
    Label:
        text: f"Counter: {root.counter}"
    Button:
        text: "Нажми!"
        on_press: root.counter += 1
"""
class MyWidget(BoxLayout):
    counter = NumericProperty(0)

class MyApp(App):
    def build(self):
        Builder.load_string(KV)
        return MyWidget()
MyApp().run()
