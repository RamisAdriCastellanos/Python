#llegir 10 noms i juntar-los de 2 en 2 i llavors imprimir-los
l=list()
for i in range(10):
    l.append(input("Introdueix un nom: "))
r=list()
for i in range(0,10,2):
    r.append(l[i]+", "+l[i+1])
r2=list()
for i in range(5):
    r2.append(l-[i+1]+", "+l[(i)])
    print(r2)
#llegeix 10 noms i nomes imprimeix els imparells
for i in range(1,10,2):
    print(i)
#dins una llista de 9 a 0
l=list()
for i in range(9,-1,-1):
    l.append(i)
print(l)
