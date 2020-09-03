#01.09.20
#fortsettelse på objekt-orientert programmering
#KLASSER I PYTHON

class Vector3D:
    def __init__(self,x,y,z): #init er en konstruktør
        self.x = x #Legger til som atributter på klassen
        self.y = y
        self.z = z
    
    def __str__(self): #for å få finere print. 
        return f"({self.x},{self.y},{self.z})"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y},{self.z})"
    
if __name__ == "__main__":
    v = Vector3D(1, 1, 1)
    print(v)    