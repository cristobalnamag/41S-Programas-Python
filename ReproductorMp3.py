from tkinter import * #importamos la libreria tkinter
import pygame, sys
from pygame.locals import *
from tkinter import filedialog
from PIL import ImageTk, Image

pygame.init()        #iniciamos modulo de pygame

#funcion boton abrir cancion
def openfilesong():
    cancion = filedialog.askopenfilename()  #guardar el nombre o cancion que queremos reproducir
    print(cancion)
    pygame.mixer.music.load(cancion)
def playsong():
    pygame.mixer.music.play()
def stopsong():
    pygame.mixer.music.stop()
def pausesong():
    pygame.mixer.music.pause()
def resumesong():
    pygame.mixer.music.unpause()
def masvolumensong():
    volumenlevel = pygame.mixer.music.get_volume() + 0.5
    print(volumenlevel)
    pygame.mixer.music.set_volume(volumenlevel)
def menosvolumensong():
    volumenlevel = pygame.mixer.music.get_volume() - 0.5
    print(volumenlevel)
    pygame.mixer.music.set_volume(volumenlevel)

raiz = Tk()
raiz.title('Reproductor MP3 - GUI')  #para poner titulo de la ventana
raiz.iconbitmap('mp3.ico') #para cambiar icono de la ventana
raiz.geometry("550x400")   #Forza a la ventana Raiz Root a tener este tamaño 
raiz.resizable(0, 0)

#crear Frame
frameprincipal = Frame(raiz, bg="#4a4a4a")
frameprincipal.pack(fill="both", expand=1)

#etiquetas label ->Titulo reproductor
tituloreproductor = Label(frameprincipal, text="Reproductor MP3 - GUI", font=("Times New Roman", 30, "bold"), bg="#4a4a4a", fg="#fbfbfb")
tituloreproductor.place(relx=0.13, rely=0.35)

#crear botones
#Boton open song
botonopensong = Button(frameprincipal, text="Open Song", bg="#919CA4", fg="#fbfbfb", width= 10, height= 2, font=("Times New Roman", 12, "bold"), command=openfilesong)
botonopensong.place(relx=0.03, rely=0.5)
#Boton PLay song
botonplaysong = Button(frameprincipal, text="Play", bg="#2DCD32", fg="#fbfbfb", width= 10, height= 2, font=("Times New Roman", 12, "bold"), command=playsong)
botonplaysong.place(relx=0.22, rely=0.5)
#Boton Stop song
botonstopsong = Button(frameprincipal, text="Stop", bg="#e2504c", fg="#fbfbfb", width= 10, height= 2, font=("Times New Roman", 12, "bold"), command=stopsong)
botonstopsong.place(relx=0.41, rely=0.5)
#Boton Resume song
botonresumesong = Button(frameprincipal, text="Resume", bg="#33AFFF", fg="#fbfbfb", width= 10, height= 2, font=("Times New Roman", 12, "bold"), command=resumesong)
botonresumesong.place(relx=0.60, rely=0.5)
#Boton Pause song
botonpausesong = Button(frameprincipal, text="Pause", bg="#ffa400", fg="#fbfbfb", width= 10, height= 2, font=("Times New Roman", 12, "bold"), command=pausesong)
botonpausesong.place(relx=0.79, rely=0.5)  #anchor para puntos cardinales
#Boton Volumen +
botonmasvolumensong = Button(frameprincipal, text="+ Volumen", bg="#008080", fg="#fbfbfb", width= 10, height= 2, font=("Times New Roman", 12, "bold"), command=masvolumensong)
botonmasvolumensong.place(relx=0.53, rely=0.7)  #anchor para puntos cardinales
#Boton Volumen -
botonmenosvolumensong = Button(frameprincipal, text="- Volumen", bg="#800000", fg="#fbfbfb", width= 10, height= 2, font=("Times New Roman", 12, "bold"), command=menosvolumensong)
botonmenosvolumensong.place(relx=0.33, rely=0.7)  #anchor para puntos cardinales

raiz.mainloop()