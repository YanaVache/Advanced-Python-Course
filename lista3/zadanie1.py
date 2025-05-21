import math
import timeit

def pierwsze_imperatywna(n):
    lista =[]
    for i in range(2, n+1):
        is_prime=True
        for j in range(2, int(math.sqrt(i)) + 1):
            if (i%j)==0:
                is_prime=False
        if is_prime:
            lista.append(i)
    return lista


def pierwsze_skladana(n):
    return [i for i in range(2, n+1) if all(not (i % j == 0) for j in range(2, int(math.sqrt(i)) + 1)) ]
    
def pierwsze_funkcyjna(n):
    return list(filter(lambda i: all(not (i % j == 0) for j in range(2, int(math.sqrt(i)) + 1)), range(2, n+1)))

print("Test dla n=20")
print("Imperatywna:: ", pierwsze_imperatywna(20), " : ", timeit.timeit(lambda: pierwsze_imperatywna(20), number=1))
print("Skladana: ", pierwsze_skladana(20), " : ", timeit.timeit(lambda: pierwsze_skladana(20), number=1))
print("Funkcyjna: ", pierwsze_funkcyjna(20), " : ", timeit.timeit(lambda: pierwsze_funkcyjna(20), number=1))


print("Test dla n=50")
print("Imperatywna:: ", pierwsze_imperatywna(50), " : ", timeit.timeit(lambda: pierwsze_imperatywna(50), number=1))
print("Skladana: ", pierwsze_skladana(50), " : ", timeit.timeit(lambda: pierwsze_skladana(50), number=1))
print("Funkcyjna: ", pierwsze_funkcyjna(50), " : ", timeit.timeit(lambda: pierwsze_funkcyjna(50), number=1))

print("Test dla n=100")
print("Imperatywna:: ", pierwsze_imperatywna(100), " : ", timeit.timeit(lambda: pierwsze_imperatywna(100), number=1))
print("Skladana: ", pierwsze_skladana(100), " : ", timeit.timeit(lambda: pierwsze_skladana(100), number=1))
print("Funkcyjna: ", pierwsze_funkcyjna(100), " : ", timeit.timeit(lambda: pierwsze_funkcyjna(100), number=1))
