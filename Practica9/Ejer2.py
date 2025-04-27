import math
import random
from abc import ABC, abstractmethod
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass

class Figura(ABC):
    def __init__(self, color):
        self.color = color
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def __str__(self):
        return f"Color: {self.color}"
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass

class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="Rojo"):
        super().__init__(color)
        self.lado = lado
    def area(self):
        return self.lado * self.lado
    def perimetro(self):
        return 4 * self.lado
    def comoColorear(self):
        return "Colorear los cuatro lados."


class Circulo(Figura):
    def __init__(self, radio, color="Azul"):
        super().__init__(color)
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio

def main():
    figuras = []
    for _ in range(5):
        tipo = random.randint(1, 2) 
        if tipo == 1:
            lado = random.randint(1, 10)
            figura = Cuadrado(lado)
        else:
            radio = random.randint(1, 10)
            figura = Circulo(radio)

        figuras.append(figura)
    for figura in figuras:
        print(f"\n{figura}")
        print(f"Área: {figura.area():.2f}")
        print(f"Perímetro: {figura.perimetro():.2f}")

        if isinstance(figura, Coloreado):
            print(f"Cómo colorear: {figura.comoColorear()}")

if __name__ == "__main__":
    main()