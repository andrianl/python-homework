def RecursiveSum(n):
    if n == 0:
        return n
    else:
        return n + RecursiveSum(n - 1)


n = int(input('Enter integer:'))
sum = RecursiveSum(n)
print(sum)