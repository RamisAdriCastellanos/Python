
def gran_llista(llista):
    gran = llista[0]
    for i in llista:
        if i > gran:
            gran = i
    return gran