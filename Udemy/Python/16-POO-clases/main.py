#definir una clase


class Coche:

    #Atributos
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

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
