class SistemaLegado:
    def realizar_pago(self, cantidad: float) -> str:
        return f"Pago legado: ${cantidad} procesados"

class NuevoSistemaPago:
    def pagar(self, monto: float) -> str:
        return f"Pago nuevo: ${monto} aprobado"

class AdaptadorPago(NuevoSistemaPago):
    def __init__(self, sistema_legado: SistemaLegado):
        self._sistema_legado = sistema_legado

    def pagar(self, monto: float) -> str:
        return self._sistema_legado.realizar_pago(monto)

def procesar_pago(sistema: NuevoSistemaPago, monto: float):
    print(sistema.pagar(monto))

legado = SistemaLegado()
adaptador = AdaptadorPago(legado)

procesar_pago(NuevoSistemaPago(), 100.0)  
procesar_pago(adaptador, 200.0)          