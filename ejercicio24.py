'''Modificar el código del ejemplo de la página 15 del apunte de la clase 3
para que, además de mostrar mediante una etiqueta el texto que ingresamos en
la caja de texto, luego de hacerlo, borre todo el contenido de dicha caja
de texto, limpiando el formulario antes del próximo ingreso.

from tkinter import *

ventana = Tk()
ventana.title("Ingreso de datos")
ventana.resizable(0,0)
ventana.geometry("600x300")

def click():
        mensaje=texto.get()
        etiqueta_dos.config(text=mensaje)

etiqueta_uno=Label(ventana, text='Texto a ingresar')
etiqueta_uno.grid(row=0,column=0)

etiqueta_dos=Label(ventana,text='Ingrese un texto')
etiqueta_dos.grid(row=1,column=0)

texto=Entry(ventana,width=30)
texto.grid(row=0,column=1)

boton=Button(ventana,text='Aceptar', command=click)
boton.grid(row=0,column=2)

ventana.mainloop()'''
#libreria para configurar la ventana
from tkinter import *
#inicio de la configuracion de la ventana
ventana = Tk()
ventana.title("Ingreso de datos")
ventana.resizable(0,0)
ventana.geometry("600x300")
#fin de la configuracion
#declaracion de la funcion
def click():
        #variable a ejecutar el mensaje
        mensaje=texto.get()
        #variable de configuracion para el mensaje
        etiqueta_dos.config(text=mensaje)
        #variable donde se va a borrar el mensaje
        texto.delete(0,len(mensaje))
#etiquetas de para configurar lo que va a mostrar la ventana
etiqueta_uno=Label(ventana, text='Texto a ingresar')
etiqueta_uno.grid(row=0,column=0)

etiqueta_dos=Label(ventana,text='Ingrese un texto')
etiqueta_dos.grid(row=1,column=0)

texto=Entry(ventana,width=30)
texto.grid(row=0,column=1)
#boton que ejecuta la accion para mostrar el mensaje
boton=Button(ventana,text='Aceptar', command=click)
boton.grid(row=0,column=2)

ventana.mainloop()
