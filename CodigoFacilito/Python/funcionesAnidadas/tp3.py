texto="asd"

def estaBacio(p_texto):
    return len(p_texto)<=0


if estaBacio(texto):
    print("La lista está bacia")
    texto=input("Ingrese Freace en minusculas\n")
print("El texto ingresado es: {}".format(texto.upper()))
