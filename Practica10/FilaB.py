class Empleado:
    def __init__(self, nombre, ap_paterno, ap_materno, edad, sueldo):
        self.nombre = nombre
        self.ap_paterno = ap_paterno
        self.ap_materno = ap_materno
        self.edad = edad
        self.sueldo = sueldo

    def mostrar(self):
        return f"{self.nombre} {self.ap_paterno} {self.ap_materno} - Edad: {self.edad}, Sueldo: {self.sueldo}"


class Direccion:
    def __init__(self, ciudad, zona, calle, referencia):
        self.ciudad = ciudad
        self.zona = zona
        self.calle = calle
        self.referencia = referencia

    def mostrar(self):
        return f"{self.ciudad}, Zona {self.zona}, Calle {self.calle} ({self.referencia})"


class Ministerio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion  
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def eliminar_por_edad(self, edad_x):
        self.empleados = [e for e in self.empleados if e.edad != edad_x]

    def mostrar_menor_edad(self):
        if not self.empleados:
            print("Sin empleados.")
            return
        menor = min(e.edad for e in self.empleados)
        for e in self.empleados:
            if e.edad == menor:
                print("Menor edad:", e.mostrar())

    def mostrar_menor_sueldo(self):
        if not self.empleados:
            print("Sin empleados.")
            return
        menor = min(e.sueldo for e in self.empleados)
        for e in self.empleados:
            if e.sueldo == menor:
                print("Menor sueldo:", e.mostrar())

    def __add__(self, otro):
        """Transferir el último empleado del segundo ministerio al primero"""
        if otro.empleados:
            e = otro.empleados.pop()
            self.empleados.append(e)
        return self



dir1 = Direccion("La Paz", "Centro", "Camacho", "Frente a plaza")
dir2 = Direccion("El Alto", "16 de Julio", "Av. Naciones Unidas", "Esquina semáforo")

min1 = Ministerio("Ministerio de Transporte", dir1)
min2 = Ministerio("Ministerio de Educación", dir2)

min1.agregar_empleado(Empleado("Pedro", "Rojas", "Luna", 35, 2500))
min1.agregar_empleado(Empleado("Lucy", "Sosa", "Rios", 43, 3250))
min1.agregar_empleado(Empleado("Ana", "Perez", "Rojas", 26, 2700))
min1.agregar_empleado(Empleado("Saul", "Arce", "Calle", 29, 2500))


min1.eliminar_por_edad(26)

min2.agregar_empleado(Empleado("Carlos", "Valdez", "Chavez", 32, 2200))
min1 + min2

min1.mostrar_menor_edad()
min1.mostrar_menor_sueldo()