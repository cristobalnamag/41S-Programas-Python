from tkinter import *
from tkinter import messagebox as MessageBox
import time
from time import strftime
import pygame, sys
from pygame.locals import *
from tkinter import filedialog as filedialog

ventana= Tk()
ventana.title('ALARMA')
ventana.iconbitmap('alarma.ico') 
ventana.geometry('480x400')
ventana.resizable(0,0)
ventana.config(bg='black')

pygame.init()        #iniciamos modulo de pygame

def setalarma():
    global hora_alarma, x_hora, x_minutos, x_horapar, x_minutospar    

    setparx_hora = str(horatecleada.get())
    resultadosetparx_hora = NumLetras(setparx_hora)
    digitosLetras = resultadosetparx_hora[1]
    if digitosLetras > 0:
         error()
         borrardatos()
         resetalarma()
         tiempo_real()
    else:
         setparx_hora = int(horatecleada.get())
    if setparx_hora > 23:
         error()
         borrardatos()
         resetalarma()
         tiempo_real()
    elif setparx_hora < 10:
         x_horapar = str(setparx_hora)
         x_hora = str("0" + x_horapar)
    else:
         x_hora = str(setparx_hora)

    setparx_minutos = str(minutostecleados.get())
    resultadosetparx_minutos = NumLetras(setparx_minutos)
    digitosLetras = resultadosetparx_minutos[1]
    if digitosLetras > 0:
         error()
         borrardatos()
         resetalarma()
         tiempo_real()
    else:
         setparx_minutos = int(minutostecleados.get())
    if setparx_minutos > 59:
         error()
         borrardatos()
         resetalarma()
         tiempo_real()
    elif setparx_minutos < 10:
         x_minutospar = str(setparx_minutos)
         x_minutos = str("0" + x_minutospar)
    else:
         x_minutos = str(setparx_minutos) 
    hora_alarma = str(x_hora + " : " + x_minutos)
    texto_hora.delete(0, END)
    texto_minuto.delete(0, END)
    texto_hora.insert(0, "")
    texto_minuto.insert(0, "")
    texto_valoralarma.config(text= "ALARMA ACTIVADA",bg="#000000",fg="#dfff1a")  
    texto_valoralarma.after(4000, cerrar)

    return hora_alarma, x_hora, x_minutos, x_horapar, x_minutospar

def cerrar():
    texto_valoralarma.config(text= "----------",bg="#000000",fg="#dfff1a")    
def valoralarma():
    hora_alarmaparx = str(hora_alarma)
    hora_alarmax = str(hora_alarmaparx + " Hrs.")

    texto_valoralarma.config(text= hora_alarmax,bg="#000000",fg="#dfff1a")  
    texto_valoralarma.after(3500, cerrar)

def openfilesong():
    cancion = filedialog.askopenfilename()  #guardar el nombre o cancion que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)

def playsong():
    global x_minutos
    playx_minutos = int(x_minutos)
    playx_minutos += 1
    if playx_minutos < 10:
         x_minutospar = str(playx_minutos)
         x_minutos = str("0" + x_minutospar)
    else:
         x_minutos = str(playx_minutos)
    
    pygame.mixer.music.play()
    MessageBox.showinfo(message = hora_alarma, title="Alarma")
    
    return x_minutos

def stopsong():
    pygame.mixer.music.stop()
    resetalarma()

def resetalarma():
     global x_hora, x_minutos, hora_alarma, x_minutospar, x_horapar
     x_hora = ""
     x_minutos = ""
     x_horapar = ""
     x_minutospar = ""
     hora_alarma = str(x_hora + " : " + x_minutos)
     return x_hora, x_minutos, hora_alarma, x_minutospar, x_horapar

def posalarma():
    global hora_alarma, x_hora, x_minutos
    pygame.mixer.music.stop()

    posparx_hora = int(x_hora)
    if posparx_hora < 10:
         x_horapar = str(posparx_hora)
         x_hora = str("0" + x_horapar)
    else:
         x_hora = str(posparx_hora)

    posparx_minutos = int(x_minutos)
    posparx_minutos += 9
    if posparx_minutos < 10:
         x_minutospar = str(posparx_minutos)
         x_minutos = str("0" + x_minutospar)
    else:
         x_minutos = str(posparx_minutos)
    
    hora_alarma = str(x_hora + " : " + x_minutos)
    return hora_alarma, x_hora, x_minutos

def NumLetras(digitos):
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

def error():
    MessageBox.showerror("Error", "Ingresa una hora válida")

def borrardatos():
    texto_hora.delete(0, END)
    texto_minuto.delete(0, END)
    texto_hora.insert(0, "")
    texto_minuto.insert(0, "")

def tiempo_real():
    global hora, minutos, x_hora, x_minutos
    hora = strftime('%H')
    minutos = strftime('%M')
    segundos = strftime('%S')
    hora_total = str(hora + " : " + minutos + " : "+ segundos + " hrs.")
    texto_horareal.config(text= hora_total,bg="#000000",fg="#fafafa")
    print(hora_total)

    texto_horareal.after(1000, tiempo_real)

    if str(hora) == str(x_hora) :
        if str(minutos) == str(x_minutos) :
                playsong()    
    return hora, minutos, x_hora, x_minutos

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
x_hora = StringVar()
x_minutos = StringVar()
horatecleada = StringVar() 
minutostecleados = StringVar()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

tituloalarma = Label(ventana, text="ALARMA", font=("Roboto", 20),bg="#000000",fg="#fafafa")
tituloalarma.grid(row=1, column=1,columnspan=2,padx=5, pady=5)

titulohora = Label(ventana, text="HORA:", font=("Roboto", 20),bg="#000000",fg="#fafafa")
titulohora.grid(row=2, column=1,columnspan=1,padx=5, pady=5)

titulominuto = Label(ventana,text="MINUTOS:",font=("Roboto", 20),bg="#000000",fg="#fafafa")
titulominuto.grid(row=3, column=1,columnspan=1,padx=5, pady=5)

texto_horareal = Label(ventana, text="",font=("Roboto", 20),bg="#000000",fg="#fafafa")
texto_horareal.grid(row=4, column=1,columnspan=2,ipadx=5, ipady=5)

texto_valoralarma = Label(ventana, text="----------",font=("Roboto", 20),bg="#000000",fg="#fafafa")
texto_valoralarma.grid(row=5, column=1,columnspan=2,ipadx=5, ipady=5)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

botonset= Button(ventana,text="SET ALARMA",font=("Times New Roman", 16, "bold"),bg="#0d0FFF",fg="#fafafa",width= 17, height= 1, command = setalarma)
botonset.grid(row=6, column=1,padx=3, pady=3,columnspan=1)

botonvalor= Button(ventana,text="VALOR ALARMA",font=("Times New Roman", 16, "bold"),bg="#0d0FFF",fg="#fafafa",width= 17, height= 1, command=valoralarma)
botonvalor.grid(row=6, column=2,padx=3, pady=3,columnspan=1)

botonopensong = Button(ventana,text="GUARDAR SONIDO",font=("Times New Roman", 16, "bold"),bg="#919CA4",fg="#0d0d0d",width= 17, height= 1, command=openfilesong)
botonopensong.grid(row=7, column=1,padx=3, pady=3,columnspan=2)

botonpararalarma= Button(ventana,text="PARAR ALARMA",font=("Times New Roman", 16, "bold"),bg="#0d0FFF",fg="#fafafa",width= 17, height= 1, command= stopsong)
botonpararalarma.grid(row=8, column=1,padx=3, pady=3,columnspan=1)

botonposponeralarma= Button(ventana,text="POSPONER ALARMA",font=("Times New Roman", 15, "bold"),bg="#0d0FFF",fg="#fafafa",width= 17, height= 1, command=posalarma)
botonposponeralarma.grid(row=8, column=2,padx=3, pady=3,columnspan=1)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

texto_hora = Entry(ventana,textvariable = horatecleada,font=("Roboto", 20), width=4)
texto_hora.grid(row=2, column=2,columnspan=1,padx=100, pady=5)

texto_minuto = Entry(ventana,textvariable = minutostecleados,font=("Roboto", 20), width=4)
texto_minuto.grid(row=3, column=2,columnspan=1,padx=100, pady=5)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
tiempo_real()

ventana.mainloop()