def is_prime(num):
    d = 2
    if num >= 1 and num <=1000:
        while num % d != 0:
            d += 1
        return d == num

print(is_prime(6))
