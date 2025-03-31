import math
class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    def __mul__(self, escalar):
        return Vector3D(self.x * escalar, self.y * escalar, self.z * escalar)
    def magnitud(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def normalizar(self):
        magnitud = self.magnitud()
        if magnitud == 0:
            raise ValueError("El vector tiene magnitud cero y no puede ser normalizado")
        return Vector3D(self.x / magnitud, self.y / magnitud, self.z / magnitud)
    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

print("coordenadas del primer vector: ")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))

print("\ncoordenadas del segundo vector:")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))

#crearr los vectores para el escalra
a = Vector3D(x1, y1, z1)
b = Vector3D(x2, y2, z2)


print(f"Suma de vectores: {a + b}")
r = float(input("\nIngresar un escalar para multiplicar el primer vector: "))
print(f"Multiplicación por escalar: {a * r}")
print(f"Magnitud del primer vector: {a.magnitud():.2f}")
print(f"Vector normalizado (a): {a.normalizar()}")
print(f"Producto escalar: {a.dot(b):.2f}")
print(f"Producto vectorial: {a.cross(b)}")
