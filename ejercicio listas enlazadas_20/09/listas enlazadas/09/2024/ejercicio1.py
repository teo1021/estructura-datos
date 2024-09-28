class Animal:
    def __init__(self, nombre, tipo, edad):
        self.nombre = nombre
        self.tipo = tipo
        self.edad = edad
        self.siguiente = None  

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Edad: {self.edad} años"


class ListaEnlazadaAnimales:
    def __init__(self):
        self.cabeza = None

    def agregar_animal(self, nuevo_animal):
        if self.cabeza is None:
            self.cabeza = nuevo_animal
        else:
            actual = self.cabeza
            while actual.siguiente:
                if actual.nombre == nuevo_animal.nombre: 
                    print(f"El animal {nuevo_animal.nombre} ya está en la lista.")
                    return
                actual = actual.siguiente
            if actual.nombre == nuevo_animal.nombre:
                print(f"El animal {nuevo_animal.nombre} ya está en la lista.")
                return
            actual.siguiente = nuevo_animal
        print(f"Animal {nuevo_animal.nombre} agregado con éxito.")

    
    def mostrar_en_bucle(self):
        actual = self.cabeza
        if actual is None:
            print("La lista de animales está vacía.")
            return
        while actual:
            print(actual)
            actual = actual.siguiente

  
    def mostrar_en_recursion(self, nodo=None):
        if nodo is None:
            nodo = self.cabeza
            if nodo is None:
                print("La lista de animales está vacía.")
                return
        print(nodo)
        if nodo.siguiente:
            self.mostrar_en_recursion(nodo.siguiente)


def menu_interactivo():
    lista_animales = ListaEnlazadaAnimales()

    while True:
        print("\n--- Menú de Gestión del Zoológico ---")
        print("1. Agregar un nuevo animal")
        print("2. Mostrar animales usando bucle")
        print("3. Mostrar animales usando recursión")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del animal: ")
            tipo = input("¿que tipo de animal es?: ")
            try:
                edad = int(input("Ingrese la edad del animal en años: "))
            except ValueError:
                print("Por favor ingrese un numero para la edad.")
                continue

            nuevo_animal = Animal(nombre, tipo, edad)
            lista_animales.agregar_animal(nuevo_animal)

        elif opcion == '2':
            print("\nAnimales en la lista (bucle):")
            lista_animales.mostrar_en_bucle()

        elif opcion == '3':
            print("\nAnimales en la lista (recursión):")
            lista_animales.mostrar_en_recursion()

        elif opcion == '4':
            print("hasta la proxima.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


menu_interactivo()
