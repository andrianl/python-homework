import functools
import time


def timer(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time)
        print("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 3)))
        return value

    return wrapper


@timer
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


print(SieveofEratosthenes(100))
