from abc import ABC, abstractmethod

class TiendaOnline:
    def __init__(self):
        self._clientes = []
        self._estado = None

    def agregar(self, cliente):
        self._clientes.append(cliente)

    def notificar(self):
        for cliente in self._clientes:
            cliente.actualizar(self._estado)

    def cambiar_estado(self, nuevo_estado):
        print(f"Cambiando estado a: {nuevo_estado}")
        self._estado = nuevo_estado
        self.notificar()

class Cliente(ABC):
    @abstractmethod
    def actualizar(self, estado):
        pass

class ClienteEmail(Cliente):
    def actualizar(self, estado):
        print(f"Email enviado: Producto {estado} disponible")

class ClienteSMS(Cliente):
    def actualizar(self, estado):
        print(f"SMS enviado: ¡Tu producto está {estado}!")

tienda = TiendaOnline()
tienda.agregar(ClienteEmail())
tienda.agregar(ClienteSMS())

tienda.cambiar_estado("en stock")
