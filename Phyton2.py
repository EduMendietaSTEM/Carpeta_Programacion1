# El input recoge el dato y lo guarda en nombre.
nombre = input("Introduce tu nombre: ")
print ("Hola " + nombre)

#   Existen dos tipos de =s en programación:
#   = -> Asigna lo que hay a la izquierda a
#           lo que hay en la derecha.
#           Ej. numero=5
#   ==  -> Es un igual LÓGICO.  ¡Compara los
#           valores que tiene a izq y der!
#           Devuleve true, si son iguales; o
#           false, si son distintas.

#   1. Entrada:Número. Salida: true si es mayor
#   de edad.
#   input siempre guarda el valor introducido como str. Si quieremos que sea un
#   entero hay que transformarlo. int(input)...))
numero = int(input("Introduce tu edad: "))
#   Para saber el tipo -> print (type(numero))
print ("¿Es mayor de edad? ")
print (numero >= 18)
#   2. Entrada: Dia semana. Salida: True si fin de semana.
diaSemana = input("¿Introduce un día de la semana? ")
print ("¿Es fin de semana?: ")
print ( diaSemana == "Sabado" or diaSemana == "Domingo")
#   3. Entrada: Numero. Salida: True si es positivo.
numero = int(input("¿Es un número positivo?"))
print (numero >=0)
#   4. Entrada: Letra. Salida: True si es vocal.
Vocal = input("¿Es una vocal? ")
print (Vocal =="a" or Vocal =="b" or Vocal =="o" or Vocal =="i" or Vocal =="u")
#   5. Entrada: Numero. Salida: True si está aprovado.
numero = int(input("¿ He aprovado? "))
print (numero >=5 and numero <=10)
             


