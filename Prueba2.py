def NombreHobbit():
    return input("Introduce el nombre del Hobbit: ")
def EdadHobbit():
    return int(input("Introduce la edad del Hobbit: "))


def MenorDeEdad():
    num1 = EdadHobbit()
    num2 = EdadHobbit()
    num3 = EdadHobbit()
    return 


def resultado():

    Nombre = NombreHobbit()
    Edad = EdadHobbit()
    return f"Soy el Hobbit {NombreHobbit} + y tengo {EdadHobbit}s"
# 1 Crear tres Hobbits: Introduce, solicitándolo por pantalla, el nombre y la edad de los tres hobbits.
# Crea una variable booleana para cada hobbit en la que almacenes True o False dependiendo de si cada uno de 
#nuestros Hobbits puedeRepetir o no. 


Nombre1 = input("¿Como se llama el primer Hobbit?: ")
Nombre2 = input("¿Como se llama el segundo Hobbit?: ")
Nombre3 = input("¿Como se llama el tercer hobbit ")
Edad1 = int(input("Dime la edad del primero:" ))
Edad2 = int(input("Dime la edad del segundo: "))
Edad3 = int(input("Dime la edad del tercero:" ))


# 2 Menor de edad: ¿Sabéis que los hobbits cumplen la mayoría de edad a los 33 años? Si alguno de nuestros Hobbits tiene menos 
# de 33 años, automáticamente puede repetir. ¡Están en edad de crecimiento! [Esto debería hacerse con una bonita función]






# 3 Segunda oportunidad: Crea una función a la que le pases la edad de los tres hobbits y te devuelva la suma de las tres.  
# Si la suma es múltiplo de 2, el primer hobbit puede repetir. 
# Si la suma es múltiplo de 3, el segundo hobbit puede repetir. 
# Si la suma es múltiplo de 5, el tercer hobbit puede repetir.
# Por ejemplo: Si la suma fuera 60 años, los tres pueden repetir porque 60 es múltiplo de 2, 3 y 5. 

def TodasLasEdades(Edad1, Edad2, Edad3):

    operacion = input("Introduce suma: ")
    if operacion == "suma":
        resultado = Edad1 + Edad2 + Edad3








# ¿Qué ha pasado al final? Escribe por pantalla qué hobbits puede repetir y cuáles no.





# [EXTRA +1 PUNTO] Repartir: 
# Solo nos quedan dos platos de comida extra, así que toca decidir:
# Si los tres hobbits pueden repetir imprime “Toca repartir la comida”
# Si ningún hobbit puede repetir imprime “Va a sobrar comida”
# Si pueden uno o dos hobbits imprime  “¡A comer!”
