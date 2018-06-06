def insertionSort(L):
    for j in range(1,len(L)):
        key = L[j]
        i = j-1
        print(L[i])
        while i>=0 and L[i]>key:
            L[i+1] = L[i]
            i = i-1
        L[i+1]=key 
    return L


L = [5,2,4,6,1,3]
print(L)
L1 = insertionSort(L)
print(L1)
