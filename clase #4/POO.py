
#Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; la clase también debe contener dos métodos encender y arrancar. 
#Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado


class Vehiculo:
    def __init__(self, marca: str, combustible: str):
        self.marca = marca 
        self.combustible = combustible
    
    def encender (self):
        pass 
    def arrancar (self):
        pass 
    def __str__(self):
        return f"el vehiculo de marca {self.marca} utiliza gasolina {self.combustible}"
carro= Vehiculo("subaru", "corriente")
print(carro)
print(type(carro))# no es necesario el "type", es solo para ver a que variable pertenece 

print("*"*100)
#Ejercicio 2: Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
#Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado

class Moto (Vehiculo):
    def __init__(self, marca: str, combustible:str):
        super().__init__(marca, combustible)
class Carro (Vehiculo):
    pass

motocicleta = Moto("honda", "corriente")
mi_carro = Carro("mazda", "extra")
print(motocicleta)
print(mi_carro)

print("*"*100)


