class Tarea:
    def __init__(self, descripcion:str, prioridad:int, fecha_vencimiento:int):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = fecha_vencimiento
        self.completada = False

    def __str__(self):
        return f"Tarea: {self.descripcion}, Prioridad: {self.prioridad}, Fecha de vencimiento: {self.fecha_vencimiento}, Completada: {self.completada}"

class ListaEnlazada:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, descripcion=None, posicion=None):
        if descripcion:
            for tarea in self.tareas:
                if tarea.descripcion == descripcion:
                    self.tareas.remove(tarea)
                    return
        elif posicion:
            try:
                del self.tareas[posicion - 1]
            except IndexError:
                print("Posición fuera de rango")

    def buscar_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion:
                return tarea
        return None

    def marcar_completada(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        if tarea:
            tarea.completada = True
            self.eliminar_tarea(descripcion)

    def mostrar_tareas(self):
        for tarea in self.tareas:
            print(tarea)

def main():
    gestor_tareas = ListaEnlazada()

    while True:
        print("\nOpciones:")
        print("1. Agregar tarea")
        print("2. Eliminar tarea")
        print("3. Buscar tarea")
        print("4. Marcar tarea como completada")
        print("5. Mostrar tareas")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripcion de la tarea: ")
            prioridad = int(input("Ingrese la prioridad de la tarea (1-3): "))
            fecha_vencimiento = input("Ingrese la fecha limite de entreda de la tarea (DD/MM/AAAA): ")
            tarea = Tarea(descripcion, prioridad, fecha_vencimiento)
            gestor_tareas.agregar_tarea(tarea)
            print("Tarea agregada con éxito!")

        elif opcion == "2":
            descripcion = input("Ingrese la descripcion de la tareaque desea eliminar: ")
            gestor_tareas.eliminar_tarea(descripcion)
            print("Tarea eliminada con exito")

        elif opcion == "3":
            descripcion = input("Ingrese la descripción de la tarea a buscar: ")
            tarea = gestor_tareas.buscar_tarea(descripcion)
            if tarea:
                print(f"Tarea encontrada: {tarea}")
            else:
                print("Tarea no encontrada")

        elif opcion == "4":
            descripcion = input("Ingrese la descripcion de la tarea a marcar como completada: ")
            gestor_tareas.marcar_completada(descripcion)
            print("Tarea completada, felicidades")

        elif opcion == "5":
            print("Tareas:")
            gestor_tareas.mostrar_tareas()

        elif opcion == "6":
            print("Hasta pronto")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()