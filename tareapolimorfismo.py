class auto:
    def __init__(self, nombre): #init permite inicializar los valores del constructor
        self.nombre = nombre
    rueda = 4
    def desplazamiento(self):
        print("el auto se esta desplazando sobre 4 ruedas")

class moto:
    def __init__(self, nombre): #init permite inicializar los valores del constructor
        self.nombre = nombre
    rueda = 2
    def desplazamiento(self):
        print("el auto se esta desplazando sobre 2 ruedas")

auto1 = auto("RAV4")
auto1.desplazamiento()

moto1 = moto("Italika")
moto1.desplazamiento()