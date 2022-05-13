from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle



class BotonRedondo(Button):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        with self.canvas.before:
                Color(rgba=(151/255, 154/255, 154/255, 1))
                self.rect = RoundedRectangle(radius=[8], size = self.size, pos = self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)  
        #self.size_hint = (.62, .62)
        self.background_color = (0,0,0,0)
        self.background_normal = ""
        self.background_down = ""

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class TecladoBotonRedondo(Button):

    def __init__(self, **kwargs):

        super().__init__()
        self.texto = kwargs["nombre"]
        with self.canvas.before:
                Color(rgba=(174/255, 214/255, 241/255, 1))
                self.rect = RoundedRectangle(radius=[8], size = self.size, pos = self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)  
        
        self.color = (23/255, 32/255, 42/255, 1)
        self.bold = True
        self.text = self.texto
        self.background_color = (0,0,0,0)
        self.background_normal = ""
        self.background_down = ""
        #self.on_press = root.pulsar_boton

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size  