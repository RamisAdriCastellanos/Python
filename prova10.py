l=list()
l = []
for i in range(10):
    num = int(input("Introdueix un nombre: "))
    l.append(num)

suma = 0
for n in l:
    if n % 2 != 0:
        suma += n

print("La suma dels nombres imparells és:", suma)
