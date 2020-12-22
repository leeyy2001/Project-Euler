import math

n = -1
odd_compo = []
primes = []
while True:
    n += 2
    for a in range(2, n):
        if n % a == 0:
            odd_compo.append(n)
            break
    if len(odd_compo) == 10000:
        break

for b in range(10000):
    IsPrime = True
    for c in range(2, b):
        if b % c == 0:
            IsPrime = False
    if IsPrime: # when IsPrime is False theres no need to continue the loop. Its inefficient. So just exit the loop and append is IsPrime is True.
        primes.append(b)
primes.remove(0)

values = []

for c in primes:
    for d in range(10000):
        goldbach = c + 2 * (d**2)
        values.append(goldbach)

answer = list(set(odd_compo) - set(values))
answer.sort()
print(answer)