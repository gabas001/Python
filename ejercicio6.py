'''Si creamos tres listas. La primera contiene 4 números, la segunda contiene
5 letras y en la tercera le cargamos como elementos las dos listas anteriores.
¿Cuántos elementos contendrá la tercera lista? Demostrar mediante un breve
código.'''
#se declaran variales y entre los [] se define la lista
lista1=[1,2,3,4]
lista2=['a','b','c','d','e']
#se calculan las listas cargadas
lista3=lista1+lista2
#se muestran dicha suma
print(len(lista3))
