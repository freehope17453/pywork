def fibonacci(n):
    a,b =1,1
    L = [1]
    for x in range(n):
        a,b = b,a+b
        L.append(a)
    return L
L = fibonacci(10)
print(L)


