# crear un arreglo con 10 numeros aleatorios e imprimir en pantalla el promedio de estos numeros
import random 
numero = [random.randint(1,100)for _ in range(10)]
promedio = sum(numero)/len(numero)
print ("numeros aleatorio: ", numero)
print ("el promedio de los datos generados es: ",promedio)


