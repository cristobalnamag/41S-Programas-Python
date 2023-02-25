class persona:
    
    def __init__(self, nombre, apellido): #init permite inicializar los valores del constructor
        self.nombre = nombre
        self.apellido = apellido

     #metodos
    def presentar(self):
        print(f'mi nombre es {self.nombre} y mi apellido es {self.apellido}')


class maestro(persona):
    def __init__(self, nombre, apellido, carrera, edad):
        super().__init__(nombre, apellido)
        self.carrera = carrera
        self.edad = edad
    def presentarmaestro(self):
        print(f'mi nombre es {self.nombre} y mi apellido es {self.apellido}, mi carrera es {self.carrera}, y mi edad es {self.edad} años')


class alumno(maestro):
    def __init__(self, nombre, apellido, carrera, edad, semestre, sexo, turno, matricula):
        super().__init__(nombre, apellido, carrera, edad )
        self.semestre = semestre
        self.sexo = sexo
        self.turno = turno
        self.matricula = matricula
    def presentaralumno(self):
        print(f'mi nombre es {self.nombre} y mi apellido es {self.apellido}, mi carrera es {self.carrera}, mi edad es {self.edad} años, voy en {self.semestre} semestre, mi sexo es {self.sexo}, mi turno es {self.turno} y mi matricula es {self.matricula}')



persona1 = persona("Cristobal", "Nava")
persona1.presentar()
print("-------------------------------")
maestro1 = maestro("Cristobal", "Nava", "Ing. electronica", 23)
maestro1.presentarmaestro()
print("-------------------------------")
alumno1 = alumno("Cristobal", "Nava", "Ing. electronica", 23, "4to", "masculino", "matutino", "18560036")
alumno1.presentaralumno()
