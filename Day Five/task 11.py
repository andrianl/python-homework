from math import sqrt

def QuadraticEquationPolynom(a,b,c,d=0):
    c-=d
    d=0
    def Polynom(x1,x2):
        return a*x1*x1+b*x1+c, a*x2*x2+b*x2+c

    D=b*b-4*a*c
    if D>0:
        x1=(-b+sqrt(D))/2*a
        x2=(-b-sqrt(D))/2*a
        return Polynom(x1,x2)
    else:
        D=abs(complex(D))
        j=complex(0,1)
        x1=(-b+j+sqrt(D))/2*a
        x2=(-b-j+sqrt(D))/2*a
        return Polynom(x1, x2)





print('F(x)=ax^2+bx+c')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
print('default d=0')
d=float(input('d='))
print(QuadraticEquationPolynom(a,b,c,d))