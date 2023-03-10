#MAQUINA DESPENDEDORA QUE CREA BEBIDAS

class Bebidas(): #clase madre
    
    def __init__(self, nombre, tamaño):
        self.nombre = nombre
        self.tamaño = tamaño

    def set_tamaño(self, tamaño):
        self.tamaño = tamaño

    def get_tamaño(self):
        return self.tamaño
    
class Refrescos(Bebidas): #clase hijo1
    def __init__(self, nombre, tamaño, temperatura, etiquetado):
        super().__init__(nombre, tamaño)
        self.temperatura = temperatura
        self.__etiquetado = etiquetado

    def mostrarDatosRefresco(self):
        print(f'nombre: {self.nombre}, tamaño: {self.tamaño} ml, frio: {self.temperatura}')

    def calcularPrecio(self, otrotamaño):

        if opcion2 == "UNO":   
            precioR = (self.tamaño)* 0.03
            return precioR
        
        else:
            precioR = (self.tamaño  + otrotamaño.get_tamaño()) * 0.03
            return precioR

class Jugos(Bebidas): #clase hijo2
    def __init__(self, nombre, tamaño, sabor, temperatura, natural, etiquetado):
        super().__init__(nombre, tamaño)
        self.sabor = sabor
        self.temperatura = temperatura
        self.natural = natural
        self.__etiquetado = etiquetado

    def mostrarDatosJugo(self):
        print(f'nombre: {self.nombre}, tamaño: {self.tamaño} ml, sabor: {self.sabor}, frio: {self.temperatura}, natural: {self.natural}')

    def calcularPrecio(self, otrotamaño):
            
        if opcion2 == "UNO":
            precioJ = self.tamaño * 0.025
            return precioJ
        
        else:
            precioJ = (self.tamaño + otrotamaño.get_tamaño())*0.028
            return precioJ

print("----------------------------------------------------------------------------------\n")

print('''
    Bebidas disponibles en la maquina

        REFRESCOS                   JUGOS      ----    Sabores de Jugos -------- Tamaños para ambos
        Coca                        Delvalle           Mango                     600 ml
        Sprite                      Jumex              Uva                       500 ml
        Pepsi                       Aquafruit          Naranja                   
        Fanta(solo hay naranja)                        Manzana        
        Sangría                                        Durazno
    ''')


print("¿Qué le gustaría comprar usuario? REFRESCO o JUGO")
opcion1 = input()

if opcion1 == "REFRESCO":

    print("\n----------------------------------------------------------------------------------\n")

    print("¿Quieres UNO o DOS refrescos?")
    opcion2 = input()

    print("\n----------------------------------------------------------------------------------\n")

    if opcion2 == "UNO":
        print("Nombre del refresco: ")
        nombre = input()
        print("Tamaño del refresco en ml: ")
        tamaño = int(input())
        print("¿Frío?")
        temperatura = input()

        print("\n----------------------------------------------------------------------------------\n")

        R = Refrescos(nombre, tamaño, temperatura, 56238545)

        print("DATOS DEL REFRESCO:\n")
        R.mostrarDatosRefresco()
        print("El precio del refresco es: ", R.calcularPrecio(0), "pesos")

        print("\n----------------------------------------------------------------------------------")
    
    if opcion2 == "DOS":
        print("Nombre del primer refresco: ")
        nombre1 = input()
        print("Tamaño del primer refresco en ml: ")
        tamaño1 = int(input())
        print("¿Frío?")
        temperatura1 = input()

        print("\n----------------------------------------------------------------------------------\n")

        print("Nombre del segundo refresco: ")
        nombre2 = input()
        print("Tamaño del segundo refresco en ml: ")
        tamaño2 = int(input())
        print("¿Frío?")
        temperatura2 = input()

        print("\n----------------------------------------------------------------------------------\n")

        R1 = Refrescos(nombre1, tamaño1, temperatura1, 56238545)
        R2 = Refrescos(nombre2, tamaño2, temperatura2, 56238545)

        print("DATOS DE LOS REFRESCOS:\n")
        R1.mostrarDatosRefresco()
        R2.mostrarDatosRefresco()
        print(f'El precio de ambos refrescos es: {R1.calcularPrecio(R2)} pesos')

        print("\n----------------------------------------------------------------------------------")

if opcion1 == "JUGO":

    print("\n----------------------------------------------------------------------------------\n")

    print("¿Quieres UNO o DOS jugos?")
    opcion2 = input()

    print("\n----------------------------------------------------------------------------------\n")

    if opcion2 == "UNO":
        print("Nombre del jugo: ")
        nombre = input()
        print("Tamaño del jugo en ml: ")
        tamaño = int(input())
        print("Sabor del jugo:")
        sabor = input()
        print("¿Frío?")
        temperatura = input()
        print("¿Natural?")
        natural = input()

        print("\n----------------------------------------------------------------------------------\n")

        J = Jugos(nombre, tamaño, sabor, temperatura, natural, 45265235)

        print("DATOS DEL JUGO:\n")
        J.mostrarDatosJugo()
        print("El precio del jugo es: ", J.calcularPrecio(0))

        print("\n----------------------------------------------------------------------------------")

    if opcion2 == "DOS":
        print("Nombre del primer jugo: ")
        nombre1 = input()
        print("Tamaño del primer jugo en ml: ")
        tamaño1 = int(input())
        print("Sabor del primer jugo:")
        sabor1 = input()
        print("¿Frío?")
        temperatura1 = input()
        print("¿Natural?")
        natural1 = input()

        print("\n----------------------------------------------------------------------------------\n")

        print("Nombre del primer jugo: ")
        nombre2 = input()
        print("Tamaño del primer jugo en ml: ")
        tamaño2 = int(input())
        print("Sabor del primer jugo:")
        sabor2 = input()
        print("¿Frío?")
        temperatura2 = input()
        print("¿Natural?")
        natural2 = input()

        print("\n----------------------------------------------------------------------------------\n")

        J1 = Jugos(nombre1, tamaño1, sabor1, temperatura1, natural1, 45265235)
        J2 = Jugos(nombre2, tamaño2, sabor2, temperatura2, natural2, 45265235)

        print("DATOS DE LOS JUGOS:\n")
        J1.mostrarDatosJugo()
        J2.mostrarDatosJugo()
        print(f'El precio de ambos jugos es: {J1.calcularPrecio(J2)} pesos')

        print("\n----------------------------------------------------------------------------------")