# creaqr un sistema de control de ingreso para evitar el sobre cupo
# definir cual va a ser el numero a controlar
# antes de pedir el ingreso debe solicitar el boleto de entrada, y si e boleto no es valido mostrar el mensaje "acceso denegado", de lo contrario
# dejar entrar y contar el cupo
control=0
cupo = int(input("ingrese cupo:"))
while control < cupo:
    valido = input("voleto valido?: ")
    if valido == "si":
        print("puede ingresar")
        control = control+1
        print("numero de boletos: ",control)
    else:
        print("no puede ingresar")
print("cupos agotados")