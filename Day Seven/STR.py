class SuperString:
    def __init__(self,string):
        self.string = string

    def __truediv__(self, other):
        return f'{self.string}  /  {other}'


a = SuperString('gmail')
b = 'mail'

print(a/b)