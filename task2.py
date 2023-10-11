a = int(input('num: '))
n = int(input('power: '))

def power(a, n):
    res = 1
    while n > 0:
        res *= a
        n -= 1
    return res
print(power(a,n))