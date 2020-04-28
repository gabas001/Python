'''Modificar el siguiente código para que no de error al recibir un argumento
que no es del tipo Lista.

def lista (argumentos):
    print(argumentos)
    print(len(argumentos))

lista([1,'hola',['a','b','c']])'''

def  lista ( * argumentos ):
    print ( argumentos )
    print ( len ( argumentos ))

lista ([ 1 , 'hola' , [ 'a' , 'b' , 'c' ]])
