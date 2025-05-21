import timeit

def doskonale_imperatywna(n):
    lista=[]
    for i in range(1, n+1):
        sum=0
        for j in range(1, i):
            if i%j==0:
                sum += j
        if sum==i:
            lista.append(i)
    return lista


def doskonale_skladana(n):
    return [i for i in range(1,n+1) if sum([j for j in range (1,i) if i%j == 0]) == i]

def doskonale_funkcyjna(n):
    return list(filter(lambda i: i==sum([j for j in range(1,i) if i%j==0]), range(1,n+1)))

print("Test dla n=100")
print("Imperatywna:: ", doskonale_imperatywna(100), " : ", timeit.timeit(lambda: doskonale_imperatywna(100), number=1))
print("Skladana: ", doskonale_skladana(100), " : ", timeit.timeit(lambda: doskonale_skladana(100), number=1))
print("Funkcyjna: ", doskonale_funkcyjna(100), " : ", timeit.timeit(lambda: doskonale_funkcyjna(100), number=1))

print("Test dla n=1000")
print("Imperatywna:: ", doskonale_imperatywna(1000), " : ", timeit.timeit(lambda: doskonale_imperatywna(1000), number=1))
print("Skladana: ", doskonale_skladana(1000), " : ", timeit.timeit(lambda: doskonale_skladana(1000), number=1))
print("Funkcyjna: ", doskonale_funkcyjna(1000), " : ", timeit.timeit(lambda: doskonale_funkcyjna(1000), number=1))

print("Test dla n=10000")
print("Imperatywna:: ", doskonale_imperatywna(10000), " : ", timeit.timeit(lambda: doskonale_imperatywna(10000), number=1))
print("Skladana: ", doskonale_skladana(10000), " : ", timeit.timeit(lambda: doskonale_skladana(10000), number=1))
print("Funkcyjna: ", doskonale_funkcyjna(10000), " : ", timeit.timeit(lambda: doskonale_funkcyjna(10000), number=1))