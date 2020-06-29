tabla = ""
for i in range (1,11):
    tabla = "Tabla del "+str(i)+": "
    for j in range(0,11):
        if j!=10:
            tabla += str(i*j) + ", "
        else:
            tabla += str(i*j)
    print(tabla)
