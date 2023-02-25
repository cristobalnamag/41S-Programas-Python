#Abstracción definir las caracteristicas y los metodos, como y que va a hacer nuestro objeto
class Pilares:
    #Propiedades/Atributos
    nombre = " "
    postura = " "
    edad = 18
    espada = "normal"
    estatura = 1.6
    respiracion = "normal"
   
    #metodos
    def ataque(self):
        print("Ataque")

    def defensa(self):
        print("Defensa")

#Se crea el objeto a partir de la clase
personajeMisumoto = Pilares()
personajeMisumoto.nombre = "Pips"

personajesuguko = Pilares()
personajesuguko.nombre = "kanao"



#se llama a los personajes o atributos
print(f'El personaje {personajeMisumoto.nombre}, tiene {personajeMisumoto.edad} años y su respiracion es {personajeMisumoto.respiracion}')

print(f'El personaje {personajesuguko.nombre}, tiene {personajesuguko.edad} años y su respiracion es {personajesuguko.respiracion}')

kibutzuji =input("Esta cerca el enemigo? ")

if kibutzuji == "si":
    personajeMisumoto.ataque()

else:
    personajeMisumoto.defensa()


