import math

class AlgebraVectorial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def magnitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __add__(self, other):
        return AlgebraVectorial(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return AlgebraVectorial(self.x - other.x, self.y - other.y)
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    def cross(self, other):
        return self.x * other.y - self.y * other.x
    def proyeccion(self, other):
        factor = self.dot(other) / (other.magnitud() ** 2)
        return AlgebraVectorial(factor * other.x, factor * other.y)
    def es_perpendicular(self, other):
        return self.dot(other) == 0
    def es_paralelo(self, other):
        return self.cross(other) == 0

print("Ingresa tus coordenadas del primer vector:")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
print("\nIngresa tus coordenadas del segundo vector:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))

a = AlgebraVectorial(x1, y1)
b = AlgebraVectorial(x2, y2)

print("son paralelos", a.es_paralelo(b))
print("son perpendiculares", a.es_perpendicular(b))
proyeccion = a.proyeccion(b)
print(f"Proyección de a sobre b: ({proyeccion.x:.2f}, {proyeccion.y:.2f})")
