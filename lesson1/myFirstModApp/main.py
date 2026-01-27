from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen


class ScrButton(Button): 
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal

    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mainhbox = BoxLayout(padding=8)
        mainlabel = Label(text='Выбери экран')
        vbox = BoxLayout(orientation='vertical', spacing=8)
        btnToScr1 = ScrButton(self, direction='right', goal='first', text="1")
        btnToScr2 = ScrButton(self, direction='right', goal='second', text="2")
        btnToScr3 = ScrButton(self, direction='right', goal='third', text="3")
        btnToScr4 = ScrButton(self, direction='right', goal='fourth', text="4")
        vbox.add_widget(btnToScr1)
        vbox.add_widget(btnToScr2)
        vbox.add_widget(btnToScr3)
        vbox.add_widget(btnToScr4)
        mainhbox.add_widget(mainlabel)
        mainhbox.add_widget(vbox)
        self.add_widget(mainhbox)

class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mainvbox = BoxLayout(orientation='vertical', size_hint = (.3, .5), pos_hint = {'center_x':.5, 'center_y':.5,})
        btnToScrReturn = ScrButton(self, direction='left', goal='main', text="Назад", pos_hint = {'center_x':1})
        anyButton = Button(text='Выбор 1', pos_hint = {'center_x':0}, )
        mainvbox.add_widget(anyButton)
        mainvbox.add_widget(btnToScrReturn)
        self.add_widget(mainvbox)

class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Виджеты
        mainvbox = BoxLayout(orientation='vertical', padding=8)
        hlineLabelTInput = BoxLayout(size_hint = (.85, .1), pos_hint = {'center_x':.5})
        hlineButtons = BoxLayout(size_hint = (.5, .3), pos_hint = {'center_x':.5})
        btnToScrReturn = ScrButton(self, direction='left', goal='main', text="Назад")
        anyButtonEvent = Button(text='OK!')
        self.infoLabel = Label(text = 'Выбор 2')
        passwordLabel = Label(text = 'Введите пароль:')
        self.enterTInput = TextInput(hint_text='Ваш пароль', multiline=False)
        # Размещение
        mainvbox.add_widget(self.infoLabel)
        hlineLabelTInput.add_widget(passwordLabel)
        hlineLabelTInput.add_widget(self.enterTInput)
        mainvbox.add_widget(hlineLabelTInput)
        hlineButtons.add_widget(anyButtonEvent)
        hlineButtons.add_widget(btnToScrReturn)
        mainvbox.add_widget(hlineButtons)
        self.add_widget(mainvbox)
        anyButtonEvent.on_press = self.change_text

    def on_enter(self):
        ''' on_enter - метод экрана, который будет вызван, как только экран будет создано
            после того, как интерфейс будет сформирован, можно устанавливать фокус,
            иначе ввод с клавиатуры будет заблокирован '''
        self.enterTInput.focus = True

    def change_text(self):
        self.infoLabel.text = f'Выбор 2 {self.enterTInput.text}'
        self.enterTInput.text = ''


class ThirdScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class FourthScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # загрузить большой объём текста
        with open('bigtext.txt', encoding='utf-8') as file:
            bigtext = file.read()
        # виджеты
        mainvbox = BoxLayout(orientation='vertical', padding=8)
        btnToScrReturn = ScrButton(self, direction='left', goal='main', text="Назад", size_hint=(1, .2))
        infoLabel = Label(text = 'Дополнительное задание', size_hint=(1, .2))
        self.veryBigText = Label(text = bigtext, size_hint_y=None, font_size = '25sp', halign='left', valign='top')
        self.scrollMyText = ScrollView(size_hint=(1, 1))
        # размещение и подписка на изменение размера texture (контейнер для текста на Label)
        self.scrollMyText.add_widget(self.veryBigText)
        self.veryBigText.bind(size=self.resizeBigText)
        mainvbox.add_widget(infoLabel)
        mainvbox.add_widget(btnToScrReturn)
        mainvbox.add_widget(self.scrollMyText)
        self.add_widget(mainvbox)

    def resizeBigText(self, *args):
        self.veryBigText.text_size = (self.veryBigText.width, None)
        self.veryBigText.texture_update()
        self.veryBigText.height = self.veryBigText.texture_size[1]
        

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