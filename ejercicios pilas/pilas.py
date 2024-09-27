def agregar_elemento(pila, tope, n):
    if verificar_llena(pila, tope, n):
        print("Desbordamiento - Pila llena")
    else:
        dato = int(input("Coloque dato NUMÉRICO a insertar: "))
        tope += 1
        pila[tope] = dato
    return tope

def eliminar_elemento(pila, tope):
    if verificar_vacia(pila, tope):
        print("Subdesbordamiento - Pila vacía")
    else:
        pila[tope] = 0  # Limpiar el valor
        tope -= 1
    return tope

def mostrar_elementos(pila, n):
    print("La pila tiene los siguientes elementos actualmente:")
    for i in range(n, 0, -1):
        print(f"Posición {i}: {pila[i]}")

def verificar_estado(pila, tope):
    return tope == 0

def verificar_llena(pila, tope, n):
    return tope == n

def verificar_vacia(tope):
    return tope == 0

def main():
    n = int(input("Ingrese el tamaño de la pila: "))
    pila = [0] * (n + 1)  # Inicializa la pila con ceros
    tope = 0
    seleccion = -1

    while seleccion != 0:
        print("Seleccione una opción para la pila")
        print("--------------------------------")
        print("1. Agregar elemento")
        print("2. Eliminar elemento")
        print("3. Mostrar elementos")
        print("4. Verificar estado de la pila")
        seleccion = int(input())

        if seleccion == 1:
            tope = agregar_elemento(pila, tope, n)
        elif seleccion == 2:
            tope = eliminar_elemento(pila, tope)
        elif seleccion == 3:
            mostrar_elementos(pila, n)
        elif seleccion == 4:
            if verificar_estado(pila, tope):
                print("La pila está vacía")
            else:
                print("La pila no está vacía")
        
        print("")  

if __name__ == "__main__":
    main()


# Ahora hecho en Pseint (pseudocodigo)

"""
Algoritmo PilaDinamica
    
    Definir pila como entero; 
    Definir tope como entero; 
    Definir seleccion como entero; 
    Definir dato como entero; 
    Definir band como logico; 
    Definir n como entero; 
	
    Escribir "Ingrese el tamaño de la pila: ";
    Leer n;
	
    Dimension pila[n+1]; 
	
    tope <- 0  
    band = Falso;
    dato = 0; 
	
    Repetir 
        Escribir "Seleccione una opción para la pila";
        Escribir "-----------------------------";
        Escribir "1. Agregar elemento";
        Escribir "2. Eliminar elemento";
        Escribir "3. Mostrar elementos";
        Escribir "4. Verificar estado de la pila";
        Leer seleccion; 
        Segun seleccion Hacer 
            1:
                tope = agregarElemento(pila,tope,n,dato); 
            2: 
                tope = eliminarElemento(pila, tope,n); 
            3: 
                mostrarElementos(pila,n); 
            4:
                band = verificarEstado(pila,tope,n); 
                Si (band=Verdadero) Entonces 
                    Escribir "La pila está vacía";
                Sino 
                    Escribir "La pila no está vacía";
                FinSi
        Fin Segun
        Escribir "                                         ";
		Hasta Que(seleccion = 0) 
		
FinAlgoritmo

Funcion tope <- agregarElemento(pila,tope,n,dato) 
    band = verificarLlena(pila,tope,n); 
    Si(band=Verdadero) Entonces 
        Escribir "Desbordamiento - Pila llena";
    Sino 
        Escribir Sin Saltar "Coloque dato NUMÉRICO a insertar "; Leer dato; 
        pila[tope+1] = dato; 
        tope <- tope + 1; 
    FinSi
FinFuncion

Funcion tope <- eliminarElemento(pila, tope,n) 
    band = verificarVacia(pila,tope); 
    Si(band=Verdadero) Entonces 
        Escribir "Subdesbordamiento - Pila vacía";
    Sino
        tope <- tope-1; 
        pila[tope+1] = 0; 
    FinSi
FinFuncion

Funcion mostrarElementos(pila,n)
    Escribir "La pila tiene los siguientes elementos actualmente: ";
    Para i <- n Hasta 1 Con Paso -1 Hacer
        Escribir "Posición ", i, ": ", pila[i];
    FinPara
FinFuncion

Funcion band <- verificarEstado(pila,tope,n) 
    Si(tope=0) Entonces 
        band <- Verdadero 
    Sino
        band <- Falso; 
    FinSi
FinFuncion

Funcion band <- verificarLlena(pila,tope,n)  
    Si(tope=n) Entonces 
        band <- Verdadero; 
    Sino 
        band <- Falso; 
    FinSi
FinFuncion

Funcion band <- verificarVacia(pila,tope) 
    Si(tope=0) Entonces 
        band <- Verdadero 
    Sino
        band <- Falso; 
    FinSi
FinFuncion
.
"""