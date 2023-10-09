"""
 Estás organizando una fiesta de Halloween y quieres calcular cuántos dulces necesitas comprar
 para los niños que vendrán a tu casa.

 Cada niño podrá llevarse 5 dulces y esperas la llegada de un máximo de 20 niños (si vienen más
 de 20 niños ponemos un cartel en la puerta que ponga: ¡No podemos comprar tantos dulces!)
 [Crea variables para almacenar estas cantidades]

 Crea un programa que solicite el número de niños que asistirán y calcule al cantidad total de 
 dulces que necesitas comprar. 
 [El cálculo se realizará en una función]
"""

import random
#Funciones:

def cuantosdulces(nNinios,nDulces):
    return nNinios*nDulces
#Codigo principal: 


numMaxDulcesNinioPorNinios = 5
numNinios = random.randrange(50)

#Como ya numNinios ya no puede ser entre 0 y 50, las comprobaciones sobran.
print(f"Vendran a visitarnos {numNinios} niños: ")
numDulces = cuantosdulces(numNinios,numMaxDulcesNinioPorNinios)  
print (f"¡Compraremos {numDulces} dulces!")