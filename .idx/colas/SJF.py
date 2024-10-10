class Tarea:
    def __init__(self, nombre, tiempo_rafaga):
        self.nombre = nombre
        self.tiempo_rafaga = tiempo_rafaga

def sjf(tareas):
    tareas.sort(key=lambda x: x.tiempo_rafaga)
    programa = []
    tiempo_espera = 0
    tiempo_espera_total = 0
    tiempo_retorno_total = 0

    for tarea in tareas:
        programa.append(tarea.nombre)
        tiempo_espera_total += tiempo_espera
        tiempo_espera += tarea.tiempo_rafaga
        tiempo_retorno_total += tiempo_espera

    tiempo_espera_promedio = tiempo_espera_total / len(tareas)
    tiempo_retorno_promedio = tiempo_retorno_total / len(tareas)

    return programa, tiempo_espera_promedio, tiempo_retorno_promedio


num_tareas = int(input("Ingresa el número de tareas: "))
tareas = []

for i in range(num_tareas):
    nombre = input(f"Ingresa el nombre de la tarea {i + 1}: ")
    tiempo_rafaga = int(input(f"Ingresa el tiempo de ráfaga de la tarea {i + 1}: "))
    tareas.append(Tarea(nombre, tiempo_rafaga))

programa, tiempo_espera_promedio, tiempo_retorno_promedio = sjf(tareas)

print("...:", programa)
print("Tiempo de Espera Promedio:", tiempo_espera_promedio)
print("Tiempo de Retorno Promedio:", tiempo_retorno_promedio)