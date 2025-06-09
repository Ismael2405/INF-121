from abc import ABC, abstractmethod
class Vehiculo(ABC):
    @abstractmethod
    def entregar(self):
        pass

class Camion(Vehiculo):
    def entregar(self):
        return "Entrega por tierra en caja grande"

class Barco(Vehiculo):
    def entregar(self):
        return "Entrega por mar en contenedor"

class Logistica(ABC):
    @abstractmethod
    def crear_vehiculo(self) -> Vehiculo:
        pass
    
    def planificar_entrega(self):
        vehiculo = self.crear_vehiculo()
        return f"Planificando: {vehiculo.entregar()}"

class LogisticaTerrestre(Logistica):
    def crear_vehiculo(self) -> Vehiculo:
        return Camion()

class LogisticaMaritima(Logistica):
    def crear_vehiculo(self) -> Vehiculo:
        return Barco()

logistica = LogisticaTerrestre()
print(logistica.planificar_entrega())  

logistica = LogisticaMaritima()
print(logistica.planificar_entrega())  