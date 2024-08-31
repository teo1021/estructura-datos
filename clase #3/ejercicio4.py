# verificar si una palabra dada es un palindromo
def es_palindromo(texto:str) -> str:
    texto_libre = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_libre == texto_libre[::-1]

texto = input("Ingresa una palabra o frase para verificar si es un palindromo: ")
if es_palindromo(texto):
    print(f'{texto} es un palindromo.')
else:
    print(f'{texto} no es un palindromo.')