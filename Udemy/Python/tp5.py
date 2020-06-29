numero1=int(input("Ingrese un numero minimo: \n"))
numero2=int(input("Ingrese otro numero maximo: \n"))
seleccion= input("p o np? p/n")


for i in range(numero1+1,numero2):
    if seleccion == "p"  and i%2==0:
        print(f"{i} ")
    elif seleccion != "p" and i%2 !=0:
        print(f"{i} ")
