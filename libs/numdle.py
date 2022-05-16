from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
#from kivy.graphics import Color, RoundedRectangle
from kivymd.app import MDApp


from libs.clases import BotonRedondo, TecladoBotonRedondo


class Numdle(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()
        self.celdas =[[None for j in range(0,8)] for i in range(0,6)]
        self.panel_teclado = [] 
        self.intento = 0
        self.solucion = "98-19=79"

    def on_kv_post(self, base_widget):
        self.grid = self.ids["grid"]
        self.teclas = self.ids["teclado"]
        self.simbolos = self.ids["simbolos"]
        self.errores = self.ids["error"]
        self.mensaje = self.ids["mensaje"]
        simbolos = {"sumar": "+", "restar":"-",
                    "multiplicar" : "*", "dividir":"/", "igual": "=",
                    "calcular": "Calcular", "Borrar": "Borrar"
                    }
        for i in range(0,6):
            for j in range(0,8):
                self.boton= BotonRedondo(widgets = self.celdas, intento = self.intento)
                self.grid.add_widget(self.boton)
                self.celdas[i][j] = self.boton
                if i == 0 and j == 0:
                    self.boton.disabled = True

        for celda in range(0,10):
            self.teclado = TecladoBotonRedondo(nombre = str(celda), widgets = self.celdas, teclas = self.panel_teclado, solucion = self.solucion,
                                                 intento = self.intento, errores = self.errores, mensaje = self.mensaje)
            self.panel_teclado.append(self.teclado)
            self.teclas.add_widget(self.teclado)

        for clave, valor in simbolos.items():
            self.teclado = TecladoBotonRedondo(nombre = valor, widgets = self.celdas, teclas = self.panel_teclado, solucion = self.solucion,
                                                 intento = self.intento, errores = self.errores, mensaje = self.mensaje)
            self.panel_teclado.append(self.teclado)
            self.simbolos.add_widget(self.teclado)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size   

    def on_pre_enter(self, *args):
        self.app.title = "numdle."
    
    
        
        
