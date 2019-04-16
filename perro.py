class Perro():
    def __init__(self,n,e,p):
        self.nombre=n
        self.edad=e
        self.peso=p
        
    def ladrar(self):
        if self.peso>=8:
            print("Guau, Guau")
        else:
            print("guau,guau")
            
    def __str__(self):
            return "Soy el Perro {}".format(self.nombre)
    
            
            