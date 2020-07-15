class Series(object):
    def __init__(self, low, high, step=1):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self, step=1):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += step
            return self.current - step

    def series_generator(self,low, high, step=1):
        while low <= high:
            yield low
            low += step



alphabet=[]
alphabet2=[]
r=Series(1,26)
for i in r:
    alphabet.append(chr(i+96))


for i in r.series_generator(1,26):
    alphabet2.append(chr(i+96))

print(alphabet)
print(alphabet2)