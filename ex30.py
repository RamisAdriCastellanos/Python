#Escriure un programa que converteixi el números binaris en enters.
def binari_a_enter(binari):
    enter = 0
    for i in range(len(binari)):
        enter += int(binari[-(i + 1)]) * (2 ** i)
    return enter