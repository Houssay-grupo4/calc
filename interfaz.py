import Resta
import division
import multiplicacion
import suma
import conjuncion

operacion = input("Escriba una operación de entre estas (suma, resta, multiplicacion, division): ")

a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))

if operacion == "resta":
    resultado = Resta.resta(a, b)
    print("El resultado de la resta es:", resultado)

elif operacion == "division":
    resultado = division.division(a, b)
    print("El resultado de la división es:", resultado)

elif operacion == "multiplicacion":
    resultado = multiplicacion.multiplicacion(a, b)
    print("El resultado de la multiplicación es:", resultado)

elif operacion == "suma":
    resultado = suma.suma(a, b)
    print("El resultado de la suma es:", resultado)

elif operacion  == "conjuncion":
  resultado = conjuncion.conjuncion(a, b)
  print("el resultado de la conjuncion es : ", resultado)

else:

 print("Operación no válida")