class Personas():

    def __init__(self, nombre, edad, DNI):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI

    def mostrarDatos(self):
        print(f'\nEl nombre de la persona es {self.nombre}, tiene {self.edad} años de edad y su DNI es {self.DNI}')

    def esMayorDeEdad(self):
        if self.edad >= 18:
            return True
        else:
            return False

print("----------------------------------------------------------------------------------")

nombre = input("\n¿Cuál es su primer nombre usuario? ")
print(f"\n¿Cuál es tu edad {nombre}? ")
edad = int(input())
DNI = input("\n¿Cuál es tu DNI usuario? ")

print("\n----------------------------------------------------------------------------------")

PersonaN = Personas(nombre, edad, DNI)
PersonaN.mostrarDatos()

print(f'\n{nombre} es mayor de edad: {PersonaN.esMayorDeEdad()}\n')

print("----------------------------------------------------------------------------------")