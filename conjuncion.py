def conjuncion(a, b):
    if a < 3 and b > 8:
        a = a + 1
    else:
        a = a * b
    return a

a = conjuncion(a, b)
print('a =', a)

