import math

n = int(input("Value of n?"))

def legendre(n):
    if n == 1:
        return True
    for i in range(1, n + 1):
        n_low = i ** 2
        n_high = (i + 1) ** 2 + 1
        for z in range (n_low, n_high):
            for x in range(2, math.floor(math.sqrt(z))):
                if z % x != 0:
                    return True
                else: return False

print(legendre(n)) 