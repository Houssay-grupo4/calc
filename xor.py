
def xor(a, b):
    resultado = a ^ b
    print("El resultado de la operación XOR entre", a, "y", b, "es:")
    print("En binario:", bin(resultado))
    print("En decimal:", resultado)


if __name__ == '__main__':
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    xor(a, b)