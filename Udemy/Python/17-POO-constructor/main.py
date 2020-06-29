from Coche import Coche

carro = Coche("Rojo","Fiat","Uno",200,100,2)

print(carro.mostrar_todo())

#detectar tipado

if type(carro) == Coche:
    print("Es un Carro")
else:
    print("No es un Obejeto")

