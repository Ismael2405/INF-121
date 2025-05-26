class Artista: 
    def __init__(self, nombre, años_experiencia): 
        self.nombre = nombre 
        self.años_experiencia = años_experiencia 
 
class Anuncio: 
    def __init__(self, numero, precio):  
        self.numero = numero 
        self.precio = precio 
    
class Obra: 
    def __init__(self, titulo, material, artista1, artista2, anuncio=None): 
        self.titulo = titulo 
        self.material = material 
        self.artista1 = artista1 
        self.artista2 = artista2 
        self.anuncio = anuncio 
        
    def artista_mas_experiencia(self): 
        if self.artista1.años_experiencia > self.artista2.años_experiencia: 
            return self.artista1 
        return self.artista2 
        
        
    def agregar_anuncio(self, anuncio): 
            self.anuncio = anuncio 
        
    def precio_venta(self): 
        return self.anuncio.precio if self.anuncio else 0 
 
picasso = Artista("Picasso", 50) 
vangogh = Artista("Van Gogh", 20) 
anuncio1 = Anuncio(1, 1000000) 
guernica = Obra("Guernica", "Óleo", picasso, vangogh, anuncio1) 
 
davinci = Artista("Da Vinci", 60) 
michelangelo = Artista("Michelangelo", 55) 
ultima_cena = Obra("La última cena", "Fresco", davinci, michelangelo) 
 
artista1 = guernica.artista_mas_experiencia() 
artista2 = ultima_cena.artista_mas_experiencia() 
 
mas_experiencia = artista1 if artista1.años_experiencia > artista2.años_experiencia else artista2 
print(f"Artista con más experiencia: {mas_experiencia.nombre}") 
 
anuncio2 = Anuncio(2, 2000000) 
ultima_cena.agregar_anuncio(anuncio2) 
 
total_venta = guernica.precio_venta() + ultima_cena.precio_venta() 
print(f"Monto total de venta: ${total_venta}") 
