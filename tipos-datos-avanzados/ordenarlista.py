animales = ["perro", "gato", "venado", "vaca", "toro", "tigre", "león", "mono", "perro", "venado", "vaca", "perro"]
numeros = [8,5,4,2,45,65,-5,25,1,65,125]
usuarios = [[4, "Javo"], [3, "Pedro"], [2, "Alicia"]]
usuarios1 = [["Javo", 4], ["Pedro", 3], ["Alicia", 2]]

def ordena(elemento):
    return elemento[1]

# print (animales)
# animales.sort()
# print (animales)
# animales.sort(reverse=True)
# print (animales)
# numeros1 = sorted(numeros, reverse=True)
# print(numeros)
# print(numeros1)
print (usuarios)
usuarios.sort()
print (usuarios)
usuarios1.sort(key=ordena)
print(usuarios1)



