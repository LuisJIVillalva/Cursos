class Persona:

    def __init__ (self, p_nombre, p_apellido, p_altura, p_edad):
        self.nombre=p_nombre
        self.apellido=p_apellido
        self.altura=p_altura
        self.edad = p_edad

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getAltura(self):
        return self.altura
    
    def getEdad(self):
        return self.edad

    def setNombre(self,p_nombre):
        self.nombre= p_nombre

    def setApellido(self,p_apellido):
        self.apellido=p_apellido

    def setAltura(self,p_altura):
        self.altura=p_altura

    def setEdad(self,p_adad):
        self.edad=p_adad


class Informatico(Persona):
    

    def __init__ (self,p_nombre, p_apellido, p_altura, p_edad,p_lenguaje,p_experiencia):
        Persona.__init__(self,p_nombre,p_apellido,p_altura,p_edad)
        self.lenguajes= p_lenguaje
        self.experiencia = p_experiencia

    def getLenguajes(self):
        return self.lenguajes

    def setLenguaje(self,p_lenguaje):
        self.lenguajes=p_lenguaje
    
    def aprender(self,p_lenguaje):
        self.setLenguaje(self.getLenguajes()+f", {p_lenguaje}")
