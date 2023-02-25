'''
def NombreFuncion(par1, par2):
    Codigo
    suma = par1 + par2
    pass
'''

def suma(numeroA, numeroB, numeroC):
    resultado = numeroA + numeroB 

    return resultado

def resta(numeroA, numeroB, numeroC):

    return numeroA - numeroB - numeroC


numeroA = int(input("Ingresa el 1er numero: "))
numeroB = int(input("Ingresa el 2do numero: "))
numeroC = int(input("Ingresa el 3er numero: "))



print(suma(numeroA, numeroB, numeroC))
print(resta(numeroA, numeroB, numeroC))
