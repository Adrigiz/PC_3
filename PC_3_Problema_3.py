import math

class Circulo:

    def __init__(self, radio):
        self.radio = int(radio)
        
    def area(self):
        
        area = (math.pi)*self.radio**2
        return area

radio = input("Ingrese el radio:")

circulo = Circulo(radio)
area_circulo = circulo.area()
print(f"El area del circulo de radio {radio} es {area_circulo}")