
def paraula_mes_llarga(llista):
    paraula = llista[0]
    for i in llista:
        if len(i) > len(paraula):
            paraula = i
    return paraula