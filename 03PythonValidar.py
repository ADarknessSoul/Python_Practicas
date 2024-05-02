import re

def validar_correo(correo):
    # Patrón para validar una dirección de correo electrónico
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Utilizamos la función match de la librería re para buscar el patrón en la cadena de correo
    if re.match(patron, correo):
        return True
    else:
        return False

# Capturamos la cadena de texto que representa la dirección de correo
direccion_correo = input("Ingrese una dirección de correo electrónico: ")

# Llamamos a la función validar_correo para determinar si la dirección ingresada es válida
if validar_correo(direccion_correo):
    print("La dirección de correo electrónico es válida.")
else:
    print("La dirección de correo electrónico no es válida.")