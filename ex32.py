
def mostrar_majors_que(tupla, num):
    for i in tupla:
        if i > num:
            print(i)

tupla = ()
for i in range(5):
    val = int(input(f"Introdueix el valor {i+1}: "))
    tupla += (val,)

mostrar_majors_que(tupla, 18)