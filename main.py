from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder

from libs.numdle import Numdle

class AppNumdle(MDApp):
    def build(self):
        Window.size = (450, 720)
        self.title = "NumDle"
        return Builder.load_file("main.kv")

AppNumdle().run()