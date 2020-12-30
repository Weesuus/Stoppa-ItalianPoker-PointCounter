from kivymd.app import MDApp
from kivy.lang import Builder

global contoFinale
global nowCard

KV = """
Screen:
    
    GridLayout:
        id:primo
        rows:2
        cols:5
        MDIconButton:
            id:uno
            icon: "Graphic/assoIcon.png"
            on_press: app.one()
        MDIconButton:
            id:due
            icon: "Graphic/twoIcon.png"
            on_press: app.two()
        MDIconButton:
            id:tre
            icon: "Graphic/threeIcon.png"
            on_press: app.three()
        MDIconButton:
            id:quattro
            icon: "Graphic/fourIcon.png"
            on_press: app.four()
        MDIconButton:
            id:cinque
            icon: "Graphic/fiveIcon.png"
            on_press: app.five()
        MDIconButton:
            id:sei
            icon: "Graphic/sixIcon.png"
            on_press: app.six()
        MDIconButton:
            id:sette
            icon: "Graphic/sevenIcon.png"
            on_press: app.seven()
        MDIconButton:
            id:otto
            icon: "Graphic/fanteIcon.png"
            on_press: app.eight()
        MDIconButton:
            id:nove
            icon: "Graphic/horseIcon.png"
            on_press: app.nine()
        MDIconButton:
            id:dieci
            icon: "Graphic/kingIcon.png"
            on_press: app.ten()
    GridLayout:
        adaptive_size: True
        rows:1
        cols:2
        MDLabel:
            text: "Risultato:"
        MDLabel:
            id:conto
            text:"0"
    BoxLayout:
        id:secondo
        rows:2
        cols:3
        MDIconButton:
            id:cardZero
            icon: "Graphic/sampleIcon.png"
        MDIconButton:
            id:cardOne
            icon: "Graphic/sampleIcon.png"
        MDIconButton:
            id:cardTwo
            icon: "Graphic/sampleIcon.png"
        MDRaisedButton:
            text: "PULISCI"
            on_press: app.clear()
"""

contoFinale = 0
nowCard = 0
insertedCard = [0, 0, 0]


class Stoppa(MDApp):

    def build(self):
        self.title = "Stoppa"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Gray"
        self.theme_cls.primary_hue = "400"
        return Builder.load_string(KV)

    def one(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 1:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 16
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(1)

    def two(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 2:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 12
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(2)

    def three(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 3:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 13
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(3)

    def four(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 4:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 14
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(4)

    def five(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 5:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 15
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(1)

    def six(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 6:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 18
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(6)

    def seven(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 7:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 21
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(7)

    def addCard(self, num):
        icn = ""
        global nowCard, insertedCard
        if num == 1:
            icn = 'Graphic/assoIcon.png'
        elif num == 2:
            icn = "Graphic/twoIcon.png"
        elif num == 3:
            icn = "Graphic/threeIcon.png"
        elif num == 4:
            icn = "Graphic/fourIcon.png"
        elif num == 5:
            icn = "Graphic/fiveIcon.png"
        elif num == 6:
            icn = "Graphic/sixIcon.png"
        elif num == 7:
            icn = "Graphic/sevenIcon.png"
        elif num == 8:
            icn = "Graphic/fanteIcon.png"
        elif num == 9:
            icn = "Graphic/horseIcon.png"
        elif num == 10:
            icn = "Graphic/kingIcon.png"
        if nowCard == 0:
            self.root.ids['cardZero'].icon = icn
        elif nowCard == 1:
            self.root.ids['cardOne'].icon = icn
        elif nowCard == 2:
            self.root.ids['cardTwo'].icon = icn
        insertedCard[nowCard] = num
        nowCard += 1

    def eight(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 8:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 10
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(8)

    def nine(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 9:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 10
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(9)

    def ten(self):
        global contoFinale, nowCard, insertedCard
        for i in insertedCard:
            if i == 10:
                return 0
        if nowCard > 2:
            return 0
        contoFinale += 10
        self.root.ids["conto"].text = str(contoFinale)
        self.addCard(10)

    def clear(self):
        global contoFinale, nowCard, insertedCard
        contoFinale = 0
        self.root.ids["conto"].text = str(contoFinale)
        self.root.ids['cardZero'].icon = 'Graphic/sampleIcon.png'
        self.root.ids['cardOne'].icon = 'Graphic/sampleIcon.png'
        self.root.ids['cardTwo'].icon = 'Graphic/sampleIcon.png'
        nowCard = 0
        insertedCard = [0, 0, 0]


Stoppa().run()
