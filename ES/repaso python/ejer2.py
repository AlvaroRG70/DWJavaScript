class Persona:
    
    def __init__(self,nom,ap,ed):
        self.nombre = nom
        self.apellido = ap
        self.edad = ed
        
    def __str__(self):
        return "Nombre: {} \nApellidos: {}\nEdad:{}".format(self.nombre, self.apellido, self.edad)