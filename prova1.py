def menu(): 
    opcio = 0
    while opcio < 1 or opcio > 4:  
        print("""
        Menu principal:
        1.suma
        2.resta
        3.multiplicacio
        4.divisio
        """)
        opcio =int(input("indiqui el numero de la funcio que vol executar:"))
    return opcio

# Programa principal    

op =menu()
match(op):
    case 1:
        print("operacions de suma \n ")
        x = int(input("indiqui el primer numero:"))
        y = int(input("indiqui el segon numero:"))
        print("el resultat de la suma es:",x+y)
    case 2:
        print("operacions de  resta \n ")
        x = int(input("indiqui el primer numero:"))
        y = int(input("indiqui el segon numero:"))
        print("el resultat de la resta es:",x-y)
    case 3:
        print("operacions de  multiplicacio \n ")
        x = int(input("indiqui el primer numero:"))
        y = int(input("indiqui el segon numero:"))
        print("el resultat de la multiplicacio es:",x*y)
    case 4:
        print("operacions de  divisio \n ")
        x = int(input("indiqui el primer numero:"))
        y = int(input("indiqui el segon numero:"))
        print("el resultat de la divisio es:",x/y)
    case _:
         print("En qualsevol altre cas \n ")


        
