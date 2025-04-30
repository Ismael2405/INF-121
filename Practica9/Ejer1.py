import tkinter as tk
from tkinter import ttk, messagebox

class Boleto:
    def __init__(self, numero):
        self.numero = numero
        self.precio = 0.0
    def __str__(self):
        return f"Número: {self.numero}, Precio: {self.precio}"

class Palco(Boleto):
    def __init__(self, numero):
        super().__init__(numero)
        self.precio = 100.0

class Platea(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 50.0
        else:
            self.precio = 60.0

class Galeria(Boleto):
    def __init__(self, numero, dias_anticipacion):
        super().__init__(numero)
        if dias_anticipacion >= 10:
            self.precio = 25.0
        else:
            self.precio = 30.0

class AppBoletos:
    def __init__(self, master):
        self.master = master
        master.title("Compra de Boletos")

        self.tipo_boleto = tk.StringVar()
        self.tipo_boleto.set("palco")  # Valor por defecto

        self.numero_boleto = tk.StringVar()
        self.dias_anticipacion = tk.StringVar()

        ttk.Label(master, text="Tipo de Boleto:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(master, text="Palco", variable=self.tipo_boleto, value="palco").grid(row=0, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(master, text="Platea", variable=self.tipo_boleto, value="platea").grid(row=1, column=1, padx=5, pady=5, sticky="w")
        ttk.Radiobutton(master, text="Galería", variable=self.tipo_boleto, value="galeria").grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(master, text="Número de Boleto:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(master, textvariable=self.numero_boleto).grid(row=3, column=1, padx=5, pady=5, sticky="ew")

        self.label_dias = ttk.Label(master, text="Días de Anticipación:")
        self.entry_dias = ttk.Entry(master, textvariable=self.dias_anticipacion)

        ttk.Button(master, text="Comprar Boleto", command=self.comprar_boleto).grid(row=5, column=0, columnspan=2, pady=10)

        self.resultado_label = ttk.Label(master, text="")
        self.resultado_label.grid(row=6, column=0, columnspan=2, pady=5)

        # Ocultar inicialmente los campos de días de anticipación
        self.label_dias.grid_forget()
        self.entry_dias.grid_forget()

        # Configurar el comportamiento al cambiar el tipo de boleto
        for radio in master.winfo_children():
            if isinstance(radio, ttk.Radiobutton):
                radio.config(command=self.mostrar_ocultar_dias)

    def mostrar_ocultar_dias(self):
        tipo = self.tipo_boleto.get()
        if tipo in ['platea', 'galeria']:
            self.label_dias.grid(row=4, column=0, padx=5, pady=5, sticky="w")
            self.entry_dias.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        else:
            self.label_dias.grid_forget()
            self.entry_dias.grid_forget()
            self.dias_anticipacion.set("") # Limpiar el campo si se oculta

    def comprar_boleto(self):
        tipo = self.tipo_boleto.get()
        try:
            numero = int(self.numero_boleto.get())
            boleto = None
            if tipo == 'palco':
                boleto = Palco(numero)
            elif tipo == 'platea':
                dias = int(self.dias_anticipacion.get())
                boleto = Platea(numero, dias)
            elif tipo == 'galeria':
                dias = int(self.dias_anticipacion.get())
                boleto = Galeria(numero, dias)
            else:
                messagebox.showerror("Error", "Tipo de boleto no válido.")
                return

            if boleto:
                self.resultado_label.config(text=str(boleto))
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese un número válido para el boleto y los días de anticipación.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppBoletos(root)
    root.mainloop()
