#   Funciones.

#   num1, num2 y num3 son argumentos de entrada.
def mediaTresNumeros (num1,num2, num3):
    resultado = (num1+ num2+ num3) /3
    return resultado

#Para  operaciones sencillas:
def mediaTresNumeros (num1,num2, num3):
    return (num1+num2+num3)/3

#Para dividir la operaión en más sencilla:
def mediaTresNumeros (num1,num2, num3):
    suma =num1+num2+num3
    return suma/3

# resultado argumento de salida.

#   Podemos tener fucinones sin return
#   Esto es una excepción,  de normal no usamos
#   print() en funciones, solo cuando el
#   objetivo de la función sea mostrar algo.


def dibujarLinea(forma): #  forma = "="
    print(forma*20)
# sin return

def dibujarLineaPuntos (): #sin parámetros de entrada.
    print("."*20)
#Para hacerlo sin print ():
def crearLinea (forma):
    return forma*20
#Ejercicio:
def presentacion (nombre,edad):
    return ("Hola me llamo Edu y tengo 21 años")
#------------------------------------

# Código Principal.
print ("Probando función")
media = mediaTresNumeros (20,30,40)
print (media)
dibujarLinea("=")
dibujarLinea("x")
dibujarLinea("_")
dibujarLineaPuntos ()
#   print () de lo que devuelve la función.
#   Para no hacer print() dentro....
print(crearLinea("*"))

#-------------------------------------

dibujarLinea("o")
mediaTresNumeros (5,10,15)
print (mediaTresNumeros (5,10,15))
mediaTresNumeros (15,23,87)
print (mediaTresNumeros (15,23,87))
dibujarLinea("O")

#Ejercicio: Nombre función -> programarla
nombre = input("Escribe tu nombre:")
edad = input("Escribe tu edad:")
print(presentacion(nombre,edad))
























