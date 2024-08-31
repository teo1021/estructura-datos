#crear una funcion que combierta temperatura de celsius a fahrenheit
def celcius_fahrenheit(celcius:int) -> int: 
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit 

temperatura_celcius = float(input("ingrese la temperatura en grados celcius: "))
temperatura_fahrenheit = celcius_fahrenheit(temperatura_celcius)
print(f"{temperatura_celcius} grados Celsius son {temperatura_fahrenheit:.2f} grados Fahrenheit.")
