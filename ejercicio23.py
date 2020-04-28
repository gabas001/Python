'''Hacer un programa que contenga tres botones y cada uno de ellos muestre por
pantalla (usando una etiqueta) un número al azar con el siguiente criterio:
•	Botón 1: un número al azar entre 0 y 10.
•	Botón 2: un número al azar entre 0 y 50.
•	Botón 3: un número al azar entre 0 y 100.'''
#librerias
from tkinter import *
import random
#funciones
def numero10():
    #cuadros de texto donde se declaran los parametros
    label1.configure(text=random.randint(0,10))
    
def numero50():
    label2.configure(text=random.randint(0,50))
    
def numero100():
    label3.configure(text=random.randint(0,100))
#inicio de la configuracion de la ventana
ventana = Tk()
ventana.title('presione el boton')
ventana.resizable(0,0)
ventana.geometry('450x100')
#fin de la configuracion
#confiracion de los botones
boton1= Button(ventana, text='un numero entre el 0 y el 10', command=numero10)
boton1.grid(row=0, column=0)

boton2= Button(ventana, text='un numero entre el 0 y el 50', command=numero50)
boton2.grid(row=0, column=1)

boton3= Button(ventana, text='un numero entre el 0 y el 100', command=numero100)
boton3.grid(row=0, column= 2)
#fin de la configuracion
#inicio de los cuadros de dialogos
label1= Label(ventana)
label1.grid(row=1, column=0)

label2= Label(ventana)
label2.grid(row=1, column=1)

label3= Label(ventana)
label3.grid(row=1, column=2)
#fin de los cuadros de dialogos
#fin del programa
ventana.mainloop()
