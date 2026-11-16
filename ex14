
x = int(input("Quina operació vols fer? (1: suma, 2: resta, 3: multiplicació, 4: divisió, 5: canvi de base): "))

if x == 1:
    a = int(input("Introdueix el primer número: "))
    b = int(input("Introdueix el segon número: "))
    print("El resultat de la suma és:", a + b)

elif x == 2:
    a = int(input("Introdueix el primer número: "))
    b = int(input("Introdueix el segon número: "))
    print("El resultat de la resta és:", a - b)

elif x == 3:
    a = int(input("Introdueix el primer número: "))
    b = int(input("Introdueix el segon número: "))
    print("El resultat de la multiplicació és:", a * b)

elif x == 4:
    a = int(input("Introdueix el primer número: "))
    b = int(input("Introdueix el segon número: "))
    if b != 0:
        print("El resultat de la divisió és:", a / b)
    else:
        print("Error: No es pot dividir per zero.")

elif x == 5:
    print("Canvi de base:")
    print("1: Binari")
    print("2: Octal")
    print("3: Decimal")
    print("4: Hexadecimal")

    origen = int(input("Introdueix la base d'origen: "))
    desti = int(input("Introdueix la base de destí: "))

    numero = input("Introdueix el número que vols convertir: ")

    # Convertim el número a decimal
    if origen == 1:
        decimal = int(numero, 2)
    elif origen == 2:
        decimal = int(numero, 8)
    elif origen == 3:
        decimal = int(numero, 10)
    elif origen == 4:
        decimal = int(numero, 16)
    else:
        print("Base d'origen no vàlida.")
        decimal = None

    # Convertim de decimal a la base desitjada
    if decimal is not None:
        if desti == 1:
            resultat = bin(decimal)
        elif desti == 2:
            resultat = oct(decimal)
        elif desti == 3:
            resultat = str(decimal)
        elif desti == 4:
            resultat = hex(decimal)
        else:
            resultat = None

        if resultat is not None:
            print("El resultat de la conversió és:", resultat)
        else:
            print("Base de destí no vàlida.")

else:
    print("Operació no vàlida.")
