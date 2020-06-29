from io import open
import pathlib
import shutil

#Abrir achivo
ruta =str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

archivo.write("***********Texto desde Python*************\n")
archivo.close()

ruta =str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta,"r")

#Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

#leer contenido y guardarlo en una lista

lista = archivo_lectura.readline()
archivo_lectura.close()

for frase in lista:
    print("_ "+frase.center(100))
"""
#Copiar Archivos

ruta_original =str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva =str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"

shutil.copyfile(ruta_original,ruta_nueva)

#mover
ruta_original =str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
ruta_nueva =str(pathlib.Path().absolute()) + "/fichero_texto_copiado_nuevo.txt"
shutil.move(ruta_original,ruta_nueva)


#eliminar
import os
ruta_nueva =str(pathlib.Path().absolute()) + "/fichero_texto_copiado_nuevo.txt"
os.remove(ruta_nueva)
"""
#comprobar si existe
import os.path
ruta_comprobar = os.path.abspath("./")+"/fichero_texto.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")