'''Pedirle al usuario que ingrese dos números enteros por teclado y contar
cuantos números pares hay entre ambos valores ingresados, verificando también
los números ingresados por el usuario.'''
#se declaran variables y mediante un imput de tipo entero se piden numeros
n1 = int(input('Ingresa el primer numero entero: '))
n2 = int(input('Ingresa el segundo numero entero: '))
#el for recorre entre los numeros ingresados
for i in range (n1, n2+1):
    #el if indica que todo numero dividido por dos es par
    if i%2==0:
        #se muestran los numeros
        print('los numeros pares ingresados entre el primero y el segundo son: ',i)


