#llegir 10 numeros i guardar-los en una llista
l=list()
for i in range(10):
    l.append(int(input("Introdueix un numero: ")))
print(l)
#llegir 10 numeros i guardar-los en una llista amb cuadrats
l2=list()
for i in range(10):
    l2.append(l[i]**2)
print(l2)
#imprimir els numeros i al costat el seu cuadrat
for i in range(10):
    print(l[i],l2[i])