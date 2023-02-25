
respuesta = "si"
calificacionesAlumnos = []

while respuesta == "si":
    calificacionesAlumnos.append(int(input("Escribe las calificaciones del siguiente alumno: ")))

    respuesta = input("Escribe si para seguir añadiendo calificaciones ")

print(calificacionesAlumnos)
promedio = sum(calificacionesAlumnos)/len(calificacionesAlumnos)
print(promedio)
