import tkinter as tk
from pygame import mixer
from os import walk,getcwd
import numpy as np

class ReproductorMusical:

    def __init__(self ,container):
        container = tk.Tk() # creo variable con tkinter
        self.container = container
        self.container.title("Reproductor Media ")# creo el titulo de la applicacion
        self.container.geometry("500x300") # medidas de la interfaz
        self.container.configure(background="Black")# color de fondo de la interfaz 
        self.cancion = ""
        self.estado = "Stopped"
        self.ruta = "musica/"
        self.agregar_musica
        self.agregar_label
        self.crear_botones
        self.container.mainloop()# me ejecuta la interfaz creada 
    
    @property
    def agregar_musica(self):
        self.lista_canciones = tk.Listbox(self.container,selectmode="SINGLE")
        self.lista_canciones.insert(1,"hm.mpeg")
        self.lista_canciones.insert(2,"hyp.mpeg")
        self.lista_canciones.pack()

    @property
    def agregar_label(self):
        self.label=tk.Label(self.container,text=self.estado)#creo un cuadro tipo label definiendo tamaño y tipo de letra
        self.label.pack(side=tk.BOTTOM,fill=tk.X)# posicion de la barra en la interfaz (BOTTOM es para que vaya en la parte de abajo) TOP (arriba) fill sera el eje donde se presentara

    @property
    def crear_botones(self):
        buttonframe = tk.LabelFrame(self.container, text="Flow",font=("times new roman",15,"bold"),bg="black",fg="white",bd=5)
        buttonframe.place(x=0,y=100,width=600,height=100)    
        self.play = tk.Button(buttonframe,text="PLAY",width=10,command = self.reproducir_cancion, height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=0,padx=10,pady=5)
        self.pause = tk.Button(buttonframe,text="PAUSE",width=8,command = self.pausar_cancion,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=1,padx=10,pady=5)
        self.stop = tk.Button(buttonframe,text="STOP",width=10,command = self.detener_cancion,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="pink").grid(row=0,column=2,padx=10,pady=5)
        
    def reproducir_cancion(self):
        mixer.init()
        self.cancion = self.lista_canciones.get(self.lista_canciones.curselection())
        mixer.music.load(self.ruta+self.lista_canciones.get(self.lista_canciones.curselection()))
        if self.estado.__eq__("Paused"):
            self.estado = "Unpaused"
            self.label.configure(text=self.estado)
            mixer.music.unpause()
        self.estado = "Playing"
        self.label.configure(text=self.estado)
        mixer.music.play()
 
        

    def detener_cancion(self):
        self.estado = "Stopped"
        self.label.configure(text=self.estado)
        mixer.music.stop()
            

    def pausar_cancion(self):
        self.estado = "Paused"
        self.label.configure(text=self.estado)
        mixer.music.pause()
            


a = ReproductorMusical('aa')
