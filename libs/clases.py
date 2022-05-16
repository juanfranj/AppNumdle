from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp, sp
from kivy.clock import Clock
from collections import Counter


#from /libs.numdle import Numdle
intento = 0




class BotonRedondo(Button):
    global intento
    def __init__(self, **kwargs):

        super().__init__()
        self.widgets = kwargs["widgets"]
        #self.fila = kwargs["intento"]
        self.fila = intento
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
        #print(self.fila, intento)
        for i in range(len(self.widgets)):
            for j in range(len(self.widgets[i])):
                if id(self) == id(self.widgets[i][j]) and i == intento:#i == self.fila:
                    #print(id(self), id(self.widgets[i][j]))
                    self.limpiar_desactivar()
                    self.disabled = True

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
        self.solucion = kwargs["solucion"]
        self.teclado = kwargs["teclas"]
        self.errores = kwargs["errores"]
        self.mensaje = kwargs["mensaje"]
        #self.fila = kwargs["intento"]
        #self.fila = intento
        
        with self.canvas.before:
                self.btn_color = Color(rgba=(174/255, 214/255, 241/255, 1))
                self.rect = RoundedRectangle(radius=[8], size = self.size, pos = self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)  
        self.color = (23/255, 32/255, 42/255, 1)
        self.bold = True
        self.text = self.texto
        self.font_style = "H6"
        #self.font_size = "17sp"
        self.background_color = (0,0,0,0)
        self.background_normal = ""
        if self.texto == "Calcular" or self.texto == "Borrar":
            self.size_hint_x = None
            self.width = self.teclado[0].size[0] * .8
            #self.width = minimum_width
            
        if self.texto in ["+", "-", "*", "/", "="]:
            #self.font_size = "18sp"
            self.font_style = "H6"
        

    def on_press(self):
        if intento < 6:
            self.btn_color.rgba =  (46/255, 134/255, 193/255, 1)
            i, j = self.buscar_posicion()
            if self.text not in ["Calcular", "Borrar"]:
                self.widgets[i][j].text = self.text
                self.desactivar_siguiente(i, j)
            elif self.text == "Borrar":
                self.borrar(i, j)
            else:
                self.calcular_expersion()
    
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
        if intento < 6:
            self.widgets[i][j].text = ""
            self.desactivar_enterior(i, j)
    
    def desactivar_enterior(self, i , j):
        if j == 0:
            j_next = 7
        else:
            j_next = j - 1
        self.limpiar_desactivar()
        self.widgets[i][j_next].disabled = True
    
    def calcular_expersion(self):
        global intento
        solucion = self.solucion.split("=")
        digitos = Counter(self.solucion)

        if intento < 6:
            expresion_correcta = self.evaluar_expresion()
            if expresion_correcta:
                self.limpiar_desactivar()
                self.widgets[intento][0].disabled = True
            
        else:
            self.limpiar_desactivar()
            print("Maximo numero de intentos")
       
        
    def evaluar_expresion(self):
        try:
            global intento
            expresion = ""
            expresion_correcta = False
            for digito in self.widgets[intento][:]:
                expresion += digito.text
            digitos = Counter(expresion)
            if len(expresion) < 8:
                self.mensaje.text = f"Completa la expresion."
                self.errores.pos_hint = {'x':0.025, 'top': .99}
            elif digitos["="] == 0 or digitos["="] > 1:
                self.mensaje.text = (f"Dos iguales.")
                self.errores.pos_hint = {'x':0.025, 'top': .99}
            elif self.digitos_repetidos(expresion, digitos):
                self.mensaje.text = (f"Simbolo repetido.")
                self.errores.pos_hint = {'x':0.025, 'top': .99}
            
            else:
                ecuacion, solucion = expresion.split("=")[0], expresion.split("=")[1]
                sol_ec = eval(ecuacion)
                if solucion != str(sol_ec):
                    print("Solucion: ",solucion,"Solucion_calculada: " ,sol_ec)
                    self.mensaje.text = (f"Expresion mal calculada.")
                    self.errores.pos_hint = {'x':0.025, 'top': .99}
                else:
                    print("Ecuacion: ",ecuacion,"Solucion: " ,solucion)
                    print(f"{ecuacion} = {sol_ec} = {solucion}")
                    intento += 1
                    expresion_correcta = True
        except:
            self.mensaje.text = (f"Expresion no Evaluable.")
            self.errores.pos_hint = {'x':0.025, 'top': .99}
        Clock.schedule_once(self.quitar_error, 2)
        return expresion_correcta

    def quitar_error(self, dt):
        self.errores.pos_hint = {'x':0.025, 'top': 2}

    def digitos_repetidos(self, expresion, digitos):
        consec = False
        #print(consec, digitos, expresion)
        for clave, valor in digitos.items():
        
            if clave in ["+", "-", "*", "/", "="]:
                temp = list(expresion)
                #print(clave, valor)
                while valor > 0:
                    pos = temp.index(clave)
                    #print(temp, valor, pos)
                    del temp[pos]
                    #print(temp)
                    if temp[pos] in ["+", "-", "*", "/", "="]:
                        valor = 0
                        consec = True
                        break
                    else:
                        valor -= 1
                        
        #print(consec)
        return consec

                





            