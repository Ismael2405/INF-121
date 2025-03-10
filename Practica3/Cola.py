class Cola:
    def __init__(self, n):
        self.arreglo = [0] * n
        self.inicio = 0
        self.fin = -1
        self.n = n
        self.numero_elementos = 0

    def insert(self, e):
        if self.isFull():
            print("La cola está llena")
        else:
            self.fin = (self.fin + 1) % self.n
            self.arreglo[self.fin] = e
            self.numero_elementos += 1

    def remove(self):
        if self.isEmpty():
            print("La cola está vacía")
            return None
        else:
            e = self.arreglo[self.inicio]
            self.inicio = (self.inicio + 1) % self.n
            self.numero_elementos -= 1
            return e

    def peek(self):
        if self.isEmpty():
            print("La cola está vacía")
            return None
        else:
            return self.arreglo[self.inicio]

    def isEmpty(self):
        return self.numero_elementos == 0

    def isFull(self):
        return self.numero_elementos == self.n

    def size(self):
        return self.numero_elementos


# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola(5)
    cola.insert(10)
    cola.insert(20)
    print("Elemento en la parte delantera:", cola.peek())
    print("Eliminar elemento:", cola.remove())
    print("Elemento en la parte delantera:", cola.peek())
