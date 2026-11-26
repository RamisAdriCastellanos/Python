#Definir una funció filtrar_paraules() que, donada una llista de paraules i un número x, retorni la llista de paraules que tenen més de x caràcters.
def filtrar_paraules(llista, x):
    paraules_filtrades = []
    for paraula in llista:
        if len(paraula) > x:
            paraules_filtrades.append(paraula)
    return paraules_filtrades