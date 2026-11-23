l=[1,2,[2,3], "hola"]
l[3]="hala"
#print(l[3])
for e in l:
    print(e)
for i in range(len(l)):
    print(i)
for i,e in enumerate(l):
    print("la posició",i,"té el valor",e)
    if l[i]==1 or l[i]=="1":
        l[i]="a"
    
    
   