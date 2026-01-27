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
        