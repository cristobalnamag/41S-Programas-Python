from tkinter import *
from tkinter import messagebox as MessageBox

ventana= Tk()
ventana.title('CAMBIAR COLOR DEL FONDO DE VENTANA')
ventana.iconbitmap('colores.ico') 
ventana.geometry('450x350')
ventana.resizable(0,0)
ventana.config(bg= 'black')

def hexacolor():
    global x_red, x_green, x_blue, color_total

    x_red   = str(hexared.get()) 
    resultadored = Numposiciones(x_red)
    digitosred = resultadored[0] + resultadored[1]
    if digitosred == 2:
        pass
    else:
        borrardatos()
        error()

    x_green = str(hexagreen.get()) 
    resultadogreen = Numposiciones(x_green)
    digitosgreen = resultadogreen[0] + resultadogreen[1]
    if digitosgreen == 2:
        pass
    else:
        borrardatos()
        error()

    x_blue  = str(hexablue.get()) 
    resultadoblue = Numposiciones(x_blue)
    digitosblue = resultadoblue[0] + resultadoblue[1]
    if digitosblue == 2:
        pass
    else:
        borrardatos()
        error()

    digitos_total = digitosblue + digitosgreen + digitosred
    if digitos_total ==6:
        solo0_9_A_F()

        if count == 6:
            color_total = str("#"+x_red + x_green + x_blue)
            #color_totalnuevo = color_total
            ventana.config(bg=color_total)
            titulohexacolor.config(text=color_total)
            titulocambiocolor.config(bg=color_total)
            titulored.config(bg=color_total)
            titulogreen.config(bg=color_total)
            tituloblue.config(bg=color_total)
            borrardatos()
        else:
            borrardatos()
            error()
    else:
        borrardatos()
    

def error():
    MessageBox.showerror("Error", "Ingresa un color válido")

def borrardatos():
    texto_red.delete(0, END)
    texto_green.delete(0, END)
    texto_blue.delete(0, END)
    texto_red.insert(0, "00")
    texto_green.insert(0, "00")
    texto_blue.insert(0, "00")

def Numposiciones(digitos):
    numeros = 0
    letras = 0

    for a in digitos:
        if a.isdigit():
            numeros +=1
        elif a.isalpha():
            letras +=1
        else:
            pass
    return numeros, letras

def solo0_9_A_F():
    global count, color_totalparcial
    color_totalparcial = str(x_red + x_green + x_blue)
    count = 0

    for i in color_totalparcial:
        if i == "a":
            count = count+1
    for i in color_totalparcial:
        if i == "A":
            count = count+1

    for i in color_totalparcial:
        if i == "b":
            count = count+1
    for i in color_totalparcial:
        if i == "B":
            count = count+1

    for i in color_totalparcial:
        if i == "c":
            count = count+1
    for i in color_totalparcial:
        if i == "C":
            count = count+1

    for i in color_totalparcial:
        if i == "d":
            count = count+1
    for i in color_totalparcial:
        if i == "D":
            count = count+1

    for i in color_totalparcial:
        if i == "e":
            count = count+1
    for i in color_totalparcial:
        if i == "E":
            count = count+1

    for i in color_totalparcial:
        if i == "f":
            count = count+1
    for i in color_totalparcial:
        if i == "F":
            count = count+1
    
    for i in color_totalparcial:
        if i == "0":
            count = count+1
    for i in color_totalparcial:
        if i == "1":
            count = count+1
    for i in color_totalparcial:
        if i == "2":
            count = count+1
    for i in color_totalparcial:
        if i == "3":
            count = count+1
    for i in color_totalparcial:
        if i == "4":
            count = count+1
    for i in color_totalparcial:
        if i == "5":
            count = count+1
    for i in color_totalparcial:
        if i == "6":
            count = count+1
    for i in color_totalparcial:
        if i == "7":
            count = count+1
    for i in color_totalparcial:
        if i == "8":
            count = count+1
    for i in color_totalparcial:
        if i == "9":
            count = count+1
    return count, color_totalparcial
    

hexared = StringVar() 
hexared.set("00")
hexagreen = StringVar()
hexablue = StringVar()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
titulocambiocolor = Label(ventana, text="CAMBIADOR DE COLOR DE FONDO", font=("Roboto", 20),bg="#000000",fg="#ffff00")
titulocambiocolor.grid(row=1, column=1,columnspan=2,padx=5, pady=5)

titulored = Label(ventana, text="RED:", font=("Roboto", 20),bg="#000000",fg="#ff0000")
titulored.grid(row=2, column=1,columnspan=1,padx=5, pady=5)

titulogreen = Label(ventana,text="GREEN:",font=("Roboto", 20),bg="#000000",fg="#00ff00")
titulogreen.grid(row=3, column=1,columnspan=1,padx=5, pady=5)

tituloblue = Label(ventana,text="BLUE:",font=("Roboto", 20),bg="#000000",fg="#0000ff")
tituloblue.grid(row=4, column=1,columnspan=1,ipadx=5, ipady=5)

titulohexacolor = Label(ventana,text="#000000",font=("Roboto", 20),bg="#828282",fg="#000000")
titulohexacolor.grid(row=6, column=1,columnspan=2,ipadx=5, ipady=5)

titulovolver = Label(ventana,text="Para cambiar a color de Inicio volver a presionar SET COLOR",font=("Roboto", 12),bg="#828282",fg="#000000")
titulovolver.grid(row=7, column=1,columnspan=2,ipadx=5, ipady=5)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

botonsetcolor= Button(ventana,text="SET COLOR",font=("Roboto", 20),bg="#ffff00",fg="#000000",command = hexacolor)
botonsetcolor.grid(row=5, column=1,padx=3, pady=3,columnspan=2)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

texto_red = Entry(ventana,textvariable = hexared,font=("Roboto", 20), width=4)
texto_red.grid(row=2, column=2,columnspan=1,padx=5, pady=5)
#texto_red.insert(0, "00")

texto_green = Entry(ventana,textvariable = hexagreen,font=("Roboto", 20), width=4)
texto_green.grid(row=3, column=2,columnspan=1,padx=5, pady=5)
texto_green.insert(0, "00")

texto_blue = Entry(ventana,textvariable = hexablue,font=("Roboto", 20), width=4)
texto_blue.grid(row=4, column=2,columnspan=1,padx=5, pady=5)
texto_blue.insert(0, "00")

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
ventana.mainloop()


