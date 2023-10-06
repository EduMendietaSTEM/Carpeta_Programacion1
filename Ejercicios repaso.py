#10

num1 = float (input("Dime el primer número:"))
num2 = float (input("Dime el segundo número:"))
operacion = input("Introduce resta o suma")
suma = (num1+num2)
resta = (num1-num2)

if operacion == "suma":
    print (num1+num2)

elif operacion == "resta":
    print (num1-num2)

else:
    print ("La operacion no es válida")

#print(f"La operacion '{operacion}' da de resultado {resultado})


#13 
color = "azul" 
otroColor = input("Introduce un color")
if color == otroColor:
    print (f"¿Cómo sabias que ese era mi color favorito es {color}?")



#14


# esGanador = False
diaSemana = input("Introduce un día de la semana:")
diaSemana = ("viernes, sabado, domingo")
print("No solicito numero porque ya lo he pedido antes....:")

if diaSemana == "viernes":
    print("Has ganado")
elif diaSemana == "lunes" and num1 == 1:
esGanador = True

elif diaSemana == "martes" and num1 == 2:
esGanador = True
print("has ganado")

else:
print("has perdido")
esGanador = False
#.....
#Magnífica variable.
esGanador = diaSemana = "viernes:"

if esGanador("Has ganado"):

else:
    print("Has perdido")



    