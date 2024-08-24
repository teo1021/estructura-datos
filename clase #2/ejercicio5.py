#calcular la factorial de un numer dado 
def factorial(n):
    resultados = []
    resultado = 1
    for i in range(1,n + 1):
        resultado *= i
        resultados.append(resultados)
    return resultados, resultados

