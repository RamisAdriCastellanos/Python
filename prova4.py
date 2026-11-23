x=input("intro la paraula: ")
sum_a=0
sum_m=0
sum_altres=0

for c in x:
  if c=="a":
     sum_a=sum_a+1
print("la paraula {} te {}-a". format(x, str(sum_a)))
elif c=="m":
    sum_m=sum_m+1
print("la paraula {} te {}-m". format(x, str(sum_m)))
else:
 sum_altres=sum_altres+1
print("la paraula {} te {}-m". format(x, str(sum_m)))