
class Alumno:
    def __init__(self, nombre, registro):
        self.nombre = nombre
        self.registro = registro
        self.edad = None
        self.nota = None

    def Display(self):
        return f"El nombre del alumno: {self.nombre}, con numero de registro: {self.registro}"

    def setAge(self,edad):
        self.edad = edad

    def setNota(self, nota):
        self.nota = nota
    
        