def primera_letra_mayuscula(cadena):
    return cadena[0].isupper()

# Punto 2
def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

# Punto 3
def obtener_lista_palabras(cadena):
    return cadena.split()

# Punto 4
def cadena_invertida(cadena):
    return cadena[::-1]

# Punto 5
def ultima_letra_mayuscula(cadena):
    palabras = cadena.split()
    palabras_modificadas = [palabra[:-1] + palabra[-1].upper() for palabra in palabras]
    return ' '.join(palabras_modificadas)

# Ejemplo de uso:
texto = "Hola mundo, este es un texto de ejemplo"
print("¿La primera letra es mayúscula?", primera_letra_mayuscula(texto))
print("Número de palabras en el texto:", contar_palabras(texto))
print("Lista de palabras:", obtener_lista_palabras(texto))
print("Texto invertido:", cadena_invertida(texto))
print("Texto con última letra de cada palabra en mayúscula:", ultima_letra_mayuscula(texto))