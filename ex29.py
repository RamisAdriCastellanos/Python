#Definir una funció que donada una cadena, avaluï quantes lletres majúscules hi ha.
def comptar_majusculas(cadena):
    comptador = 0
    for caracter in cadena:
        if caracter.isupper():
            comptador += 1
    return comptador