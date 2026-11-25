
def superposicio(llista1, llista2):
    for element in llista1:
        if element in llista2:
            return True
    return False