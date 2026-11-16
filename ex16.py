num1 = int(input("Dona el primer número: "))
num2 = int(input("Dona el segon número: "))
num3 = int(input("Dona el tercer número: "))

if num1 > num2 and num1 > num3:
    print("El major és:", num1)
elif num2 > num3:
    print("El major és:", num2)
else:
    print("El major és:", num3)