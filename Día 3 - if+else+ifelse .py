#   1. Entrada:Número. Salida: true si es mayor
#   de edad.
#   input siempre guarda el valor introducido como str. Si quieremos que sea un
#   entero hay que transformarlo. int(input)...))

#   Para saber el tipo -> print (type(numero))
edad = int(input("introduce tu edad: "))
print ("¿Es mayor de edad? ")
#   Se puede escribir 'esMayorEdad = >=18'
esMayorEdad = (edad >= 18)
print (esMayorEdad)
#   esMayorEdad es de tipo bool.
print(type(esMayorEdad))
if esMayorEdad:
# Ojo con las tabulaciones.
    print("Es mayor de edad")
#   Else debajo de if. No obligatorio.
else:
    print("Es menor de edad")
print ("Se imprime siempre")
#   Sin la variable bool esMayorEdad.
#   También se puede poner como:
#   if edad >=18
#   else:
#   print("Es menor de edad")
#   2. Entrada: Dia semana. Salida: True si fin de semana.
diaSemana = input("¿Introduce un día de la semana? ")
if diaSemana= Sabado 
elif diaSemana == Domingo
#   3. Entrada: Numero. Salida: True si es positivo.
numero = int(input("Introduce un número"))
print ("¿Es positivo?")
esPositivo = (numero > 0)
if esPositivo:
    print("Es positivo:")
elif numero == 0:
    print("Es 0")
else:
    print("Es negativo:")

#   4. Entrada: Letra. Salida: True si es vocal.
Vocal = input("¿Es una vocal? ")
print (Vocal =="a" or Vocal =="e" or Vocal =="o" or Vocal =="i" or Vocal =="u")
#   5. Entrada: Numero. Salida: True si está aprovado.
nota = int(input("¿ Introduce tu nota? "))
print ("¿Qué nota tiene? ")
#   Si no sumimos una nota válida.
#if nota <= 10 and nota >=9:
if nota > 10 or nota < 0:
    print("No es una nota válida ")
#   Asumimos una nota válida.
#   'if nota <= 10 and nota >= 9:
elif nota >= 9:
    print("Sobresaliente ")
elif nota >= 7:
    print ("Notable ")
elif nota >= 6:
    print ("Bien ")
elif nota >= 5:
    print ("suficiente ")
else:
    print ("Suspenso ")
