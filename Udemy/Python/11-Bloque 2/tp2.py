lista=[]

def hay_espacio(p_lista,p_n):
    return (p_n - len(p_lista)) >= 0

def lee_entero(entero):
    try:
        entero = int(entero)
        return entero
    except ValueError:
        print("Ingrese un numero")

def cargar_n_for(p_lista,p_n=10):
    if not hay_espacio(p_lista,p_n):
        print("Lista llena")
    else:
        for i in range(p_n-len(p_lista)):
            p_lista.append(input("Ingrese elemento: "))
        print("Lista llena: contiene {} elemntos".format(len(p_lista)))


def cargar_n_while(p_lista,p_n=10):
    if not hay_espacio(p_lista,p_n):
        print("Lista llena")
    else:
        while len(p_lista)<p_n:
            p_lista.append(input("Ingrese elemento: "))
    print("Lista llena: Contiene {} elementos".format(len(p_lista))) 


opcion = input("Cargar con While o For  F/W\nSalir S\n").upper()

while opcion != "S":
    if opcion != "F" and opcion != "W":
        print("Ingrese una opcion valida")
    else:
        dimension = input("Ingrese la dimension de la lista:\n")
        if lee_entero(dimension):
            if opcion == "W":
                cargar_n_while(lista,int(dimension))
            else:
                cargar_n_for(lista,int(dimension))
    opcion = input("Cargar con While o For  F/W\nSalir S\n").upper()
print(f"La lista es {lista}")
