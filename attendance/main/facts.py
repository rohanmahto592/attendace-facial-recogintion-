f1=1;
f2=1;
n1=int(input("enter the number1"))
n2=int(input("enter the number2"))
for i in range(1,n1+1):
    f1=f1*i
for j in range(1,n2+1):
    f2=f2*j
while f1!=f2:
    if f1>f2:
        f1=f1-f2
    else:
        f2=f2-f1
print(f1)
