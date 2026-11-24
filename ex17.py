
def calcular_longitud(element):
    comptador = 0
    for i in element:
        comptador += 1
    return comptador

cadena = "Hola"
llista = [1, 2, 3, 4, 5]
print("La longitud de la cadena és:", calcular_longitud(cadena))
print("La longitud de la llista és:", calcular_longitud(llista))