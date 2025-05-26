class Artista: 
    def __init__(self, nombre, ci, años_experiencia): 
        self.nombre = nombre 
        self.ci = ci 
        self.años_experiencia = años_experiencia 
 
class Anuncio: 
    def __init__(self, numero, precio): 
        self.numero = numero 
        self.precio = precio 
 
class Obra: 
    def __init__(self, titulo, material, a1, a2, anuncio=None): 
        self.titulo = titulo 
        self.material = material 
        self.a1 = a1  # Artista 1 
        self.a2 = a2  # Artista 2 
        self.anuncio = anuncio  # Anuncio asociado 
 
class Pintura(Obra): 
    def __init__(self, titulo, material, a1, a2, genero, anuncio=None): 
        super().__init__(titulo, material, a1, a2, anuncio) 
        self.genero = genero 
     
    def promedio_experiencia_artistas(self): 
        return (self.a1.años_experiencia + self.a2.años_experiencia) / 2 
     
    def incrementar_precio_anuncio(self, incremento): 
        if self.anuncio: 
            self.anuncio.precio += incremento 
 
artista1 = Artista("Picasso", "1234567", 40) 
artista2 = Artista("Van Gogh", "7654321", 35) 
anuncio1 = Anuncio(1, 500000) 
pintura1 = Pintura("Guernica", "Óleo", artista1, artista2, "Cubismo", anuncio1) 
 
artista3 = Artista("Da Vinci", "9876543", 50) 
artista4 = Artista("Claude Monet", "3456789", 45) 
anuncio2 = Anuncio(2, 750000) 
pintura2 = Pintura("La Gioconda", "Óleo", artista3, artista4, "Renacimiento", anuncio2) 
 
promedio_pintura1 = pintura1.promedio_experiencia_artistas() 
promedio_pintura2 = pintura2.promedio_experiencia_artistas() 
 
print(f"Promedio experiencia pintura 1: {promedio_pintura1} años") 
print(f"Promedio experiencia pintura 2: {promedio_pintura2} años") 
print(f"Promedio general: {(promedio_pintura1 + promedio_pintura2) / 2} años") 
 
def incrementar_precio_por_artista(pintura, nombre_artista, incremento): 
    if pintura.a1.nombre == nombre_artista or pintura.a2.nombre == nombre_artista: 
        pintura.incrementar_precio_anuncio(incremento) 
        print(f"Precio actualizado para {pintura.titulo}: ${pintura.anuncio.precio}") 
    else: 
        print(f"Ningún artista coincide con el nombre {nombre_artista} en {pintura.titulo}") 
 
incrementar_precio_por_artista(pintura1, "Picasso", 100000) 
incrementar_precio_por_artista(pintura2, "Claude Monet", 150000)