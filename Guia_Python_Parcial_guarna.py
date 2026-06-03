# #esarrollar una función que devuelva en un vector (una lista) los números primos entre 2 y 200. Reutilizar lo que ya se escribió y probó. 
# def primos ():
#     primos = []
#     for i in range (2,200):
#         es_primo = True
#         for j in range (2,int(i**0.5)+1):
#             if i % j == 0:
#                 es_primo = False
#                 break

#         if es_primo:
#             primos.append(i)
#     return primos
# print (primos())    

#Dados dos vectores A y B, de N elementos cada uno, se desean calcular:a. el vector suma. b. el producto escalar. 
# def suma (A,B):
#     suma = []
#     for i in range (len(A)):
#         resultado = A[i] + B[i]
#         suma.append(resultado)
#     return suma    
# print(suma([4,5,6,7,8,9],[4,2,5,6,2,9]))    

# def producto_escalar (A,B):
#     resultado = 0
#     for i in range (len(A)):
#         resultado = A[i] * B[i]
#     return resultado
# print(producto_escalar([4,5,6,7,8,9],[4,2,5,6,2,9]))

#Por cada alumno que rindió un examen de una materia se lee el número de legajoy la nota obtenida. Se desea saber la cantidad de alumnos que rindieron elexamen, el porcentaje de alumnos que obtuvieron cada nota, y el (o los) legajos de la nota más alta. 
# Esta es la estructura típica que te vas a encontrar en el parcial
# datos_alumnos = [
#     {"legajo": 10234, "nota": 7},
#     {"legajo": 10556, "nota": 9},
#     {"legajo": 10112, "nota": 4},
#     {"legajo": 10987, "nota": 9},
#     {"legajo": 10432, "nota": 6},
#     {"legajo": 10765, "nota": 2}
# ]

# def analizar_alumnos(datos_alumnos):
#     cantidad_alumnos = len(datos_alumnos)
#     conteo = {}
#     for anumno in datos_alumnos:
#         nota = anumno["nota"]
#         if nota in conteo:
#             conteo[nota] +=1
#         else:
#             conteo[nota] =1

#     porcentaje ={}
#     for nota, cantidad in conteo.item():
#         porcentaje = (cantidad / cantidad_alumnos) * 100
#         porcentaje[nota] = porcentaje

#     nota_maxima = max(conteo.keys())
#     legajos = []
#     for alumno in datos_alumnos:
#         if alumno["nota"] == nota_maxima:
#             legajos.append(alumno["legajo"])
#     return cantidad_alumnos, porcentaje, legajos
# cantidad_alumnos, porcentaje, legajos = analizar_alumnos(datos_alumnos)

#4. Escribir una función que reciba una lista y un valor y devuelva verdadero (True)
#si el valor está en la lista, falso (False) en caso contrario. Hacerlo sin usar in ni count.
# def buscar_valor (lista,valor):
#     for numero in lista :
#         if numero == valor:
#             return True
#     return False              
# print(buscar_valor([1,2,3,4,5],3))

# los mismo pero con count
# def buscar_valor (lista,valor):
#     return lista.count(valor) > 0
# print(buscar_valor([1,2,3,4,5],3))    

# Escribir una función que reciba una lista y un valor y devuelva la posición en que encuentra al valor en la lista, si el valor estuviera repetido devolver la primera aparición, si no estuviera devolver –1. Escribirla sin utilizar funciones como in,
# count, index, etc.
# def buscar_posicion (lista,valor):
#     for i in range(len(lista)):
#         if lista[i] == valor:
#             return i
#     return -1
# print(buscar_posicion([1,2,3,4,3],3))

#  Se leen dos vectores A y B, de N y M elementos respectivamente. Construir un algoritmo que halle los vectores unión e intersección de A y B. Desarrollarlo sin usar conjuntos (set) en Python. 

# def union (A,B):
#     union = list(A)
#     for elemenot in B:
#         if elemenot not in union:
#             union.append(elemenot)
#     return union
# print(union([1,2,3,4,5],[4,5,6,7,8]))

# def interseccion (A,B):
#     interseccion = []
#     for elemenot in A:
#         if elemenot in B and elemenot not in interseccion:
#             interseccion.append(elemenot)
#     return interseccion
# print(interseccion([1,2,3,4,5],[4,5,6,7,8]))

# Escribir un algoritmo que halle una matriz C como suma de dos matrices A y B.# La dimensión de las matrices de M × N se lee como dato (suponer un MAX para # fila y columna). 

# MAX_FILAS = 3
# MAX_COLUMNAS = 3
# def suma_matrices (A,B):
#     c = []
#     for i in range (MAX_FILAS):
#         fila = []
#         for j in range (MAX_COLUMNAS):
#             suma = A[i][j]+ B[i][j]
#             fila.append(suma)
#         c.append(fila)
#     return c
# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[9,8,7],[6,5,4],[3,2,1]]
# print(suma_matrices(A,B))

#. Escribir un algoritmo que halle un vector cuyos elementos son la suma de los elementos de cada fila de una matriz previamente ingresada. 
# def suma_filas (matriz):
#     fila = []
#     for i in range (len(matriz)):
#         suma = 0 
#         for j in range (len (matriz[i])):
#             suma = suma + matriz[i][j]
#         fila.append(suma)
#     return fila
# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# print(suma_filas(matriz))

#. Escribir un programa que calcule la traza de una matriz cuadrada. Recordar que la traza de una matriz es la suma de los elementos de su diagonal principal. 
# def traza (matriz):
#     suma = 0 
#     for i in range (len(matriz)):
#         suma = suma + matriz [i][i]
#     return suma
# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# print(traza(matriz))

# lo mismo pero saber si es la matriz identidad, la diagola = 1 1 1 
# def es_identidad (matriz):
#     for i in range (len (matriz)):
#         for j in range (len (matriz [i])):
#             if i == j and matriz [i][j] != 1 :
#                 return False
#             elif i != j and matriz [i][j] != 0 :
#                 return False
#     return True
# matriz = [[1,0,0],[0,1,0],[0,0,1]]
# print(es_identidad(matriz))

#Escribir un algoritmo que construya un vector con los valores mínimos de cada una de las filas de una matriz.
# def min_filas (matriz):
#     minimos = []
#     for i in range (len(matriz)):
#         minimo = matriz [i][0]
#         for j in range (len(matriz[i])):
#             if matriz [i][j] < minimo :
#                 minimo = matriz [i][j]
#         minimos.append(minimo)
#     return minimos
# matriz = [[1,2,3],[4,5,6],[7,8,9]]
# print(min_filas(matriz))

# capicua
# def capicua (palabra):
#     if palabra == palabra [::-1]:
#         return True
#     else :
#         return False
# print(capicua("ana"))

#Escribir una función que ordene alfabéticamente una lista de N nombres. Escribirlo sin utilizar sort ni sorted. 
# def ordenar_nombres (nombres):
#     for i in range (len(nombres)):
#         for j in range (i+1, len(nombres)):
#             if nombres[1] > nombres[j]:
#                 nombres[i], nombres[j] = nombres[j], nombres[i]
#     return nombres
# nombres = ["Julian", "Ana", "Carlos", "Beatriz"]
# print(ordenar_nombres(nombres))

# # ahora con sorted
# def ordenar_nombres (nombres):
#     return sorted(nombres)
# nombres = ["Julian", "Ana", "Carlos", "Beatriz"]
# print(ordenar_nombres(nombres))

#ahora con sort
# def ordenar (nombres):
#     nombres.sort()
#     return nombres
# nombres = ["Julian", "Ana", "Carlos", "Beatriz"]
# print(ordenar(nombres))

# from random import random

# provincias = [
#     "Buenos Aires", "CABA", "Catamarca", "Chaco", "Chubut", "Córdoba", 
#     "Corrientes", "Entre Ríos", "Formosa", "Jujuy", "La Pampa", "La Rioja", 
#     "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta", "San Juan", 
#     "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero", 
#     "Tierra del Fuego", "Tucumán"
# ]

# def cargar_datos():
#     # Creamos matrices de 24 filas x 12 columnas
#     # Lluvia: enteros (mm), Humedad: reales (promedio 0 a 100)
#     lluvia = [[random.randint(0, 300) for _ in range(12)] for _ in range(24)]
#     humedad = [[round(random.uniform(40.0, 90.0), 2) for _ in range(12)] for _ in range(24)]
    
#     return lluvia, humedad

# lluvia, humedad = cargar_datos()

# # a ) indicar q mes llovio mas en cada provincia, columnas 12, filas 24, cada fila es una provincia, cada columna un mes
# def mes_mas_lluvioso(lluvia):
#     for i in range (len(lluvia)):

#         max = lluvia[i][0]
#         mes = 0
#         for j in range (len(lluvia[i])):
#             if lluvia[i][j] > max:
#                 max = lluvia[i][j]
#                 mes = j 
#         print(f"En la provincia de {provincias[i]} el mes mas lluvioso fue el mes {mes+1} con {max} mm de lluvia")
# mes_mas_lluvioso(lluvia)

# #Indicar si la provincia donde más llovió es la que tiene mayor humedad relativa. 
# def provincia_mas_lluviosa(lluvia):
#     sumar_provincia = 0 
#     max_lluvia_total = 0  
#     for i in range (len(lluvia)):
#         for j in range (len(lluvia[i])):
#             sumar_provincia = sumar_provincia + lluvia[i][j]
#         if sumar_provincia > max_lluvia_total:
#             max_lluvia_total = sumar_provincia
#             provincia_mas_lluviosa = i
#         return provincia_mas_lluviosa
    
# provincia_mas_lluviosa(lluvia)
# inx = provincia_mas_lluviosa(lluvia)
# suma_humedad = 0 
# for j in range (len(humedad[inx])):
#     suma_humedad = suma_humedad + humedad[inx][j]
# promedio_humedad = suma_humedad / len(humedad[inx])
# es_la_mas_humeda = True

# for i in range (len(humedad)):
#     suma_humedad_provincia = sum(humedad[i]) / 12
#     if suma_humedad_provincia > promedio_humedad:
#         es_la_mas_humeda = False
# if es_la_mas_humeda:
#     print(f"La provincia con más lluvia es {provincias[inx]} y también es la más húmeda con un promedio de humedad de {promedio_humedad:.2f}%")
# else:
#     print(f"La provincia con más lluvia es {provincias[inx]} pero no es la más húmeda, su promedio de humedad es de {promedio_humedad:.2f}%")    


# def provincias_10_mas_lluviosas (lluvia, provincias):
#     suma_provincias = []
#     for i in range (len(lluvia)):
#         suma = sum(lluvia[i])
#         suma_provincias.append((suma, provincias[i]))
#     suma_provincias.sort(key = lambda x: x[0], reverse = True)

#     for i in range (10):
#         print(f"{suma_provincias[i][1]} con un total de {suma_provincias[i][0]} mm de lluvia")
# provincias_10_mas_lluviosas(lluvia, provincias)

# empezamos a pracrticar para el parcial, parcial 2,3, y 6 mas probables

# escribir una funcion q qreciba una cadna de caracteres, devuelva un entero con la cantidad de caracteres alabeticos distintos que tiene, no debe distinguir mayusculas, de minusculas , ni caracteres con tilde

# def contar (cadena):
#     cadena = cadena.lower()
#     cadena_limpia = ""
#     for char in cadena:
#         if 'a' <= char <= 'z':
#             cadena_limpia += char
    
#     conjunto_letras = set(cadena_limpia)
#     return len(conjunto_letras)
# print(contar("Hola Mundo!"))


# decir con false o true si la ciudad esta para vsiar o no, recibe una lsita de atraccioens, otra de actividades deseadoas, y un entero con el costo promedio por actividad, la ciudad se acepta si se realiza por lo menos 3 actividades deseados y costo promedio s menor o igual al MAX_COSTO ( asumir como predeinida)

# MAX_COSTO = 100
# def evaluar_ciudad (atracciones, desadas,  costo_promedio):
#     coincidencias = 0
#     for atraccion in desadas:
#         if atraccion in atracciones:
#             coincidencias += 1
#     if coincidencias >= 3 and costo_promedio <= MAX_COSTO:
#         return True
#     else:
#         return False
# print(evaluar_ciudad(["museo", "cine", "teatro"], ["museo", "teatro", "cine"], 80))

"""
ejemplo , votaciones = [["Luisa", 4], ["Mariano", 10], ["Luisa", 5]], 

{
    "Luisa": [9, 2],    # [Suma de puntos, Cantidad de votos]
    "Mariano": [10, 1]  # [Suma de puntos, Cantidad de votos]
}
"""

# def diccionario_votos (votaciones):
#     diccionario = {}
    
#     for voto in votaciones:
#         nombre = voto[0]
#         puntaje = voto[1]
#         if nombre not in diccionario:
#             diccionario [nombre] = [puntaje , 1 ]
#         else :
#             diccionario[nombre][0] += puntaje
#             diccionario [nombre][1] += 1

#     for nombre in diccionario:
#         suma = diccionario[nombre][0]
#         cantidad = diccionario[nombre][1]
#         promedio = suma / cantidad

#         diccionario[nombre] = [suma, cantidad ,promedio]
#     return diccionario
# votaciones = [["Luisa", 4], ["Mariano", 10], ["Luisa", 5]]
# print(diccionario_votos(votaciones))



#parcial 3

# def contraseña (cadena):
#     if len (cadena) < 8 and len (cadena) > 12:
#         return False
#     mayuscula = False
#     minuscula = False
#     numero = False
#     simbolo = False
#     simbolos_permitidos = ["*","-","@","$",]
#     for char in cadena:
#         if char.isupper():
#             mayuscula = True
#         elif char.islower():
#             minuscula = True
#         elif char.isdigit():
#             numero = True
#         elif char in simbolos_permitidos:
#             simbolo = True
#     return mayuscula and minuscula and numero and simbolo
# print(contraseña("Abcdéfg1*"))


# MAX_COSTO = 100
# def asociarce (actividades, intereses, costo):
#     coincidencias = 0
#     for actividad in intereses:
#         if actividad in actividades:
#             coincidencias += 1
#     return coincidencias >=3 and costo <= MAX_COSTO
# print(asociarce(["museo","cine","natacion"],["museo","cine","natacion"],90))

"""
Escribi una función que reciba 3 listas con mediciones diarias de valores para distintas personas. 
La primer lista es de temperaturas corporales, la segunda lista es de presencia de tos seca, y la tercera es del nivel de cansancio (medido del 1 al 10).

La función tiene que devolver una lista con los índices (posiciones), de quienes son sospechosos de COVID-19, cuando la temperatura sea mayor o igual a 37 grados, haya presencia de tos y el nivel de cansancio sea mayor a 6.

Por ejemplo, si ejecutaramos la función con los siguientes casos, obtendrías:
"""

# def sospechosos_covid (temperaturas,tos,cansancio):
#     sospechosos = [] 
#     for i in range (len(temperaturas)):
#         if temperaturas[i] >= 3 and tos[i] == True and cansancio [i] > 6:
#             sospechosos.append(i)
#     return sospechosos
# temperaturas = [36.5, 37.2, 38.0, 36.8]
# tos = [False, True, True, False]
# cansancio = [5, 7, 8, 4]
# print(sospechosos_covid(temperaturas,tos,cansancio))

"""
[ [“PP”, 19, 35], [“PSOE”, 20, 30], [“VOX”, 15, 15], [“PP”, 0, 15], …]. Los
recuentos son de diferentes mesas por lo que los partidos aparecerán
varias veces.
Se pide que escribas un programa en Python que procese esa lista y
genere un diccionario con clave partido y valor total_votos.  El total de
votos es la suma de diputados y senadores.
Luego, debe listar los partidos – total_votos, ordenados de mayor a
menor por total_votos.
"""

# def contar_votos(votaciones):
#     """
#     >>> votaciones = [["PP", 19, 35], ["PSOE", 20, 30], ["VOX", 15, 15], ["PP", 0, 15]]
#     >>> contar_votos(votaciones)
#     [('PP', 69), ('PSOE', 50), ('VOX', 30)]  
#     """
#     diccionario = {}
#     for voto in votaciones:
#         partido = voto[0]
#         diputados = voto[1]
#         senadores = voto [2]
#         total_votos = diputados + senadores

#         if partido not in diccionario:
#             diccionario[partido] = total_votos
#         else:
#             diccionario[partido] += total_votos
    
#     partidos_ordenados = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)

#     return partidos_ordenados

# votaciones = [["PP", 19, 35], ["PSOE", 20, 30], ["VOX", 15, 15], ["PP", 0, 15]]
# print(contar_votos(votaciones))
# import doctest
# doctest.testmod()



# PORCENTAJE = 0.60

# def aprobar (puntaje_max, puntaje_obtenido):
#     """
#     >>> aprobar([100, 100, 100], [60, 60, 60])
#     True
#     >>> aprobar([100, 100, 100], [59, 60, 60])
#     False
#     >>> aprobar([100, 100, 100], [60, 59, 60])
#     False
#     >>> aprobar([100, 100, 100], [60, 60, 59])
#     False
#     """
#     aprobado = True
#     indice = 0
#     while indice < len(puntaje_max) and aprobado:
#         puntaje_minimo = puntaje_max [indice] * PORCENTAJE
#         if puntaje_obtenido[indice] < puntaje_minimo:
#             aprobado = False
#         indice += 1
#     return aprobado
# print(aprobar([100, 100, 100], [60, 60, 60]))

# import doctest
# print(doctest.testmod())

# """
# funcion cadena, devolver tupla con cantidad de vocales no acentuadas para cada una de las vocales, tiene en cuenta mayusculas y minusculas, pero no acentos, ni dieresis, ni nada raro, solo a,e,i,o,u
# """

# def contar_vocales(cadena):
#     """
#     >>> contar_vocales("hola mundo")
#     (2, 1, 0, 1, 1)
#     >>> contar_vocales("HOLA MUNDO")
#     (1, 0, 0, 2, 1)
#     """
#     con_a = 0
#     con_e = 0
#     con_i = 0
#     con_o = 0
#     con_u = 0
#     resultado = ()
#     for caracter in cadena:
#         if caracter.lower() == "a":
#             con_a += 1
#         elif caracter.lower() == "e":
#             con_e += 1
#         elif caracter.lower() == "i":
#             con_i += 1
#         elif caracter.lower() == "o":
#             con_o += 1
#         elif caracter.lower() == "u":
#             con_u += 1
    
#     resultado = (con_a, con_e, con_i, con_o, con_u)
#     return resultado
# print(contar_vocales("hola MUndo"))
# import doctest
# print(doctest.testmod())


"""
sublistas = emplesa string puesto string salarios  intm, hacer un diccionario con clave: puesto , valores : total_salarios, cantidad, salario_promedio, 
ordenarlos de mayor a menor por promedio salarialla salida debe estar formateada de forma que se visualice una columna para los puestos y otra para el proedio salarial.

"""
# def procesar_salarios (salarios):
#     puestos = {}

#     for salario in salarios:
#         puesto = salario[1]
#         monto = salario[2]

#         if puesto in puestos:
#             acumulado = puestos[puesto][0] + monto
#             cantidad = puestos[puesto][1] + 1
#             promedio = acumulado / cantidad
#             puestos[puesto] = (acumulado, cantidad, promedio)
#         else:
#             puestos[puesto] = (monto, 1, monto)
#     return puestos

# def ordenar_por_promedio(puestos):
#     puestos_ordenados = sorted(puestos.items(), key=lambda x: x[1][2], reverse=True)
#     return puestos_ordenados

# def main():
#     salarios = [
#         ["Empresa A", "Gerente", 5000],
#         ["Empresa B", "Analista", 3000],
#         ["Empresa A", "Analista", 3200],
#         ["Empresa C", "Gerente", 5500],
#         ["Empresa B", "Gerente", 4800],
#         ["Empresa C", "Analista", 3100]
#     ]
#     estadisticas = procesar_salarios(salarios)
#     puestos_ordenados = ordenar_por_promedio(estadisticas)
#     print(f"{'Puesto':<15} {'Promedio Salarial':>20}")
#     for puesto, datos in puestos_ordenados:
#         print(f"{puesto:<15} {datos[2]:>20.2f}")
# if __name__ == "__main__":
#     main()

# PORCENTAJE = 0.60
# def aprobados (maximas_notas, notas_obtenidas):
#     aprobado = True
#     indice = 0
#     while indice < len(maximas_notas) and aprobado:
#         nota_minima = maximas_notas[indice] * PORCENTAJE
#         if notas_obtenidas[indice] < nota_minima:
#             aprobado = False
#         indice += 1
#     return aprobado
# print(aprobados([100, 100, 100], [60, 60, 60]))


# def vocales_en_cadena (cadena):
#     """
#     >>> vocales_en_cadena("Hola Mundo")
#     (2, 1, 0, 1, 1)
#     >>> vocales_en_cadena("HOLA MUNDO")
#     (1, 0, 0, 2, 1)

#     """
#     con_a = 0 
#     con_e = 0
#     con_i = 0
#     con_o = 0
#     con_u = 0 
#     respuesta = ()
#     for char in cadena:
#         if char == "a" or char == "A":
#             con_a += 1
#         elif char == "e" or char == "E":
#             con_e += 1
#         elif char == "i" or char == "I":
#             con_i += 1 
#         elif char == "o" or char == "O":
#             con_o += 1
#         elif char == "u" or char == "U":
#             con_u += 1 
#     return (con_a, con_e, con_i, con_o, con_u)
# print(vocales_en_cadena("Hola Mundo"))

# import doctest
# print(doctest.testmod())

# def covid_nineteen (temperatura, tos,cansancio ):

#     """
#     >>> covid_nineteen([36.5, 37.2, 38.0, 36.8], [False, True, True, False], [5, 7, 8, 4])
#     [1, 2]
#     #probar 2 casos mas, uno sin sospechosos y otro con todos sospechosos
#     >>> covid_nineteen([36.5, 36.2, 36.0, 36.8], [False, False, False, False], [5, 5, 5, 5])
#     []
#     >>> covid_nineteen([37.5, 38.2, 39.0, 37.8], [True, True, True, True], [7, 8, 9, 10])
#     [0, 1, 2, 3]    

#     """

#     sospechoso = []
#     for paciente in range(len(temperatura)):
#         if temperatura[paciente] >= 37 and tos[paciente] == True and cansancio[paciente] > 6:
#             sospechoso.append(paciente)
#     return sospechoso

# temperaturas = [36.5, 37.2, 38.0, 36.8]
# tos = [False, True, True, False]
# cansancio = [5, 7, 8, 4]
# print(covid_nineteen(temperaturas,tos,cansancio))

# import doctest
# print(doctest.testmod(verbose=True))

# def _validar (cadena):

#     """
#     >>> _validar("Abcdeeefg1*")
#     True
#     >>> _validar("Abcdefg1*")
#     False
#     >>> _validar("Abcdeeefg1")
#     False
#     >>> _validar("Abcdeeefg*")
#     False
#     >>> _validar("Abcdeeefg1*#")
#     False
#     """
#     permidos = ["@","#","-","!"]
#     largo = len(cadena)
#     mayuscula = 0
#     minuscula = 0
#     simbolo = 0
#     digito = 0
#     es_valida = (8 <= largo <= 12)

#     for char in cadena :
#         if "A" <= char <="Z" :
#             mayuscula +=1
#         elif "a" <= char <= "z" :
#             minuscula +=1
#         elif "0"<= char <= "9":
#             digito +=1
#         elif char in permidos:
#             simbolo +=1
#         else:
#             es_valida = False
#     if not (mayuscula >=1 and minuscula >=3 and digito >=2 and simbolo >=1):
#         es_valida = False
    
#     return es_valida
# print(_validar("AAsdw23#"))

"""
lista de listass, saber si son cuadradas

"""
# [[4,5,6],[1,5,7]]

# def es_cuadrada(matriz):
#     n = len(matriz)
#     es_cuadrada = True
#     i = 0
#     while i < n and es_cuadrada:
#         if len(matriz[i]) != n:
#             es_cuadrada = False
#         i += 1
    
#     return es_cuadrada
# print(es_cuadrada([[4,5,6],[1,5,7]]))

# def matriz_diagonal (matriz):
#     simetrica = True
#     n = len(matriz)
#     i = 0
#     while i < n and simetrica:
#         for j in range (i+1, n):
#             if matriz[i][j] != matriz[j][i]:
#                 simetrica = False
#         i += 1
    
#     return simetrica
# print(matriz_diagonal([[1,2,3],[2,5,6],[3,6,9]]))

# def crear_diccionario(salarios):
#     diccionario = {}
    
#     for registro in salarios:
        
#         puesto = registro[0]
#         monto = registro[1]
        
#         if puesto in diccionario:
#             total = diccionario[puesto][0] + monto
#             cantidad = diccionario[puesto][1] + 1
#             promedio = total / cantidad
#             diccionario[puesto] = (total, cantidad, promedio)
#         else:
            
#             diccionario[puesto] = (monto, 1, float(monto))
            
#     return diccionario

# def contar_min_may_etc (cadena):
#     mayusculas = 0 
#     minusculas = 0 
#     otros = 0 
#     tupla = ()
#     for char in cadena:
#         if char.isupper():
#             mayusculas += 1 
#         elif char.islower():
#             minusculas += 1
#         elif char != " ":
#             otros += 1
#     tupla = (mayusculas, minusculas, otros)
#     return tupla
# print(contar_min_may_etc("Hola Mundo!mEEEgustaPython"))

# def covid (temperatura, tos, cansancio):
#     sospechosos = []
#     """
#     >>> covid([36.5, 37.2, 38.0, 36.8], [False, True, True, False], [5, 7, 8, 4])
#     [1, 2]
#     >>> covid([36.5, 36.2, 36.0, 36.8], [False, False, False, False], [5, 5, 5, 5])
#     []
#     >>> covid([37.5, 38.2, 39.0, 37.8], [True, True, True, True], [7, 8, 9, 10])
#     [0, 1, 2, 3]
#     """
    
#     for paciente in range(len(temperatura)):
#         if temperatura[paciente] >= 37 and tos[paciente] == True and cansancio [paciente] > 6:
#             sospechosos.append(paciente)
#     return sospechosos
# print(covid([36.5, 37.2, 38.0, 36.8], [False, True, True, False], [5, 7, 8, 4]))
# import doctest
# print(doctest.testmod(verbose=True))


# def elejir_comida (comidas, prohibidas):
#     """
#         elejir_comida([],[])
#         rpt
#     """
#     permitidas = []

#     for comida in comidas:
#         if not any ( ing in prohibidas for ing in comida[1:]):
#             permitidas.append(comida[0])
#     return permitidas
# elejir_comida()
# import doctest
# print(doctest.testmod(verbose=True))

# def comidass_elejir (prohibidas, comidas):
#     permitidas = []

#     for sublista in comidas:
#         nombre = sublista[0]
#         ingredientes = sublista[1:]

#         apta = True
#         for ing in ingredientes:
#             if ing in prohibidas:
#                 apta = False

#         if apta:
#             permitidas.append(nombre)
#     return permitidas
# comidass_elejir()

# def comidas_elejir (comidas, prohibidas):
#     permitidas = []

#     i = 0 
#     while i < len (comidas):
#         nombre = comidas [0]
#         sublista = comidas [i]

#         apta = True
#         j = 1

#         while j < len (sublista) and apta :
#             if sublista [j] in prohibidas:
#                 apta = False
#             j += 1

#         if apta :
#             permitidas.append(nombre)
#         i += 1
#     return permitidas

# ej [["llv", 2, 3, 5], ...]
# def votaciones_Arg (votaciones):
#     diccionario = {}
#     total_votos = 0 
#     mesas_estructuras = len (votaciones)

#     for registro in votaciones:
#         partido = registro [0]
#         diputados = registro[2]
#         senadores = registro [3]
#         votos_mesa = diputados + senadores

#         total_votos += votos_mesa

#         if partido not in diccionario:
#             diccionario[partido] = [diputados, senadores]
#         else:
#             diccionario[partido][0] += diputados
#             diccionario[partido][1] += senadores
#     return diccionario, total_votos, mesas_estructuras

# def mostrar_informe (total_votos, diccionario):
#     listado = []
#     for partido , totales in diccionario:
#         suma = totales [0] + totales[1]
#         porcentaje = (suma / total_votos) * 100
#         listado.append((partido, suma, porcentaje))
#     listado.sort(key = lambda x: x[1], reverse= True)
#     return listado

# def analisis (cadena):
    
#     cant_a = 0
#     cant_e = 0
#     cant_i = 0 
#     cant_o = 0 
#     cant_u = 0

#     for char in cadena :
#         if char == "a" or char == "A":
#             cant_a += 1
#         elif char == "e" or char == "E":
#             cant_e += 1
#         elif char == "i" or char == "I":
#             cant_i += 1
#         elif char == "o" or char == "O":
#             cant_o += 1
#         elif char == "u" or char == "U":
#             cant_u += 1
#     return(cant_a, cant_e, cant_i,cant_o,cant_u)
# print(analisis("aaAeEiiiioo9oooOU"))

# porcentaje = 0.60 
# def aprobo (puntaje_max , notas_obtenidas):
#     """
#     >>> aprobo_cursada([10, 10, 10, 10, 10], [6, 7, 8, 9, 10])
#     True
#     >>> aprobo_cursada([10, 10, 10, 10, 10, 10], [6, 6, 6, 6, 6, 5])
#     False
#     """
#     Aprobacion = True
#     i = 0 
#     while i < len (puntaje_max) and Aprobacion:
#         if puntaje_max [i] * porcentaje > notas_obtenidas[i]:
#             Aprobacion = False
#         i += 1
#     return Aprobacion
# print (aprobo([10, 10, 10, 10, 10, 10], [6, 6, 6, 6, 6, 6]))
# import doctest


# def modular (salarios):
#     diccionarios = {}

#     for sublista in salarios:
#         puesto = sublista [0]
#         salario = sublista [1]

#         if puesto not in diccionarios:
#             diccionarios[puesto] = [salario, 1 ,salario]
#         else:
#             diccionarios[puesto][0] += salario
#             diccionarios[puesto][1] += 1
    
#     for puesto in diccionarios:
#         total = diccionarios[puesto][0]
#         cantidad = diccionarios[puesto][1]
#         diccionarios[puesto][2] = total / cantidad
#     return diccionarios

# def informe (diccionarios):
#     lista_ordenada = []
#     for puesto, valores in diccionarios.items():
#         lista_ordenada.append((puesto, valores[2]))

#     lista_ordenada.sort(key = lambda x: x[1], reverse= True)
#     return lista_ordenada

# def main ():
#     salarios = obtener_lista_salarios()

#     diccionario = modular(salarios)

#     informe(diccionario)

# if __name__ == "__main__":
#     main()

# def analisar_ (cadena):
#     cant_mayus = 0
#     cant_minus = 0
#     otros = 0

#     for char in cadena:
#         if char.isupper():
#             cant_mayus +=1
#         elif char.islower():
#             cant_minus += 1
#         elif char not in  " ":
#             otros += 1
#     return(cant_mayus, cant_minus, otros)
# print(analisar_tetas("AÁEÉ Iiií )=)))999ooíoó"))


# def covid (temperatura, tos, cansancio):
#     sospechos = []
    
#     for paciente in range(len(temperatura)):
#         if temperatura[paciente] >= 37 and tos[paciente] and cansancio[paciente] > 6:
#             sospechos.append(paciente)
#     return sospechos

# print(covid(...))}

# def analisis (salarios):
#     diccionario = {}
#     for puestos in salarios:
#         nombre = puestos[0]
#         salario = puestos[1]

#         if nombre not in diccionario:
#             diccionario[nombre] = [salario, 1, salario]

#         else :
#             diccionario[nombre][0] += salario
#             diccionario[nombre][1] += 1
        
#     for nombre in diccionario:
#         total_salarios = diccionario[nombre][0]
#         cantidad = diccionario[nombre][1]
#         diccionario[nombre][2] = total_salarios / cantidad

#     return diccionario
# print(analisis(...))

# def informe (diccionario):
#     listisha = []
    
#     for nombre, dato in diccionario.items():
#         listisha.append((nombre, dato[2]))

#     listisha.sort(key = lambda x: x[1] , reverse=True)

#     return listisha
# informe(analisis(...))


# def analisis (cadena):
#     a = 0
#     e = 0
#     i = 0
#     o = 0 
#     u = 0
#     for char in cadena :
#         if char in "aAáÁ":
#             a +=1
#         elif char in "eéEÉ":
#             e +=1
#         elif char in "iíIÍ":
#             i += 1
#         elif char in "oóOÓ":
#             o += 1
#         elif char in "uúUÚ":
#             u += 1
#     return(a,e,i,o,u)
# print(analisis("aeiuo,aeiou"))

# porcentaje  = 0.60
# def aprobadoooo (notas_maximas, notas_obtenidas):
#     aprobado = True
#     i = 0
#     while i < len(notas_maximas) and aprobado:
#         if notas_maximas[i] * porcentaje > notas_obtenidas[i]:
#             aprobado = False
#         i += 1

#     return aprobado
# aprobadoooo (...)

#from Datos_Generales import obtener_datos

# sistema_previsional = {
#     "España": [100,30,20,"UE"],
#     "Alemania": [110,40,10,"UE"],
#     "Argentina": [130,50,40,"Mercosur"],

# }

#sistema_previsional = obtener_datos()

# def promedios (sistema_previsional):
#     trabajando = 0
#     desempleada = 0
#     jubilada = 0

#     for datos in sistema_previsional.values():
#         trabajando += datos[0]
#         jubilada += datos[1]
#         desempleada += datos[2]

#     trabajando = trabajando/len(sistema_previsional)
#     jubilada = jubilada /len (sistema_previsional)
#     desempleada = desempleada /len(sistema_previsional)

#     return trabajando, jubilada, desempleada

# def listado (sistema_previsional):
#     lista_ordenar = []
#     for pais , datos in sistema_previsional.items():
#         trab, jub, desemp, _ = datos
#         total_personas = trab +jub + desemp

#         tasa_desemp = (desemp/total_personas) * 100
#         relacion_jubilados_trab = (jub / trab)
#         lista_ordenar.append((pais, tasa_desemp, relacion_jubilados_trab))
    
#     lista_ordenar.sort(key = lambda x : x[1], reverse = True)

# def agrupar_dicc (sistema_previsional):
#     dicci= {}

#     for datos in sistema_previsional.items():
#         trab, desp, jub, grupo = datos
        

#         if grupo not in dicci:
#             dicci[grupo] =[trab,jub,desp]
        
#         else:
#             dicci[grupo][0] += trab
#             dicci[grupo][1] += jub
#             dicci[grupo][2] += desp
#     return dicci

# def comida_prfereida (comidita, ingredientre_prohibios ):
#     permitidos = []
#     i = 0

#     while i < len (comidita):
#         nombre = comidita[i]
#         ingredientres = comidita[1:]

#         apta = True
#         j = 1

#         while j < len(ingredientres) and apta:
#             if ingredientres[j] in ingredientre_prohibios:
#                 apta = False

#             j+=1
#         i+=1
#     if apta :
#         permitidos.append(nombre)
#     return permitidos

# def caracteres_diferentes (cadena):
#     cantidad_caracteres = 0
#     lista = []
   
#     for char in cadena:
#         char = char.lower()

#         if char in "áéíóú":
#             if char == "á": 
#                 char = "a"
#             elif char == "é": 
#                 char = "e"
#             elif char == "í": 
#                 char = "i"
#             elif char =="ó":
#                 char = "o"
#             elif char == "ú":
#                 char = "u"

#         if char not in lista:
#             lista.append(char)
    
#     return len(lista)
# caracteres_diferentes ("fhsdauwb1948712hd")

# MAX_COSTO = 100
# def visitar_o_no (actividades_disponibles, actividades_querias, presupuesto ):
#     coincidencias = 0
#     se_puede = False
#     i = 0
#     while i < len(actividades_querias) and coincidencias <=3 :
#         if actividades_querias[i] in actividades_disponibles:
#             coincidencias += 1
#         i += 1
    
#     if coincidencias >= 3 and presupuesto < MAX_COSTO:
#         se_puede = True
    
#     return se_puede
# visitar_o_no(...)

# def camino_fama (votaciones):
#     dicco = {}

#     for votacion in votaciones :
#         nombre = votacion[0]
#         puntaje = votacion[1]

#         if nombre not in dicco:
#             dicco[nombre] = [puntaje , 1, 0]
#         else :
#             dicco[nombre][0] += puntaje
#             dicco[nombre][1] += 1
    
#     for nombre in dicco:
#         sumatoria = dicco[nombre][0]
#         total = dicco[nombre][1]
#         dicco [nombre][2]  = sumatoria / total
#     return dicco

# def ordenarlo (dicco):

#     listado = []

#     for nombre , dato in dicco.items():
#         listado.append((nombre,dato[2]))

#     listado.sort( key=lambda x: x[1], reverse = True)

#     return listado

# def main ():
#     votos_recibidos = [
#         ["Messi", 10], 
#         ["Messi", 9], 
#         ["Dibu", 10], 
#         ["Julian", 8], 
#         ["Dibu", 8],
#         ["Messi", 10]
#     ]
#     diccionario_procesado = camino_fama (votos_recibidos)

#     ranking = ordenarlo(diccionario_procesado)

#     print (diccionario_procesado, ranking)


# if __name__ == "__main__":
#     main ()



