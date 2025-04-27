class A():
    def __init__(self,x,z):
        self.x = int(x)
        self.z = int(z)
    def incrementaXZ(self):
        self.x+=1
        self.z+=1
    def incrementaZ(self):
        self.z+=1
class B():
    def __init__(self,y,z):
        self.y = int(y)
        self.z = int(z)
    def incrementaYZ(self):
        self.y += 1
        self.z += 1
    def incrementaZ(self):
        self.z += 1
class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)
    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1
    def mostrar(self):
        return self.x, self.y, self.z
objeto=D(x=2, y=4, z=7)
objeto.incrementaXYZ()
print(objeto.mostrar())