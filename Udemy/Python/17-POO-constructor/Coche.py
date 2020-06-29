class Coche:

    #Atributos
    __color = "Rojo"
    __marca = "Ferrari"
    __modelo = "Aventador"
    __velocidad = 300
    __caballaje = 500
    __plazas = 2

    def __init__(self,color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.caballale=caballaje
        self.marca=marca
        self.modelo=modelo
        self.plazas= plazas
        self.velocidad=velocidad

    #metodos
    def setColor(self,color):
        self.color=color
    
    def getColor(self):
        return self.color

    def setVelocidad(self,velocidad):
        self.velocidad=velocidad
    
    def getVelocidad(self):
        return self.velocidad

    def setMarca(self,p_marca):
        self.marca = p_marca

    def getMarca(self):
        return self.marca

    def setModelo(self,p_modelo):
        self.modelo=p_modelo

    def getModelo(self):
        return self.modelo

    def setCaballale(self,p_caballaje):
        self.caballaje= p_caballaje

    def getCaballaje(self):
        return self.caballaje

    def setPlazas(self,p_plazas):
        self.plazas = p_plazas

    def getPlazas(self):
        return self.plazas       

    


    def acelerar(self):
        self.setVelocidad(self.getVelocidad()+1)


    def frenar(self):
        self.setVelocidad(self.getVelocidad()-1)

    def mostrar_todo(self):
        return(f"---Infromación del coche---\nColor: {self.getColor()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}")
