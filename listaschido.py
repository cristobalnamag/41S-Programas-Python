
respuesta = "si"
lista = []

while respuesta == "si":
    calificacion = int(input("Ingresa la calificacion del alumno: "))
    lista.append(calificacion)

    respuesta = input("Presiona si para seguir agregando calificaciones: ")


print(lista)

promedio = sum(lista)/len(lista)
print(f'El promedio general del grupo es {promedio}')