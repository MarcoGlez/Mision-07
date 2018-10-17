#Autor: Marco Goznalez Elizalde
"""Ejecuta una accion entre dos opciones y sale hasta que lo decida el usuario,
puede dividir un numero mediante restas o encontrar el número mayor en una serie de valores"""


#Realiza una division restando el divisor al dividendo
def dividir(dividendo,divisor):
    cociente = 0
    residuo = dividendo
    #Cuando se intenta dividir entre 0
    if divisor == 0:
        print("ERROR, no se puede dividir entre 0")
    #Cuando se divide un entero positivo entre un entero positivo
    elif (divisor>0 and dividendo>=0):
        while(residuo >= divisor):
            residuo -= divisor
            cociente += 1
        print("%d / %d = %d y sobran %d" %(dividendo,divisor,cociente,residuo))
    #Cuando se divide un entero negativo entre un entero negativo
    elif (divisor<0 and dividendo<=0):
        while (residuo <= divisor):
            residuo -= divisor
            cociente += 1
        print("%d / %d = %d y sobran %d" % (dividendo, divisor, cociente, residuo))
    # Cuando se divide un entero positivo entre un entero negativo
    elif (divisor<0 and dividendo>=0):
        while(residuo >= divisor*-1):
            residuo += divisor
            cociente -=1
        print("%d / %d = %d y sobran %d" % (dividendo, divisor, cociente, residuo))
    # Cuando se divide un entero negativo entre un entero positivo
    elif (divisor>0 and dividendo<=0):
        residuo = dividendo *-1
        while(residuo >= divisor):
            residuo -= divisor
            cociente -=1
        print("%d / %d = %d y sobran %d" % (dividendo, divisor, cociente, residuo*-1))


#Encuentra el entero más grande en una serie de datos dados por el usuario
def encontrarMayor():
    mayor = 0
    entero = 0
    while(entero != -1):
        entero = int(input("Teclea un número [-1 para salir]: "))
        if entero <-1:
            print("ERROR, solamente números enteros positivos")
        if entero > mayor:
            mayor = entero
    #Si no se ingresa ningun dato, se regresa que no hay un valor mayor
    if mayor ==0:
        print("No hay valor mayor")
    else:
        print("El mayor es:",mayor)


def elegirPrograma():
    print("""Misión 07. Ciclos while"
Autor: Marco González Elizalde
Matrícula: A01376527
1. Calcular divisiones
2. Encontrar el mayor
3. Salir""")
    opcion = int(input("Teclea tu opción: "))
    print("")
    return opcion


#Funcion principal
def main():
    opcion = 0
    while(opcion !=3):
        opcion = elegirPrograma()
        
        if opcion == 1:
            print("Calculando divisiones.")
            dividendo = int(input("Teclea el dividendo: "))
            divisor = int(input("Teclea el divisor: "))
            dividir(dividendo,divisor)
            print("")
        
        elif opcion == 2:
            print("Teclea una serie de números para encontrar el mayor.")
            encontrarMayor()
            print("")
        
        elif opcion ==3:
            print("Gracias por usar este programa, regresa pronto")
            print("")
        
        else:
            print("ERROR, teclea 1, 2 o 3")
            print("")


#Corre el programa principal
main()
