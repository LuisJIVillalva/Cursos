import shutil
import os

#crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
else:
    print("El directorio ya existe\n")

"""
#ELIMINAR
os.rmdir('./mi_carpeta')
"""

"""#copiar
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_capeta_COPIADA"

shutil.copytree(ruta_original,ruta_nueva)

os.rmdir('./mi_capeta_COPIADA')

"""
import pathlib
ruta= str(pathlib.Path().absolute())+"/fichero_texto.txt"
ruta2= str(pathlib.Path().absolute())+"/mi_carpeta/fichero_textoCopiado"
shutil.copyfile(ruta,ruta2+"2.txt")
shutil.copyfile(ruta,ruta2+"3.txt")
shutil.copyfile(ruta,ruta2+"4.txt")
shutil.copyfile(ruta,ruta2+"5.txt")
shutil.copyfile(ruta,ruta2+"6.txt")

print("Contenido de mi_carpeta")
contenido= os.listdir("./mi_carpeta")

for fichero in contenido:
    print(f"fichero: {fichero}")