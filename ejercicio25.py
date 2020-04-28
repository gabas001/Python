'''Crea una función llamada modificar() que a partir de una lista de números
realice las siguientes tareas sin modificar la original:
• Borrar los elementos duplicados.
• Ordenar la lista de mayor a menor.
• Eliminar todos los números impares.
• Realizar una suma de todos los números que quedan.
• Añadir como primer elemento de la lista la suma realizada.
• Devolver la lista modificada.
Una vez escrita la función, utilizarla y verificar que la el primer elemento
de dicha lista, coincide con la suma de los demás elementos.'''
#declaramos una variable de tipo lista con elementos en ella
lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, -5, -12, 17]
#funcion que se utilizara para recorrer la lista
def modificar(lista):
    #mostrara la lista pre-creada
    print('Lista original: ',lista)
    #variable para mostrar la lista sin duplicados
    lista=list(set(lista))
    print('lista sin duplicados: ',lista)
    #variable donde nos mostrara la lista ordenada de mayor a menor
    lista.sort(reverse=True)
    print('lista ordenada de mayor a menor: ', lista)
    #inicializamos una nueva lista sin nada
    listapares=[]
    #recorremos un for con la lista creada anteriormente
    for n in lista:
        #ecuacion donde buscara todos los elementos divicibles por 2
        if n%2==0:
            listapares.append(n)
    #sumara todos los elementos divicibles por dos
    suma= sum(lista)
    #agregara el elemento del resultado al inicio de la lista
    lista.insert(0, suma)
    #mostrara por pantalla la suma
    print('la suma sin los impares es: ', suma)
    lista.append(suma)
    print('lista con la suma es: ', lista)
    #retornara en la lista finalizada
    return lista
#variable para mostrar la nueva lista modificando la anterior
nueva_lista= modificar(lista)
#mostrara la nueva lista por pantalla
print('la lista es: ', nueva_lista)
