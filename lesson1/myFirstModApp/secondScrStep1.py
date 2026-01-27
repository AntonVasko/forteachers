class SecondScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Виджеты
        mainvbox = BoxLayout(orientation='vertical')
        hlineLabelTInput = BoxLayout()
        hlineButtons = BoxLayout()
        btnToScrReturn = ScrButton(self, direction='left', goal='main', text="Назад")
        anyButtonEvent = Button(text='Выбор 1')
        self.infoLabel = Label(text = 'Выбор 2')
        passwordLabel = Label(text = 'Введите пароль:')
        self.enterTInput = TextInput()
        # Размещение
        mainvbox.add_widget(self.infoLabel)
        hlineLabelTInput.add_widget(passwordLabel)
        hlineLabelTInput.add_widget(self.enterTInput)
        mainvbox.add_widget(hlineLabelTInput)
        hlineButtons.add_widget(anyButtonEvent)
        hlineButtons.add_widget(btnToScrReturn)
        mainvbox.add_widget(hlineButtons)
        self.add_widget(mainvbox)