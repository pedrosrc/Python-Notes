## Search Index
nomes = ['Peter', 'John', 'Derek']
search = nomes.index('Derek')


def buscaList(k, L , n):
    i=0
    indiceL=-1
    while i < n:
        if L[i]==k:
            indiceL=i
            i=n+1
        i = i + 1
    return(indiceL)

si = buscaList('Peter', nomes , len(nomes))

##Busca Ordenada

def buscaOrdenada(k,L,n):
    i = 0
    indiceL=-1
    while(i<n):
        if L[i] >= k:
            if L[i] == k:
                indiceL = i 
                i=n+1
            else:
                i=n+1
        else:
                i=i+1
    return indiceL

numbers = [2,3,4,5,6,7,8,9,10]
i = buscaOrdenada(7, numbers, len(numbers))

## Insert name
##nomes.append(input('Digite um nome:'))
##print(nomes)

## Insert Number Order

def insertOrder(k, L, n):
    i= 0
    posInitial=-1
    while (i<n):
        if L[i] >= k:
            if L[i] == k:
                return -1
            else:
                posInitial = i
                i = n+1
        else:
            i=i+1
        if i ==n:
            posInitial=n

    L.append('')
    i=n
    while (i>posInitial):
        L[i]=L[i-1]
        i=i-1
    L[posInitial]=k
    return posInitial

insertOrder(1, numbers, len(numbers))

