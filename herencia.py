class cazador:
    
    def __init__(self, nombre, espada): #init permite inicializar los valores del constructor
        self.nombre = nombre
        self.espada = espada

     #metodos
    def presentar(self):
        print(f'mi nombre es {self.nombre} y mi espada es {self.espada}')

class pilar(cazador):
    def __init__(self, nombre, espada, respiracion, postura):
        super().__init__(nombre, espada)
        self.respiracion = respiracion
        self.postura = postura
    def presentarpilar(self):
        print(f'mi nombre es {self.nombre} y mi espada es {self.espada}, mi respiracion respiracion de {self.respiracion}, y tengo {self.postura} posturas')

cazador1 = cazador("Tejiro", "Espada negra")
cazador1.presentar()
print("-------------------------------")
ragoku = pilar("ragoku", "color roja", "llama", 8)
ragoku.presentarpilar()
ragoku.presentar()
   