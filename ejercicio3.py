'''Pedir al usuario que ingrese por teclado dos números reales y utilizarlos
para realizar todas las operaciones aritméticas vistas (suma, resta,
multiplicación, división, potencia, división entera y resto). Mostar todos los
resultados por pantalla (un resultado por línea) con su respectiva leyenda
aclarando de que operación se trata.'''

n1= complex(input('Ingresa primer numero: '))
n2= complex(input('Ingresa segundo numero: '))
# se declaran variables, y se le piden al usuario que ingrese por teclado
#se hacen los respectivos calculos y se le muestra al usuario
suma= n1.real + n2.real
print('La suma es = ',suma)

resta= n1.real - n2.real
print('La resta es = ',resta)

multiplicacion= n1.real * n2.real
print('La multiplicaccion es = ',multiplicacion)

divicion= n1.real / n2.real
print('La divicion es = ',divicion)

potencia= n1.real ** n2.real
print('La potencia es: ',potencia)

divicionN= n1.real // n1.real
print('LA divicion entera es = ',divicionN)

resto= n1.real % n2.real
print('El resto es: ',resto)
