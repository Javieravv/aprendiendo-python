def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"], datos["description"])

get_product(id="id123", 
            name="Iphone", 
            description="Esto es un Iphone")
