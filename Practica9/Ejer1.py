class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0
    def __str__(self):
        return f"Numero: {self.numero}, Precio: {self.precio}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 50.0
        else:
            self.precio = 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 25.0
        else:
            self.precio = 30.0
def main():
    while True:
        print("\n1. Compra Boleto")
        print("2. Salir")
        opcion = input("Seleccione una opción del menú: ")

        if opcion == '1':
            tipo = input("Ingrese tipo de boleto (palco/platea/galeria): ").lower()
            numero = int(input("Ingrese número de boleto: "))

            if tipo == 'palco':
                boleto = Palco(numero)

            elif tipo == 'platea':
                dias = int(input("Ingresa días de anticipación: "))
                boleto = Platea(numero, dias)

            elif tipo == 'galeria':
                dias = int(input("Ingresa días de anticipación: "))
                boleto = Galeria(numero, dias)

            else:
                print("Boleto no válido.")
                continue
            print(boleto)

        elif opcion == '2':
            print("Bye Byeee")
            break
        else:
            print("Del Menuuuuú te dije")

if __name__ == "__main__":
    main()
