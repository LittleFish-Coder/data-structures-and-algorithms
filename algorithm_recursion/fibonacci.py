def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

# memoization (using cache)
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

def fib_iterate(n):
    if n < 2:
        return n
    
    prev, curr = 0, 1
    for _ in range(2, n+1):
        new_num = prev + curr
        prev, curr = curr, new_num
    
    return new_num


if __name__ == '__main__':
    print(f"fib(0): {fib(0)}")
    print(f"fib(1): {fib(1)}")
    print(f"fib(2): {fib(2)}")
    print(f"fib(3): {fib(3)}")
    print(f"fib(4): {fib(4)}")
    print(f"fib(5): {fib(5)}")
    print(f"fib(6): {fib(6)}")

    print(f"fib_memo(0): {fib_memo(0)}")
    print(f"fib_memo(1): {fib_memo(1)}")
    print(f"fib_memo(2): {fib_memo(2)}")
    print(f"fib_memo(3): {fib_memo(3)}")
    print(f"fib_memo(4): {fib_memo(4)}")
    print(f"fib_memo(5): {fib_memo(5)}")
    print(f"fib_memo(6): {fib_memo(6)}")

    print(f"fib_iterate(0): {fib_iterate(0)}")
    print(f"fib_iterate(1): {fib_iterate(1)}")
    print(f"fib_iterate(2): {fib_iterate(2)}")
    print(f"fib_iterate(3): {fib_iterate(3)}")
    print(f"fib_iterate(4): {fib_iterate(4)}")
    print(f"fib_iterate(5): {fib_iterate(5)}")
    print(f"fib_iterate(6): {fib_iterate(6)}")