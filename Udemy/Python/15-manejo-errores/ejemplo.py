"""
Hacer un rograma que contenga una lista de n numeros enteros
recorer y mostrar
"""
import os
lista=[1,2,4,5,7,5,3,4,7,5]

def listar(plista):
    lista = ""
    for i in plista:
        lista += str(i)+", "
    return lista


"""def lee_entero(busqueda):
    try:
        busqueda = int(busqueda)
        return busqueda
    except ValueError:
        print("Ingrese un numero")
"""

def menu(plista):
    opcion="1"
    while(opcion != "5"):
        os.system('clear')
        print("\rver lista/1\nOrdenar lista/2\nLen lista/3\nbusca/4r\nsalir/5")
        opcion=input()
        print(" \n\n ")
        if opcion == "1":
            print("La lista es: \n{}".format(listar(lista)))
        elif opcion == "2":
            plista.sort()
            print("La lista fué ordenada")
        elif opcion =="3":
            print("La longitud de la lista es de {} elementos".format(len(plista)))
        elif opcion == "4":
            try:    
                busqueda = int(input("que numero bucará?: "))
                if(busqueda in plista):
                    print("La lista es: \n{}".format(listar(lista)))
                    print("El numero {} esta el pa posición {}".format(busqueda,plista.index(int(busqueda))))
                else:
                    print(f"el numero {busqueda} no se encuentra en la lista")
            except TypeError:
                print("Deves convertir tus cadenas a enteros....!!!!")
            except ValueError:
                print("Introduce un numero correcto !!")
        elif opcion == "5":
            print("Muchas gracias por su tiempo")
            break
        else:
             print("Ingrese un opcion correcta")
        input("Precione entrer para contnuar")

menu(lista)
