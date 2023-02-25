
lista = [5,5,6,9]

numero = 5
decimal = 65.4

print (type(numero))
print (type(decimal))
print (type(lista))

tipoTupla = (4, 5, 6, 7)# no se modifica durante la ejecucion.
print(tipoTupla)
print(type(tipoTupla))

tipolista = ["Cristobal", 23, "sagitario", 1.75]
print(f'el nombre del usuario es{tipolista[0]}, tiene {tipolista[1]} años, su signo es {tipolista[2]}')

del tipolista[2]
print(tipolista)

tipolista.append(input("escribe tu nuevo signo:"))
print(tipolista)

listaX = [154, 634, 777, 222, 23]