class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad

def planificacion_prioridad(tareas):
    tareas.sort(key=lambda x: x.prioridad, reverse=True)
    programa = []
    tiempo_espera = 0
    tiempo_espera_total = 0
    tiempo_retorno_total = 0

    for tarea in tareas:
        programa.append(tarea.nombre)
        tiempo_espera_total += tiempo_espera
        tiempo_espera += 1 
        tiempo_retorno_total += tiempo_espera

    tiempo_espera_promedio = tiempo_espera_total / len(tareas)
    tiempo_retorno_promedio = tiempo_retorno_total / len(tareas)

    return programa, tiempo_espera_promedio, tiempo_retorno_promedio


num_tareas = int(input("Ingresa el número de tareas: "))
tareas = []

for i in range(num_tareas):
    nombre = input(f"Ingresa el nombre de la tarea {i + 1}: ")
    prioridad = int(input(f"Ingresa la prioridad de la tarea {i + 1}: "))
    tareas.append(Tarea(nombre, prioridad))

programa, tiempo_espera_promedio, tiempo_retorno_promedio = planificacion_prioridad(tareas)

print("Programa:", programa)
print("Tiempo de Espera Promedio:", tiempo_espera_promedio)
print("Tiempo de Retorno Promedio:", tiempo_retorno_promedio)