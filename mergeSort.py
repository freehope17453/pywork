def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-q
    L=[]
    R=[]
    for i in range(n1):
        L.append(A[p+i-1])

    for j in range(n2):
        R.append(A[q+j])

    print('L = %s  R= %s' %(L,R))

    llen = len(L)
    rlen = len(R)
    i=0
    j=0
    k=p-1
    print(range(k,r))
    for k in range(k,r):
        if i==llen and j<rlen:
            A[k]=R[j]
            j = j+1
        elif i<llen and j==rlen:
            A[k]=L[i]
            i = i+1
        elif L[i]<=R[j]:
            A[k]=L[i]
            i = i+1
        else:
            A[k]=R[j]
            j = j+1
    

def merge_sort(A,p,r):
    if p<r:
        q = int((r+p-1)/2)
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)


#A=[5,2]
#A=[5,2,3,7]
A=[5,2,3,1,4,10003,2,6,2006,7,123,34,25,39,98,0,300,-98,200,203,-3,100,21,34,27,48,200,307,54,864,21,32,14,52,31,67]
print(A)
merge_sort(A,1,len(A))
print('A = ',A)
