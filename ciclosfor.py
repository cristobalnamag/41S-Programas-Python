import turtle
turtle. shape('turtle')


#for i in range(limite inferior, limite superior, incremento):
figuras= int(input("ESCRIBE EL NUMERO DE FIGURAS QUE QUIERAS: "))
lados = int(input("ESCRIBE EL NÚMERO DE LADOS DE LA FIGURA QUE QUIERES: "))
longitud = int(input("ESCRIBE EL NÚMERO DE LONGITUD DE CADA LADO: "))
for j in range(0,figuras):
    turtle.fillcolor("orange")
    turtle.begin_fill()
    for i in range(0,lados):
       turtle.forward (longitud)
       turtle. left(360/lados)
    turtle.forward(longitud)
    turtle.right(360/figuras)
    turtle.end_fill()
   

turtle.exitonclick()