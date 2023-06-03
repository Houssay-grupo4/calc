import Resta
import division
import multiplicacion
import suma
import conjuncion
import condicionalD
import Disyuncion
import xor


operacion = input("Escriba una operación de entre estas (suma, resta, multiplicacion, division, condicional doble, conjuncion, disyuncion, xor : ")

if operacion in ["suma", "resta", "multiplicacion", "division","conjuncion", "condicional doble"]:
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))

elif operacion == "disyuncion":
    a = input("Ingrese el primer valor (True o False): ").lower()
    b = input("Ingrese el segundo valor (True o False): ").lower()


else:
     operacion == "xor"
     a = int(input("Ingrese el primer número: "))
     b = int(input("Ingrese el segundo número: "))


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
  print("El resultado de la conjuncion es : ", resultado)

elif operacion == "condicional doble":
    resultado = condicionalD.condicional_doble(a, b)

elif operacion == "disyuncion":
    resultado = Disyuncion.disyuncion(a == "true", b == "true")
    print("El resultado de la disyuncion es:", resultado)

elif operacion == "xor":
     resultado = xor.xor(a, b)
     
         
    
else:
    print("Operación no válida")