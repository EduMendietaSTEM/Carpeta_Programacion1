"""
Contexto: Estas organizando una fiesta de halloween y quieres
calcular cuantos dulces necesitas comprar para los niños que 
vendrán a tu casa.

Caso 1: Tenemos 500 dulce y vamos a repartirlos entre niños que
    cogen un numero aleatorio de dulces.
"""



import random

#Funciones:


#Codigo principal: 
numMaxDulcesNinioPorNinios = 5
numDulces = 500
esDulce = True

# while (esDulce):
#     print("ÑamÑam")
# #Para salir de un while True: tenemos que hacer Control+C.

while numDulces > 0:
    print (f"¡Hola ente! ¿Cuantos dulces quieres?") 
    numDulcesNinio = random.randrange(numMaxDulcesNinioPorNinios+1)
    print(f"¡Quiero {numDulcesNinio} dulces! ")
