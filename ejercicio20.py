'''Escribir un programa que pida al usuario, que ingrese una frase por teclado.
El programa deberá tener dos funciones, una que reciba la frase y devuelva solo
las vocales de dicha frase y otra función que reciba la misma frase pero que
devuelva solo las consonantes. Mostrar por pantalla la frase original
ingresada por el usuario, las vocales y las consonantes devueltas por sus
respectivas funciones.'''
#iniciamos dos variables con listas vacias
vocales = []
consonantes = []
#iniciamos una funcion con una variable
def vocal(frase):
    #recorremos un for con la variable de la funcion
    for letra in frase:
        #recorremos el if con la variable del for para que busque 
        if letra in ('aeiouAEIOU'):
            #el if dentro del for buscara la variable declarada dentro de la
            #lista
            vocales.append(letra)
    #retornara en la lista 
    return(vocales)
#iniciamos una nueva funcion
def consonante(frase):
    for letra in frase:
        if letra not in ('aeiouAEIOU'):
            consonantes.append(letra)
    return(consonantes)
#pedimos al usuario que ingrese algo por teclado
frase = input('Ingrese una frase:')
#mostramos el resultado de lo ingresado por teclado
print('frase original:', frase)
print('Vocales:', vocal(frase))    
print('Consonantes:', consonante(frase))
