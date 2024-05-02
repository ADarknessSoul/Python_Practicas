#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import datetime

def calcularEdad(data):
    # Obtener la fecha de nacimiento de la lista de datos
    fecha_nacimiento = None
    for item in data:
        if item[0] == "fechaNacimiento":
            fecha_nacimiento = item[1]
            break
    # Calcular la edad
    fecha_actual = datetime.datetime.now().date()
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
    edad = fecha_actual.year - fecha_nacimiento.year
    return edad

# sample_data = [
#     ["nombre", input("Nombre: ")],
#     ["apellido1", input("Primer apellido: ")],
#     ["apellido2", input("Segundo apellido: ")],
#     ["cargo", input("Cargo: ")],
#     ["empresa", input("Empresa: ")],
#     ["calle", input("Calle: ")],
#     ["numeroExt", int(input("Número exterior: "))],
#     ["numeroInt", int(input("Número interior: "))],
#     ["colonia", input("Colonia: ")],
#     ["municipio", input("Municipio: ")],
#     ["estado", input("Estado: ")],
#     ["codigoPostal", int(input("Código Postal: "))],
#     ["telefono", input("Teléfono: ")],
#     ["correoElectronico", input("Correo Electrónico: ")],
#     ["fechaNacimiento", input("Fecha de Nacimiento (dd/mm/yyyy): ")],
# ]

sample_data = [
    ["nombre", "Pedro"],
    ["apellido1", "Pérez"],
    ["apellido2", "Torres"],
    ["cargo", "Developer"],
    ["empresa", "ABC Company"],
    ["calle", "Main Street"],
    ["numeroExt", 123],
    ["numeroInt", 3],
    ["colonia", "Downtown"],
    ["municipio", "Cityville"],
    ["estado", "Stateville"],
    ["codigoPostal", 12345],
    ["telefono", "555-123-4567"],
    ["correoElectronico", "john.doe@example.com"],
    ["fechaNacimiento", "01/01/1990"],
]

#Serializar la lista de datos en un archivo con pickle 
with open("data.pkl", "wb") as file:
    pickle.dump(sample_data, file)
file.close()

#Deserializar la lista de datos en un archivo con pickle
with open("data.pkl", "rb") as file:
    data = pickle.load(file)
    #print(data)

    #Leer el archivo formatoBackup.txt y reemplazar los valores de la lista de datos
    with open("formatoBackup.txt", "r", -1, "UTF-8") as file:
        content = file.read()
        #print(content)
        for item in data:
            content = content.replace(f"[{item[0]}]", str(item[1]))
        
        edad = calcularEdad(data)
        # Agregar la edad al final de la variable content
        content += f"\nEdad: {edad}"
        file.close()

        with open("formato.txt", "w", -1, "UTF-8") as file:
            file.write(content)
            file.close()
            