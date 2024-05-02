# Punto 1
def imprimir_sublista_medio(lista):
    mitad = len(lista) // 2
    sublista = lista[mitad - 1: mitad + 1]
    print("Sublista de la mitad de la lista original:", sublista)

# Punto 2
def imprimir_primero_ultimo(lista):
    print("Primer elemento:", lista[0], "Último elemento:", lista[-1])

# Punto 3
def agregar_elementos(lista):
    lista.extend(lista)
    print("Lista con elementos agregados al final:", lista)

# Punto 4
def ordenar_menor_a_mayor(lista):
    lista.sort()
    print("Elementos ordenados de menor a mayor:", lista)

# Punto 5
def ordenar_mayor_a_menor(lista):
    lista.sort(reverse=True)
    print("Elementos ordenados de mayor a menor:", lista)

# Punto 6
def cubo_elementos(lista):
    return [elemento ** 3 for elemento in lista]

mi_lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Lista original:", mi_lista)
imprimir_sublista_medio(mi_lista)
imprimir_primero_ultimo(mi_lista)
agregar_elementos(mi_lista)
ordenar_menor_a_mayor(mi_lista)
ordenar_mayor_a_menor(mi_lista)
nuevaLista = cubo_elementos(mi_lista)
print("Elementos al cubo:", nuevaLista)
