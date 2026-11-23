
l=list()
for i in range(10):
    l.append(int(input("Introdueix un número: ")))
l2=list()

for i in range(4,-1,-1):
    l2.append(l[i])
print(l2)
for i in range(len(l)):
    l2.append(l[i])

