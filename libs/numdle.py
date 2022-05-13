from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivymd.app import MDApp


from libs.clases import BotonRedondo, TecladoBotonRedondo

class Numdle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.celdas = []

    def on_kv_post(self, base_widget):
        self.grid = self.ids["grid"]
        self.teclas = self.ids["teclado"]
        teclado_digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 
        for celda in range(0,48):
            if celda < 10:
                self.teclado = TecladoBotonRedondo(nombre = str(celda))
                self.teclas.add_widget(self.teclado)

            self.boton= BotonRedondo()
            self.grid.add_widget(self.boton)
            self.celdas.append(self.boton)


    def pulsar_boton(self):
        pass
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size   

    def on_pre_enter(self, *args):
        self.app.title = "Numdle"
