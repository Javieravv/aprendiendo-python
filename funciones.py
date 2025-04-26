# Aprendiendo funciones
def imprime():
    print(
        """
Estamos imprimiendo un texto
Aprendiendo Python""")
    

def imprimeTexto(saludo, nombre):
    print(f"{saludo} {nombre}")

def imprimeTexto1(saludo, nombre="Javier"):
    print(f"{saludo} {nombre}")


imprime()
imprimeTexto("Hola", "Xavier")
imprimeTexto("Cómo estás?", "Armando")
imprimeTexto1("Hola")
imprimeTexto1("Bienvenido")


