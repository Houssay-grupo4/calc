def a_es_par_impar(a):
    return a % 2 == 0;

def b_es_par_impar(b):
    return b % 2 == 0;

def condicional_doble(a,b):
    if(a_es_par_impar(a) == b_es_par_impar(b)):
        print(f"Se cumple con la condicional doble, dado que tanto el número {a} como el número {b} son pares o impares.")
    else:
        print(f"No se cumple con la condicional doble, dado que uno es par y el otro, impar")