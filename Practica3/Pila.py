class Pila:
    def __init__(self, n):
        self.arreglo = [0] * n
        self.top = -1
        self.n = n

    def push(self, e):
        if self.isFull():
            print("La pila está llena")
        else:
            self.top += 1
            self.arreglo[self.top] = e

    def pop(self):
        if self.isEmpty():
            print("La pila está vacía")
            return None
        else:
            e = self.arreglo[self.top]
            self.top -= 1
            return e

    def peek(self):
        if self.isEmpty():
            print("La pila está vacía")
            return None
        else:
            return self.arreglo[self.top]

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.n - 1


# Ejemplo de uso
if __name__ == "__main__":
    pila = Pila(5)
    pila.push(10)
    pila.push(20)
    print("Elemento en la cima:", pila.peek())
    print("Eliminar elemento:", pila.pop())
    print("Elemento en la cima:", pila.peek())
