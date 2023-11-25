import numpy as np


## Create Array using Numpy
arr = np.array([1,2,3,4])
print(arr)

#Acessing a element
print(arr[1])

# DataType
print(arr.dtype)

#Copy and View

x = arr.copy()
x[1] = 32

print(x)

y = arr.view()
y[0] = 12
print(y)

## Looping Array Elements

for index, value in enumerate(arr):
    print(index, value)



## minimo = matriz.min()
## maximo= matriz.max()
## soma=matriz.sum()
## media=matriz.mean()
## desvio=matriz.std()