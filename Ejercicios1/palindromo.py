def texto_sin_espacios (text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text

def text_al_reves (text):
    text_reverse = ""
    for char in text:
        text_reverse = char + text_reverse
    return text_reverse


def es_palindromo (texto):
    nuevo_texto = texto_sin_espacios(texto)
    texto_reves = text_al_reves(nuevo_texto)
    return nuevo_texto == texto_reves


print("JAVIER ARMANDO".lower())
print(es_palindromo("Abba".lower()))
print(es_palindromo("amo la paloma".lower()))
print(es_palindromo("Javier Armando".lower()))
print(es_palindromo("Reconocer".lower()))

