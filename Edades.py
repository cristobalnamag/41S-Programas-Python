class Persona():
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def set_edad(self, edad):
        self.edad = edad

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def mostrar_persona(self):
        print(f"El nombre de la persona es {self.nombre} y tiene {self.edad} años\n")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        else:
            return False 

    def es_mayor_que(self, PersonaX):
        if self.edad > PersonaX.get_edad():
            return True
        else:
            return False

Persona1 = Persona("Johan", 19)
Persona2 = Persona("Luis", 21)

print("----------------------------------------------------------------------------------\n")

Persona1.mostrar_persona()
Persona2.mostrar_persona()

print("----------------------------------------------------------------------------------")

print(f"\n{Persona1.get_nombre()} es mayor de edad: {Persona1.es_mayor_de_edad()}")
print(f"\n{Persona2.get_nombre()} es mayor de edad: {Persona2.es_mayor_de_edad()}\n")

print("----------------------------------------------------------------------------------")

print(f"\n¿{Persona1.get_nombre()} es mayor que {Persona2.get_nombre()}?: {Persona1.es_mayor_que(Persona2)}")
print(f"\n¿{Persona2.get_nombre()} es mayor que {Persona1.get_nombre()}?: {Persona2.es_mayor_que(Persona1)}\n")

print("----------------------------------------------------------------------------------")