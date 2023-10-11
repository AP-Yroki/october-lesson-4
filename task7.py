def bank(a, years):
    for i in range(years):
        a = int(a * 1.1)
    return a

print(bank(1000, 20))