import math
import matplotlib.pyplot as plt

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def coord_cartesianas(self):
        return (self.x, self.y)
    
    def coord_polares(self):
        r = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        return (r, theta)
    
    def __str__(self):
        return f"Punto(x: {self.x}, y: {self.y})"


class Linea:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"Linea[p1: {self.p1}, p2: {self.p2}]"

    def dibuja_linea(self):
        x_values = [self.p1.x, self.p2.x]
        y_values = [self.p1.y, self.p2.y]
        plt.plot(x_values, y_values, 'bo-')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Dibujo de Línea')


class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def __str__(self):
        return f"Circulo[centro: {self.centro}, radio: {self.radio}]"

    def dibuja_circulo(self):
        circle = plt.Circle((self.centro.x, self.centro.y), self.radio, color='r', fill=False)
        plt.gca().add_patch(circle)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Dibujo de Círculo')


# Ejemplo de uso
if __name__ == "__main__":
    # Crear puntos
    p1 = Punto(1, 2)
    p2 = Punto(3, 4)
    
    # Crear y mostrar línea
    linea = Linea(p1, p2)
    print(linea)
    linea.dibuja_linea()
    
    # Crear y mostrar círculo
    centro = Punto(2, 3)
    circulo = Circulo(centro, 1.5)
    print(circulo)
    circulo.dibuja_circulo()

    # Mostrar coordenadas de punto
    print(p1)
    print("Coordenadas Cartesianas:", p1.coord_cartesianas())
    print("Coordenadas Polares:", p1.coord_polares())

    # Configuración de la gráfica
    plt.axis('equal')
    plt.grid(True)
    plt.show()
