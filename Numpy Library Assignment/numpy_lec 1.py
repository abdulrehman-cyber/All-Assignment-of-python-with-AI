# #==========================NUMPY-ARRAY-FUNCTION========================

import numpy as np

# Create a simple dimensional array

my_arr=np.array([12,53,23,44]) 
print(my_arr)


# creating a 2 row , 3 column matrix using 0
print(np.zeros((2,3)))


#creating a 2 row , 3 column matrix using 1
print(np.ones((2,3)))


print(np.full((2,3),7))


print(np.arange(0,10.2))

print(np.linspace(0,10,15))

print(np.eye(3))

print(np.diag([1,2,3]))

print(np.array([1,2,3], dtype=float))

arr= np.array([[10,20,30]])
print(arr.astype(int))
