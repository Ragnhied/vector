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
        return f"{self.__class__.__name__}({self.x},{self.y},{self.z})" #self.class.name = får tak i navnet på klassen

    def __add__(self,other): #må ikke kalle for self og other, men alle andre gjør det så er lurt.
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __eq__(self, other): #metoden returnerer True hvis self == other
        return self.x == other.x and self.y == other.y and self.z == other.z

    

"""
Forskjell på str og repr: repr bør være litt mer presis enn str-metoden. 
Huskeregel er at x == eval(repr(x)). Den evaluerer en streng som egentlig er kode
Når man implementerer klasser bør man alltid implementere repr, fint når man skal debugge.
Om man ikke implementerer str-metoden, går den automatisk over på repr. 
"""

    
if __name__ == "__main__":
    v = Vector3D(1, 4, 2)
    u = Vector3D(1, 1, 1)
    w = v + u
    w == Vector3D(2, 5, 3)
     