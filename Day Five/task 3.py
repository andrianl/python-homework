def SieveofEratosthenes(num):
    limit=num+1
    composites=set()
    primes=[]
    for i in range(2, limit):
        if i in  composites:
            continue
        for f in range(i*2, limit, i):
            composites.add(f)
        
        primes.append(i)

    return primes


print(SieveofEratosthenes(1000))
