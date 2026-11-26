
def nums_que_comencen_per(llista, lletra):
    count = 0
    for nom in llista:
        if nom.lower().startswith(lletra.lower()):
            count += 1
    return count