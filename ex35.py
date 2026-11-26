
def comptar_vocals(palabra):
    # Crear un diccionari per emmagatzemar el recompte de vocals
    recompte = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    # Convertir la paraula a minúscules per evitar problemes amb majúscules
    palabra = palabra.lower()
    
    # Iterar sobre cada lletra de la paraula
    for lletra in palabra:
        # Comprovar si la lletra és una vocal i incrementar el seu recompte
        if lletra in recompte:
            recompte[lletra] += 1
            
    return recompte