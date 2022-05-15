from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp, sp


class BotonRedondo(Button):

    def __init__(self, **kwargs):

        super().__init__()
        self.widgets = kwargs["widgets"]
        self.fila = kwargs["intento"]
        with self.canvas.before:
                self.btn_color = Color(rgba=(151/255, 154/255, 154/255, 1))
                self.rect = RoundedRectangle(radius=[10], size = self.size, pos = self.pos)
                self.btn_color_2 = Color(rgba=(151/255, 154/255, 154/255, 1))
                self.rect_2 = RoundedRectangle(radius=[10], size = self.size, pos = self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect, disabled = self.desactivar)  
        self.color = (255/255, 255/255, 255/255, 1)
        self.bold = True
        self.font_size = "20sp"
        self.background_color = (0,0,0,0)
        self.background_normal = ""
        

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        self.rect_2.pos = (self.x + dp(2.5), self.y + dp(2.5))
        self.rect_2.size = (self.width - dp(5), self.height - dp(5))
    
    def on_press(self):
        for i in range(len(self.widgets)):
            for j in range(len(self.widgets[i])):
                if id(self) == id(self.widgets[i][j]) and i == self.fila:
                    #print(id(self), id(self.widgets[i][j]))
                    self.limpiar_desactivar()
                    self.disabled = True
    
    # def on_release(self):
    #     self.btn_color.rgba =  (151/255, 154/255, 154/255, 1) 

    def desactivar(self, *args):
        if self.disabled == True:
            self.btn_color.rgba =  (0/255, 0/255, 0/255, 1)
            self.disabled_color = (255/255, 255/255, 255/255, 1)
    
    def limpiar_desactivar(self):
        #print(self.widgets)
        for i in range(len(self.widgets)):
            for j in range(len(self.widgets[i])):
                #print(self.widgets[i][j].disabled)
                self.widgets[i][j].btn_color.rgba=(151/255, 154/255, 154/255, 1)
                self.widgets[i][j].disabled = False

    
class TecladoBotonRedondo(Button):

    def __init__(self, **kwargs):

        super().__init__()
        self.texto = kwargs["nombre"]
        self.widgets = kwargs["widgets"]
        with self.canvas.before:
                self.btn_color = Color(rgba=(174/255, 214/255, 241/255, 1))
                self.rect = RoundedRectangle(radius=[8], size = self.size, pos = self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)  
        self.color = (23/255, 32/255, 42/255, 1)
        self.bold = True
        self.text = self.texto
        self.font_size = "17sp"
        self.background_color = (0,0,0,0)
        self.background_normal = ""
        if self.texto == "Calcular" or self.texto == "Borrar":
            self.size_hint_x = None
            self.widht = self.width * 1.1
        if self.texto in ["+", "-", "*", "/", "="]:
            self.font_size = "20sp"

    def on_press(self):
        self.btn_color.rgba =  (46/255, 134/255, 193/255, 1)
        i, j = self.buscar_posicion()
        if self.text not in ["Calcular", "Borrar"]:
            self.widgets[i][j].text = self.text
            self.desactivar_siguiente(i, j)
        elif self.text == "Borrar":
            self.borrar(i, j)
    
    def on_release(self):
        self.btn_color.rgba =  (174/255, 214/255, 241/255, 1) 

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def buscar_posicion(self):
        pos_x, pos_y = None, None
        for i in range(len(self.widgets)):
            for j in range(len(self.widgets[i])):
                if self.widgets[i][j].disabled == True:
                    pos_x, pos_y = i, j
        return pos_x, pos_y
    
    def desactivar_siguiente(self, i , j):
        if j == 7:
            j_next = 0
        else:
            j_next = j + 1
        self.limpiar_desactivar()
        self.widgets[i][j_next].disabled = True

    def limpiar_desactivar(self):
        #print(self.widgets)
        for i in range(len(self.widgets)):
            for j in range(len(self.widgets[i])):
                #print(self.widgets[i][j].disabled)
                self.widgets[i][j].btn_color.rgba=(151/255, 154/255, 154/255, 1)
                self.widgets[i][j].disabled = False
    
    def borrar(self, i, j):
        self.widgets[i][j].text = ""
        self.desactivar_enterior(i, j)
    
    def desactivar_enterior(self, i , j):
        if j == 0:
            j_next = 7
        else:
            j_next = j - 1
        self.limpiar_desactivar()
        self.widgets[i][j_next].disabled = True

        