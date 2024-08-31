#crear una funcinon que realice operaciones basicas entre dos numeros
def operaciones_basicas(num1:int, num2:int, operacion:str) -> int|str:
   
    if operacion == 'suma':
        return num1 + num2
    elif operacion == 'resta':
        return num1 - num2
    elif operacion == 'mult':
        return num1 * num2
    elif operacion == 'div':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

def main():
    try:
        num1 = float(input("ingrese un numero: "))
        num2 = float(input("ingrese otro numero: "))
        operacion = input("Ingresa la operación ('suma', 'resta', 'mult', 'div'): ").strip().lower()
        
        resultado = operaciones_basicas(num1, num2, operacion)
        print("El resultado de la operación es: ",resultado)
    except ValueError:
        print("Error: Entrada no válida. Asegúrate de ingresar números válidos.")

if __name__ == "__main__":
    main()