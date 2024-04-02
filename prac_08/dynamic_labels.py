from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

NAMES = ['Lindsay', 'Nathan', 'Ellie', ]


class LabelDemo(App):
    """Dynamic Lable program"""
    status_text = StringProperty()

    def build(self):
        self.title = ""
        self.root = Builder.load_file('dynamic_label.kv')
        return self.root


# create and start the App running
LabelDemo().run()
