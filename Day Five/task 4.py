def ReverseDict(d1):
    list1 = list(d1.items())
    list1.reverse()
    reverseddict = dict(list1)
    return reverseddict

d1 = {'one':1, 'two':2,'three': 3}
d2 = {}
print(d1)
d2  = ReverseDict(d1)
print(d2,type(d2))