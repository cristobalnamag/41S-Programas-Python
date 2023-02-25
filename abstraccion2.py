#Abstracción definir las caracteristicas y los metodos, como y que va a hacer nuestro objeto
class Pilares:
    #Propiedades/Atributos
    #funcion constructor con variables internas -> es el bloque para asignar las propiedades el objeto
    def __init__(self, nombre, espada, respiracion, posturas, nivelPoder): #init permite inicializar los valores del constructor
        self.nombre = nombre
        self.espada = espada
        self.respiracion = respiracion
        self.posturas = posturas
        self.nivelPoder = nivelPoder
        self.tipo = "humano"
   
    #metodos
    def ataque(self):
        print("Ataque")

    def defensa(self):
        print("Defensa")

class Aprendiz(Pilares):
    pass

#pilares
himejima = Pilares("Himejima", "bolas picos","Respiracion de la Roca", 5, 100)
rengoku = Pilares("Rengoku", "katana rojo carmesi","Respiracion de llama", 9, 70)

#lunas
lunasuperior1 = Pilares("kokushibo", "katana lunar", "respiracion lunar", 9, 120)
lunasuperior1.tipo = "Demonio"

#Aprendiz
aprendiz1 = Aprendiz("Pips", "katana", "normal", 8, 10)


print(f'El personaje {himejima.nombre}, su arma es {himejima.espada}, su respiracion es {himejima.respiracion},tiene {himejima.posturas} posturas, y tiene {himejima.nivelPoder} de nivel de poder') #Alt + z para ajustar

print("-------------------------------")

print(f'El personaje {rengoku.nombre}, su arma es {rengoku.espada}, su respiracion es {rengoku.respiracion}, tiene {rengoku.posturas} posturas, y tiene {rengoku.nivelPoder} de nivel de poder')

print("-------------------------------")

print(f'El personaje {lunasuperior1.nombre}, su arma es {lunasuperior1.espada}, su respiracion es {lunasuperior1.respiracion}, tiene {lunasuperior1.posturas} posturas, tiene {lunasuperior1.nivelPoder} de nivel de poder y es {lunasuperior1.tipo}')

print(f'El personaje {aprendiz1.nombre}, su arma es {aprendiz1.espada}, su respiracion es {aprendiz1.respiracion}, tiene {aprendiz1.posturas} posturas, tiene {aprendiz1.nivelPoder} de nivel de poder y es {aprendiz1.tipo}')

