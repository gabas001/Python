'''Pedirle al usuario que ingrese cuatro números y mostrarle el promedio.'''
#se declaran las variables, mediante un imput se piede que ingrese solo numeros
#ya que esta definido por entero
n1= int(input('Ingresa nota 1: '))
n2= int(input('Ingresa nota 2: '))
n3= int(input('Ingresa nota 3: '))
n4= int(input('Ingresa nota 4: '))
#se calcula el promedio de los numeros ingresados
promedio= (n1+n2+n3+n4)/4
#se muestra el promedio
print('El promedio es: ',promedio)
