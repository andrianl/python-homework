def DivideByZero(func):
    def inner(a, b):
        if b==0:
            print('Cant divide by zero')
            return
        return func(a,b)
    return inner
    



@DivideByZero
def Root(a,b):
    x = b / a
    return x


a=2
b=0
print(Root(a,b))

