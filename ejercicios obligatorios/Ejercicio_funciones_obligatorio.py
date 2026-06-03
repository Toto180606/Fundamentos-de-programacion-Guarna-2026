import doctest

def mcd(a, b):  

    """
    recibe: dos numeros enteros a y b, acompañados de la funcion abs que el valor absoluto de a y b
        permitiendo que el algoritmo funcione correctamente aunque el usuario ingresa numeros negativos.

    proceso: utiliza el algoritmo de Euclides para calcular el maximo comun divisor (mcd) entre a y b 

    devuelve: el maximo comun divisor (mcd) entre a y b, o 0 si ambos son 0.    
    >>> mcd(48, 18) 
    6
    >>> mcd(56, 98) 
    14
    >>> mcd(101, 10)
    1
    >>> mcd (0, 5)  
    5
    >>> mcd (5, 0)
    5
    >>> mcd (0, 0)
    0
    """

    a = abs(a)      
    b = abs(b) 
    if a == 0 and b == 0: 
        return 0 
     
    while b!= 0 : 
        a, b = b, a % b 
    return a 

def mcm (a,b):

    """
    recibe: dos numeros enteros a y b, acompañados de la funcion abs que el valor absoluto de a y b
        permitiendo que el algoritmo funcione correctamente aunque el usuario ingresa numeros negativos

    proceso: utiliza la relacion entre el maximo comun divisor (mcd) y el minimo comun multiplo (mcm) para calcular el mcm entre a y b.

    devuelve: el minimo comun multiplo (mcm) entre a y b, o 0 si alguno de los dos es 0

    >>> mcm(48, 18)
    144
    >>> mcm(0, 5)
    0
    >>> mcm(5, 0)
    0
    >>> mcm(-20, 10)
    20
    >>> mcm(7, 3)
    21
    """
    if a == 0 or b == 0: 
        return 0 
    return abs(a * b) // mcd(a, b) 

def main ():

    """
    recibe: dos numeros enteros a y b
    proceso: solicita al usuario que ingrese dos numeros y calcula su mcd y mcm
    devuelve: los resultados del mcd y mcm, aparte hay unos casos de prueba para verificar que el programa funcione correctamente

    """
    a = int(input("ingrese un numero: ")) 
    b = int(input("ingrese otro numero: ")) 
    
    print (f"el mcd de {a} y {b} es: {mcd(a, b)}") 
    print (f"el mcm de {a} y {b} es: {mcm(a, b)}") 

print(doctest.testmod())


if __name__ == "__main__":
    main()
