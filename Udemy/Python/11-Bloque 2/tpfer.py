Lista1=[]

def rellenar(Lista1):
  if len(Lista1) <= 10:
    dato=input("Ingrese elemento: ")
    Lista1.append(dato)
    rellenar(Lista1)
  else:
    print(Lista1)
    print("Lista llena")

rellenar(Lista1)
