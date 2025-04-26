# Funciones con varios parámetros
def suma(a, b):
    print (a + b)

def sumas(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(f"El resultado de la suma es {resultado}")


suma(4,8)
sumas(1,2,3,4,5,6,7)
sumas(5,10,15,20,25,30,35,40,45)