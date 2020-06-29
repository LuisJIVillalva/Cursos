import os
opcion="S"

while opcion != "N":
    os.system('cls')
    frase = input("Ingrese frase: ").strip()
    if frase == "":
        print("Solo ingreso espacios\n")
    else:
        print(f"La frase ingresada es:\n{frase.upper()}")
    opcion=input("Seguirá ingresando frases? S-si N-no").upper()
