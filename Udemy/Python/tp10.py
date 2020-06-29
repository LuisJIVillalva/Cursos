cantidad_alumnos= int(input("Cuantos alumnos clasificara\n"))
cont_aprobados=0
cont_desaprobados=0
nota_max=0
nota_min = 100
for i in range(cantidad_alumnos):
    nota = int(input(f"Ingrese nota {i+1}"))
    if nota_max< nota:
         nota_max=nota
    if nota_min> nota:
         nota_min=nota
    if nota >= 6:
        print ("Aprobado")
        cont_aprobados+=1
    else:
        print("Desaprobado")
        cont_desaprobados+=1

print(f"La cantidad de alumnos Desaprobados son: {cont_desaprobados}")
print(f"La cantidad de alumnos Aprobados son: {cont_aprobados}")
print(f"La nota maximas es {nota_max}\n")
print(f"La nota minima es {nota_min}\n")
"""alien vs depredador
asterix y obelix
batman Rebenge
clock tower
cool world
donal duck
Dragon ball z hyper Dimension
ilusion of gaia
migthy morphin power rangers - figting edition
Secret of Evermore
Sim City 2000
Star Ocean
Super Bomberman Panic Bomber World
Terranigma
Top Gear 3000
Uniracers
WWF Super Wrestlemaniaa"""
