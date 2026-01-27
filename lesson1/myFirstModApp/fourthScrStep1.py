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