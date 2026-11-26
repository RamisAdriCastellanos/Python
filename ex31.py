

actual = int(input("Introdueix l'any actual: "))
persones = []
for i in range(4):
    nom = input(f"Introdueix el nom de la persona {i+1}: ")
    naixement = int(input(f"Introdueix l'any de naixement de {nom}: "))
    edat = actual - naixement
    persones.append((nom, edat))

print("\nDades de les persones:")
print("Nom\tEdat")
for nom, edat in persones:
    print(f"{nom}\t{edat}")