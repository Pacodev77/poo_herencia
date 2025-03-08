class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    # Clase Moto Hereda clase Fabrica
class Moto(Fabrica):
    def cantidad(self):
        print(f"\nCantidad de llantas: {self._llantas}\nColor: {self._color}\nPrC: {self._precio}\n")

    def __str__(self):
        return f"Moto: {self._color}, {self._llantas} Llantas, ${self._precio}"

    # Clase Carro Hereda clase Fabrica
class Carro(Fabrica):
    def cantidad(self):
        print(f"Cantidad de llantas: {self._llantas}\nColor es: {self._color}\nPrecio es: {self._precio}\n")
    def __str__(self):
        return f"Carro: {self._color}, {self._llantas} Llantas, ${self._precio}"

# Crear Objetos
moto = Moto(2, "Rojo", 16000)
moto.cantidad()
carro = Carro(4, "Negro", 80000)
carro.cantidad()

objetos = [moto, carro]

for objeto in objetos:
    print("-" * 20)
    print(objeto)
    print("-" * 20)
