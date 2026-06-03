# Tomas Agustin Gallego
import doctest

def generar_lista_frecuencias(lista_numeros):
    """
    Recibe una lista de números enteros desordenados y potencialmente repetidos.
    Genera una lista de listas donde cada sublista contiene el elemento y su
    cantidad de apariciones.

    >>> generar_lista_frecuencias([5, 2, 1, 1, 2, 5, 5, 6])
    [[5, 3], [2, 2], [1, 2], [6, 1]]
    >>> generar_lista_frecuencias([])
    []
    >>> generar_lista_frecuencias([1, 2, 3])
    [[1, 1], [2, 1], [3, 1]]
    """
    if not lista_numeros:
        return []

    frecuencias = {}
    for num in lista_numeros:
        if num in frecuencias:
            frecuencias[num] += 1
        else:
            frecuencias[num] = 1

   
    lista_de_listas = [[num, freq] for num, freq in frecuencias.items()]
    return lista_de_listas


def ordenar_ascendente_por_elemento(lista_de_listas):
    """
    Recibe la lista de sublistas y la ordena de forma ascendente según el elemento.

    >>> ordenar_ascendente_por_elemento([[5, 3], [2, 2], [1, 2], [6, 1]])
    [[1, 2], [2, 2], [5, 3], [6, 1]]
    >>> ordenar_ascendente_por_elemento([[3, 1], [1, 1], [2, 1]])
    [[1, 1], [2, 1], [3, 1]]
    >>> ordenar_ascendente_por_elemento([[10, 5], [5, 5]])
    [[5, 5], [10, 5]]
    """
  
    lista_copia = list(lista_de_listas)
    lista_copia.sort(key=lambda x: x[0], reverse=False)
    return lista_copia


def ordenar_descendente_por_cantidad(lista_de_listas):
    """
    Recibe la lista de sublistas y la ordena de forma descendente según la cantidad.

    >>> ordenar_descendente_por_cantidad([[5, 3], [2, 2], [1, 2], [6, 1]])
    [[5, 3], [2, 2], [1, 2], [6, 1]]
    >>> ordenar_descendente_por_cantidad([[3, 1], [1, 1], [2, 1]])
    [[3, 1], [1, 1], [2, 1]]
    >>> ordenar_descendente_por_cantidad([[10, 5], [5, 2]])
    [[10, 5], [5, 2]]
    """
    lista_copia = list(lista_de_listas)
    lista_copia.sort(key=lambda x: x[1], reverse=True)
    return lista_copia

print(doctest.testmod(verbose=True))
