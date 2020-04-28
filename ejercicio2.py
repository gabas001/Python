'''Desarrollar un programa que solicite al usuario los lados de un rectángulo y
calcule su perímetro y su superficie. Informar ambos resultados por pantalla.'''

base=int(input('Ingresa la base'))
# se declara una variable, se le pide al usuario que ingrese algo y este se
#convierte en entero
altura=int(input('Ingresa la altura '))
#se declaro otra variable al igual que en el primer caso
perimetro=((base+altura)*2)
#se calcula las variables ingresadas
PI=3.1415926
#PI es utilizado para allar superficies
superficie= PI*(base+altura**2)
#se calcula el final
print('El perimetro es: ',perimetro)
#se le muestra al usuario el resultado
print('La superficie es: ',superficie)
