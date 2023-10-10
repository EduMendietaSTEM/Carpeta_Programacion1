#Funciones

#Código principal
#Los FOR en python son lo que en otro lenguages se llaman 
#FOREACH: para cada elemento de una lista, hago lo que ponga dentro de FOR.

#Creamos una lista de mounstruos.
listaDeMonstruos = ["Bruja", "Vampiro", "Fantasma", "Hombre Lobo", "Zombie"  ]


# for *cadaElemento* in *unaLista*: *Hacemos algo*

print("\nImprimo la listaDeMonstruos")
for monstruo in listaDeMonstruos:
    print(f"¡{monstruo}s! ¡Que miedo!", end=" ---")

# Ponemos 10+1 en vez de 11 porque queremos llegar hasta el 10,
# y asi lo vemos directamente.
print("\nImprimo: for numero in range(1,10+1): ")
for numero in range(1,10+1):
    print(numero)

print("Imprimo: for numero in range(10): ")
for numero in range(10):
    print(numero, end="---")

print("\nImprimo los numeros impares hasta el 10.")
for numero in range(1,10+1,2):
    print(numero, end="---")

print("\nImprimo los numeros pares hasta el 10.")
for numero in range(2,10+1,2):
    print(numero, end="---")

print("\nImprimo los numeros del 10 al 1:")
for numero in range(10,1-1,-1):
    print(numero, end="---")