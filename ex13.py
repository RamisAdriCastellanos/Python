x = int(input("quina operació vols fer? (1: suma, 2: resta, 3: multiplicació, 4: divisió): "))
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
else:
    print("Operació no vàlida.")