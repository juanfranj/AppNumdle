from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle



class BotonRedondo(Button):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
        with self.canvas.before:
                self.btn_color = Color(rgba=(151/255, 154/255, 154/255, 1))
                self.rect = RoundedRectangle(radius=[8], size = self.size, pos = self.pos)
                self.btn_color_2 = Color(rgba=(151/255, 154/255, 154/255, 1))
                self.rect_2 = RoundedRectangle(radius=[8], size = self.size, pos = self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect, disabled = self.desactivar)  
        #self.size_hint = (.62, .62)
        self.background_color = (0,0,0,0)
        self.background_normal = ""
        

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.rect_2.pos = (self.x + 2.5, self.y + 2.5)
        self.rect_2.size = (self.width - (5), self.height - 5)
    
    def on_press(self):
        self.btn_color.rgba =  (174/255, 214/255, 241/255, 1)
    
    def on_release(self):
        self.btn_color.rgba =  (151/255, 154/255, 154/255, 1) 

    def desactivar(self, *args):
        if self.disabled == True:
            self.btn_color.rgba =  (23/255, 32/255, 42/255, 1)

    
    
    



class TecladoBotonRedondo(Button):

    def __init__(self, **kwargs):

        super().__init__()
        self.texto = kwargs["nombre"]
        with self.canvas.before:
                self.btn_color = Color(rgba=(174/255, 214/255, 241/255, 1))
                self.rect = RoundedRectangle(radius=[8], size = self.size, pos = self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)  
        
        self.color = (23/255, 32/255, 42/255, 1)
        self.bold = True
        self.text = self.texto
        self.background_color = (0,0,0,0)
        self.background_normal = ""
        #self.background_down = ""
        #self.on_press = root.pulsar_boton
    
    def on_press(self):
        self.btn_color.rgba =  (46/255, 134/255, 193/255, 1)
    
    def on_release(self):
        self.btn_color.rgba =  (174/255, 214/255, 241/255, 1) 

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size  