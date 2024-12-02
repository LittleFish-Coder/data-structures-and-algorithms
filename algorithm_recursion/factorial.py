# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 5! = 5 * 4 * 3!
# 5! = 5 * 4 * 3 * 2!
# 5! = 5 * 4 * 3 * 2 * 1!
# 5! = 5 * 4 * 3 * 2 * 1

def fac(n):
    if n <= 1:
        return n
    else:
        return n * fac(n-1)
    
def fac_iterate(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res
        

if __name__ == '__main__':
    print(f"fac(1): {fac(1)}")
    print(f"fac(2): {fac(2)}")
    print(f"fac(3): {fac(3)}")
    print(f"fac(4): {fac(4)}")
    print(f"fac(5): {fac(5)}")
    print(f"fac(6): {fac(6)}")