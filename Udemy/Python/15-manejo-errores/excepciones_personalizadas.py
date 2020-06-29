try:
    nombre= input("Introduce el nombre: ")
    edad=int(input("Introduce la edad"))
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif  len(nombre) <= 1:
        raise ValueError("El nombre no está completo")
    else:
        print(f"Bienvenido al Maste en Python {nombre} !!")
except ValueError:
    print("Introduce los datos correctamente !!")
except Exception as e:
    print("Existe in error ",e)