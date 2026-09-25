# NumPy Basics
# Description: This program demonstrates basic NumPy operations including
# array creation, statistical operations, matrix indexing, array generation,
# filtering, shape checking, axis operations, reshaping, and random numbers.


import numpy as np
a=np.array([1,2,3,4,5,6,7,8,0])
print(np.mean(a))
print(np.sum(a))
print(np.max(a))
print(np.min(a))

a=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print(a[1,1])

numbers=np.arange(1,20)
print(numbers)

temperature = np.array([22, 25, 31, 28, 35, 19, 40])
print(temperature[temperature>30])

a=np.matrix([[1,2,3],[4,5,6],[7,8,9]])
print(np.shape(a))
print(a[0])
print(a[2,1])


mat=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.sum(mat,axis=0))
print(np.sum(mat,axis=1))

create=np.arange(1,13)
b=create.reshape(3,4)
print(b)

numbers=np.random.randint(1,100,10)
print(numbers)
print(np.sum(numbers))