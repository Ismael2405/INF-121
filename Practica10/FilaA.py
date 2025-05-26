class LineaTeleferico:
    def __init__(self, color, tramo, nroCabinas):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.empleados = []
        self.edades = []
        self.sueldos = []

    def agregar_empleado(self, nombre, ap_paterno, ap_materno, edad, sueldo):
        self.empleados.append((nombre, ap_paterno, ap_materno))
        self.edades.append(edad)
        self.sueldos.append(sueldo)

    def eliminar_por_apellido(self, apellido):
        nuevos_empleados = []
        nuevas_edades = []
        nuevos_sueldos = []

        for i, (nom, ap_p, ap_m) in enumerate(self.empleados):
            if ap_p != apellido and ap_m != apellido:
                nuevos_empleados.append((nom, ap_p, ap_m))
                nuevas_edades.append(self.edades[i])
                nuevos_sueldos.append(self.sueldos[i])

        self.empleados = nuevos_empleados
        self.edades = nuevas_edades
        self.sueldos = nuevos_sueldos

    def mostrar_mayor_edad(self):
        if not self.edades:
            print("No hay empleados.")
            return
        mayor = max(self.edades)
        print("Empleado(s) con mayor edad:")
        for i, edad in enumerate(self.edades):
            if edad == mayor:
                print(f"{self.empleados[i]} - Edad: {edad}")

    def mostrar_mayor_sueldo(self):
        if not self.sueldos:
            print("No hay empleados.")
            return
        mayor = max(self.sueldos)
        print("Empleado(s) con mayor sueldo:")
        for i, sueldo in enumerate(self.sueldos):
            if sueldo == mayor:
                print(f"{self.empleados[i]} - Sueldo: {sueldo}")

    def __add__(self, otro):
        """Transferir el último empleado al otro objeto"""
        if self.empleados:
            empleado = self.empleados.pop()
            edad = self.edades.pop()
            sueldo = self.sueldos.pop()

            otro.empleados.append(empleado)
            otro.edades.append(edad)
            otro.sueldos.append(sueldo)
        return otro

linea1 = LineaTeleferico("Rojo", "Estación Central - 16 de Julio", 20)
linea2 = LineaTeleferico("Verde", "Irpavi - Del Libertador", 18)

linea1.agregar_empleado("Pedro", "Rojas", "Luna", 35, 2500)
linea1.agregar_empleado("Lucy", "Sosa", "Rios", 43, 3250)
linea1.agregar_empleado("Ana", "Perez", "Rojas", 26, 2700)
linea1.agregar_empleado("Saul", "Arce", "Calle", 29, 2500)

linea1.eliminar_por_apellido("Rojas")  
linea1 + linea2

linea1.mostrar_mayor_edad()
linea1.mostrar_mayor_sueldo()