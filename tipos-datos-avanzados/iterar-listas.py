animales = ["perro", "gato", "venado", "vaca", "toro", "tigre", "león", "mono"]

# enumerate devuelve una tupla de indice y valor
for animal in enumerate(animales):
    print(animal, animal[1].capitalize())

# Si colocamos indice y variable, devuelve los dos elementos de la tupla en variables aparte
for indice, animal in enumerate(animales):
    print(indice, animal.capitalize())