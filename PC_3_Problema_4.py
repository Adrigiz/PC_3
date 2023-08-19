class Rectangulo:
    def __init__(self, largo, ancho) :
        self.largo = int(largo)
        self.ancho = int(ancho)

    def area(self):
        area = self.largo*self.ancho
        return area
    

largo = input("Ingrese su largo: ")
ancho = input("Ingrese su ancho")
rectangulo = Rectangulo(largo, ancho)
area_rectangulo = rectangulo.area()
print(f"El area del rectangulo de largo y ancho {largo} y {ancho}, es {area_rectangulo}  ")