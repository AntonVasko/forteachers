class FirstScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        mainvbox = BoxLayout(orientation='vertical', size_hint = (.3, .5), pos_hint = {'center_x':.5, 'center_y':.5,})
        btnToScrReturn = ScrButton(self, direction='left', goal='main', text="Назад")
        anyButton = Button(text='Выбор 1')
        mainvbox.add_widget(anyButton)
        mainvbox.add_widget(btnToScrReturn)
        self.add_widget(mainvbox)
        