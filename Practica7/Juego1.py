import random
class Juego:
    def __init__(self, numeroDeVidas_inicial):
        self.numeroDeVidas = numeroDeVidas_inicial
        self.record = 0
        self.vidas_inicial = numeroDeVidas_inicial

    def reinicia_partida(self):
        self.numeroDeVidas = self.vidas_inicial
        print("Partida Reiniciada")

    def actualizarRecord(self, intentos):
        if self.record == 0 or intentos < self.record:
            print(f"Nuevo record. Intentos {intentos}")
            self.record = intentos
    def quita_vidas(self):
        self.numeroDeVidas -= 1
        print(f"Te quedan {self.numeroDeVidas} vidas")
        return self.numeroDeVidas > 0

class AdivinaNumero(Juego):
    def __init__(self, numeroDeVidas_inicial):
        super().__init__(numeroDeVidas_inicial)

    def juega(self):
        super().reinicia_partida()
        self.numeroAAdivinar = random.randint(0, 10)
        print("Estoy pensando en un numero del 0-10, adivina")
        intentos = 0
        while True:
            try:
                intento_usuario = int(input("Introduce tu intento: "))
                intentos += 1
                if intento_usuario == self.numeroAAdivinar:
                    print("Felicidades!!!")
                    super().actualizarRecord(intentos)
                    break
                else:
                    if super().quita_vidas():
                        if intento_usuario < self.numeroAAdivinar:
                            print("el numero buscado es mayor")
                        else:
                            print("el numero buscado es menor")
                    else:
                        print(f"Moriste, el numero era: {self.numeroAAdivinar}")
                        break
            except ValueError:
                print("introduce un numero valido")

class Aplicacion:
    def main(self):
        vidas_iniciales = 5
        juego_adivina = AdivinaNumero(vidas_iniciales)
        juego_adivina.juega()

if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.main()