import random
class Juego:
    def __init__(self, numeroDeVidas_inicial):
        self.numeroDeVidas = numeroDeVidas_inicial
        self.record = 0
        self.vidas_inicial = numeroDeVidas_inicial
        self.rango = 10

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

    def validarNumero(self, numero):
        return 0 <= numero <= self.rango

class JuegoAdivinaNumero(Juego):
    def __init__(self, numeroDeVidas_inicial):
        super().__init__(numeroDeVidas_inicial)

    def juega(self):
        super().reinicia_partida()
        self.numeroAAdivinar = random.randint(0, self.rango)
        print(f"Pienso en un numero del 0-{self.rango}, adivina")
        intentos = 0
        while True:
            try:
                intento_usuario = int(input("Introduce tu intento: "))
                if super().validarNumero(intento_usuario):
                    intentos += 1
                    if intento_usuario == self.numeroAAdivinar:
                        print("Felicidades!")
                        super().actualizarRecord(intentos)
                        break
                    else:
                        if super().quita_vidas():
                            if intento_usuario < self.numeroAAdivinar:
                                print("El numero buscado es mayor")
                            else:
                                print("El numero busacado es menor")
                        else:
                            print(f"Estas muerto, el numero era {self.numeroAAdivinar}")
                            break
                else:
                    print(f"El numero debe estar entre 0 y {self.rango}.")
            except ValueError:
                print("Introduce un numero valido")

class JuegoAdivinaPar(JuegoAdivinaNumero):
    def juega(self):
        super().reinicia_partida()
        while True:
            self.numeroAAdivinar = random.randint(0, self.rango)
            if self.numeroAAdivinar % 2 == 0:
                break
        print(f"Pienso en un numero PAR del 0-{self.rango}, adivina")
        intentos = 0
        while True:
            try:
                intento_usuario = int(input("Introduce tu intento: "))
                if super().validarNumero(intento_usuario):
                    if intento_usuario % 2 == 0:
                        intentos += 1
                        if intento_usuario == self.numeroAAdivinar:
                            print("Felicidades!!!")
                            super().actualizarRecord(intentos)
                            break
                        else:
                            if super().quita_vidas():
                                if intento_usuario < self.numeroAAdivinar:
                                    print("El numero buscado es mayor")
                                else:
                                    print("El numero buscado es menor")
                            else:
                                print(f"Moriste, el numero era {self.numeroAAdivinar}")
                                break
                    else:
                        print("¡Debes introducir un numero PAR!")
                else:
                    print(f"El numero debe estar entre 0 y {self.rango}.")
            except ValueError:
                print("Introduce un numero valido")

class JuegoAdivinaImpar(JuegoAdivinaNumero):
    def juega(self):
        super().reinicia_partida()
        while True:
            self.numeroAAdivinar = random.randint(0, self.rango)
            if self.numeroAAdivinar % 2 != 0:
                break
        print(f"Pienso en un numero IMPAR del 0-{self.rango}, adivina")
        intentos = 0
        while True:
            try:
                intento_usuario = int(input("Introduce tu intento: "))
                if super().validarNumero(intento_usuario):
                    if intento_usuario % 2 != 0:
                        intentos += 1
                        if intento_usuario == self.numeroAAdivinar:
                            print("Felicidades!!!")
                            super().actualizarRecord(intentos)
                            break
                        else:
                            if super().quita_vidas():
                                if intento_usuario < self.numeroAAdivinar:
                                    print("El numero buscado es mayor")
                                else:
                                    print("El numero buscado es menor")
                            else:
                                print(f"Moriste, el numero era {self.numeroAAdivinar}")
                                break
                    else:
                        print("¡Debes introducir un numero IMPAR!")
                else:
                    print(f"El numero debe estar entre 0 y {self.rango}.")
            except ValueError:
                print("Introduce un numero valido")

class Aplicacion:
    def main(self):
        vidas_iniciales = 3
        juego_normal = JuegoAdivinaNumero(vidas_iniciales)
        juego_par = JuegoAdivinaPar(vidas_iniciales)
        juego_impar = JuegoAdivinaImpar(vidas_iniciales)

        print("Adivina el numero!!!")
        juego_normal.juega()

        print("Adivina el numero Par!!!")
        juego_par.juega()

        print("Adivina el numero Impar!!!")
        juego_impar.juega()

if __name__ == "__main__":
    aplicacion = Aplicacion()
    aplicacion.main()