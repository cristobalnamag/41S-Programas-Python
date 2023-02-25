import turtle
turtle.shape("turtle")

programa = input("Escribe si para graficar y no para terminar ")

while programa == "si":
    lados = int(input("escribe el numero de lados de la figura"))
    longitud = int(input("longuitud de lado:"))

    if lados == 0:
        print("opcion invalida")

    else:
        grados = 360/lados
        for i in range(0, lados):
            turtle.forward(longitud)
            turtle.right(grados)

    programa = input("escribe si para graficar y no para terminar")
print("programa termino")


turtle.exitonclick()