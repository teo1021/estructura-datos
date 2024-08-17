numero_1 = int(input("ingrese un numero: "))
numero_2 = int(input("ingrese otro numero: "))
numero_3 = int(input("ingrese otro numero: "))

if numero_1 > numero_2:
    if numero_1 > numero_3:
        print("el numero mayor es: ",numero_1)
    else:
        print("el numero mayor es: ",numero_3)

else: 
    if numero_2 > numero_3:
        print("el numero mayor es: ", numero_2)
    else:
        print("el numero mayor es: ", numero_3)  

if numero_1 < numero_2:
    if numero_1 < numero_3:
        print("el numero menor es: ",numero_1)
    else:
        print("el numero menor es: ",numero_3)

else: 
    if numero_2 < numero_3:
        print("el numero menor es: ",numero_2)
    else:
        print("el numero menor es: ",numero_3)  
              




