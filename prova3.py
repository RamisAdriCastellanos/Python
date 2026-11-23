def canvi(x):
    x=x+1
    print(x)
def canvireferncia(llista):
    if len(llista)>0:
        llista[0]="guapo"
    else:
        print("no te cap valor")
#Programa Principal
nombre =3
canvi(nombre)
print(nombre)
real=3,12141516
bool =False
cadena ="hola ramis" 
print(cadena)
llista =[3,[4,5],(1,2,3), "hola"]
canvireferncia(llista)
print(llista[0])
tupla = (1,3,3,4)
rang =range(1,11,2)
diccionari={"nom":"Adria","cognom":"Castellanos","edat":28,"telefon":"676814400"}
nombre =4
llista[3]="hola mon"
print(llista[3])



