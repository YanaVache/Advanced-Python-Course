def pierwiastek(n):
    sum = 0
    k=0
    while sum<n:
        k=k+1
        sum += 2*k-1
    if(sum > n):
            return k-1
    return k

print(pierwiastek(9)) #3
print(pierwiastek(10))#3
print(pierwiastek(15))#3
print(pierwiastek(16))#4
