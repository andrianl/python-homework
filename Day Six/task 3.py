def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def Fibonacci(num):
    fibonacci_list=[0,1]
    for i in range(num):
        fibonacci_list.append(fibonacci_list[-1]+fibonacci_list[-2])
    return fibonacci_list




print(Fibonacci(30))