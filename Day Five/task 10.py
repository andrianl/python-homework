from math import sqrt

def QuadraticEquation(a,b,c,d=0):
    c-=d
    d=0
    D=b*b-4*a*c
    if D>0:
        x1=(-b+sqrt(D))/2*a
        x2=(-b-sqrt(D))/2*a
        return x1,x2
    else:
        D=abs(complex(D))
        j=complex(0,1)
        x1=(-b+j+sqrt(D))/2*a
        x2=(-b-j+sqrt(D))/2*a
        return x1,x2



print('ax^2+bx+c=d')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
print('default d=0')
d=float(input('d='))
print(QuadraticEquation(a,b,c,d))