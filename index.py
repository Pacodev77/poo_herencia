# POO La Herencia

class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas # Argumento Restringido
        self.color = color
        self.precio = precio 

# Clase que Hereda
class Moto(Fabrica):
    def cantidad(self):
        print("Objeto: Moto")
        print(f"Cantindad de llantas: {self._llantas}\nColor: {self.color}\nPrecio: {self.precio}\n")

class Carro(Fabrica):
    def cantidad(self):
        print("Objeto: Carro")
        print(f"Cantindad de llantas: {self._llantas}\nColor: {self.color}\nPrecio: {self.precio}\n")

# Crear Objetos
moto1 = Moto(2, "Rojo", 23000)
moto1.cantidad()
carro1 = Carro(4, "Negro", 85000)
carro1.cantidad()




    
    















