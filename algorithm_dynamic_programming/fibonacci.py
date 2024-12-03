from time import time

def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
def fib_cache(n, cache):
    if n < 2:
        return n
    if n in cache.keys():
        return cache[n]
    cache[n] = fib_cache(n-1, cache) + fib_cache(n-2, cache)
    return cache[n]

if __name__ == "__main__":
    
    print("Fibonacci without cache")
    start = time()
    res = fib(30)
    end = time()
    print(f"fib(30) = {res} in {end - start} seconds")

    print("Fibonacci with cache")
    start = time()
    res = fib_cache(30, {})
    end = time()
    print(f"fib(30) = {res} in {end - start} seconds")
