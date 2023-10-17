a= int(input())
b= int(input())
c= int(input())
D= b**2 - 4*a *c
if D< 0:
    print("нет корней")
elif D==0:
    print( b/ 2*a)
else:
    print((b-D**0.5)/2*a)
    print((b+D**0.5)/2*a)