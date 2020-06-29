lista=["hola",1,1.0,True,["lista",7]]

def consultar_tipo(elemento):
        result=f"Este dato es del tipo {type(elemento)}"
        return result


for elemento in lista:
    print(consultar_tipo(elemento))