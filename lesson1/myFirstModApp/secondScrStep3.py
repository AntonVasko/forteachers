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
        # переопределение метода on_press (нажатие на кнопку) методом change_text
        anyButtonEvent.on_press = self.change_text
        
    # обработчики
    def on_enter(self):
        ''' on_enter - метод экрана, который будет вызван, как только экран будет создано
            после того, как интерфейс будет сформирован, можно устанавливать фокус,
            иначе ввод с клавиатуры будет заблокирован '''
        self.enterTInput.focus = True

    def change_text(self):
        self.infoLabel.text = f'Выбор 2 {self.enterTInput.text}'
        self.enterTInput.text = ''
