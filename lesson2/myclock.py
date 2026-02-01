# таймер
from kivy.clock import Clock # это объект, а не класс
from kivy.uix.label import Label
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.app import App

class MyClock(Label):

    total_tic = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # вызывает метод todo каждые 0.5 секунд
        Clock.schedule_interval(self.todo_interval, 0.5)

        # вызывает метод todo один раз через 5 секунд
        Clock.schedule_once(self.todo_once5sec, 5)

        # вызывает метод todo при следующем обновлении экрана
        Clock.schedule_once(self.todo_once1sec)

        self.my_clock = Clock.schedule_interval(self.mycallback_interval, 2)

        self.total_interval = 0

    def todo_interval(self, dt):
        # Ваш код
        ...
        return False  # Остановка таймера
    
    def todo_once5sec(self, dt):
        # Ваш код
        ...
        return False  # Остановка таймера
    
    def todo_once1sec(self, dt):
        # Ваш код
        ...
        return False  # Остановка таймера
    
    def mycallback_interval(self, *args):
        self.total_tic += 1
        self.total_interval += args[0]
        self.text = str(self.total_tic)
        if self.total_tic >= 5:
            self.my_clock.cancel()
            self.text += f'\nТаймер завершил свою работу через {self.total_interval} секунд.\nПерезапустить?'

class MyApp(App):
    def build(self):
        vbox = BoxLayout(orientation='vertical')
        self.myClock = MyClock()
        self.myButton = Button(text='Перезапуск')
        self.myButton.bind(on_press=self.restart)
        vbox.add_widget(self.myClock)
        vbox.add_widget(self.myButton)
        return vbox
    
    def restart(self, *args):
        if self.myClock.total_tic >= 5:
            self.myClock.total_tic = 0
            self.myClock.total_interval = 0
            self.myClock.my_clock()
    
MyApp().run()
