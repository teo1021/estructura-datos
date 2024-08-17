peso = float(input("ingrese su peso: "))
altura = float(input("ingrese su altura: "))
imc = peso / (altura * altura)
print("su imc es: ",imc)
if imc < 18.5:
    print("usted tiene bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("usted tiene peso normal")
else:
    print("usted tiene sobrepeso")

