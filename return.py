def suma(a,b,c):
    return a + b + c

def sumas(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado

print(suma(4,5,6) + sumas(2,5,8,9,6,3,4,7,9))
