import math
def calcular_area(figura, *args):
    if figura == "circulo":
        if len(args) == 1:
            radio = args[0]
            return math.pi * radio**2
        else:
            return "Error"
    
    elif figura == "rectangulo":
        if len(args) == 2:
            base, altura = args
            return base * altura
        else:
            return "Error"
    
    elif figura == "triangulo":
        if len(args) == 2:
            base, altura = args
            return (base * altura) / 2
        else:
            return "Error"
    
    elif figura == "trapecio":
        if len(args) == 3:
            base_mayor, base_menor, altura = args
            return ((base_mayor + base_menor) * altura) / 2
        else:
            return "Error"
    
    elif figura == "pentagono":
        if len(args) == 2:
            lado, apotema = args
            return (5 * lado * apotema) / 2
        else:
            return "Error"
    
    else:
        return "No existe."

figura = input("Introduce la figura geométrica (circulo, rectangulo, triangulo, trapecio, pentagono): ").lower()

if figura == "circulo":
    radio = float(input("Introduce el radio: "))
    print(f"El área del {figura} es: {calcular_area(figura, radio):.2f}")
elif figura in ["rectangulo", "triangulo"]:
    base = float(input("Introduce la base: "))
    altura = float(input("Introduce la altura: "))
    print(f"El área del {figura} es: {calcular_area(figura, base, altura):.2f}")
elif figura == "trapecio":
    base_mayor = float(input("Introduce la base mayor: "))
    base_menor = float(input("Introduce la base menor: "))
    altura = float(input("Introduce la altura: "))
    print(f"El área del trapecio es: {calcular_area(figura, base_mayor, base_menor, altura):.2f}")
elif figura == "pentagono":
    lado = float(input("Introduce el lado: "))
    apotema = float(input("Introduce la apotema: "))
    print(f"El área del pentágono es: {calcular_area(figura, lado, apotema):.2f}")
else:
    print("No existe")
