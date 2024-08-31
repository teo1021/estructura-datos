def calculo_factorial (numero: int) -> str | int:
    resultado = 1
    if numero < 0:
        return "no se pueden valores negativos"
    for n in range (1, numero+1):
        resultado = resultado*n
        return resultado 
factorial= calculo_factorial(int(input("ingrese un numero: ")))
print("el resultado es: ", factorial)
