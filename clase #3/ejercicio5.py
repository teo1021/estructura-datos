#crear una funcion que genere contraseñas aleatorias, la cantidad de caracteres a generar se envia por parametro
import random
def generar_contrasena(longitud:str) -> str|int:
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud = int(input("¿De cuantos digitos quieres la contraseña?: "))
contraseña = generar_contrasena(longitud)
print("La contraseña generada es:", contraseña)
