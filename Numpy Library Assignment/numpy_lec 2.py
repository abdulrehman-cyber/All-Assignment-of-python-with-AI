import numpy as np
import time

arr = np.array([[10,20,30],
                [40,50,60],
                [70,80,90]])

#==========================NUMPY-ARRAY-INDEXING========================
print(arr[0,1])  # 20  (row 0, column 1)
print(arr[2,2])  #  90  (row 2, column 2)


print(arr[0:2, 1:3])  # [[20 30]
                       #  [50 60]]  (rows 0-1, columns 1-2)
print(arr[::2, ::2])  # [[10 30]
                       #  [70 90]]  (every second row and column)

#==========================NUMPY-ARRAY-SLICING========================

slice_arr = arr[0] # createing the variable
slice_arr[0] = 333 # placeing new value
print(arr[0]) # [333  20  30]  (original array is modified)

#==========================NUMPY-ARRAY-COPY========================

copy_arr = arr[1].copy() # creating a copy of the array
copy_arr[0] = 555 # modifying the copy
print(arr[1]) # [40 50 60]  (original array is not modified)
print(copy_arr) # [555 50 60]  (copy array is modified)
#==========================Random-number-generation-Without-Seeding========================
rng = np.random.default_rng() # creating a random number generator
flips = rng.integers(0, 2, size=100000) # generating 10 random integers between 0 and 1
prob_heads = np.mean(flips) # calculating the mean of the flips
print(f"Estimated chance of heads: {prob_heads}") # output: Estimated chance of heads: 0.49988 (the output will vary each time you run the code)
#==========================Random-number-generation-With-Seeding========================
rng = np.random.default_rng(seed=42) # creating a random number generator with a seed
flips = rng.integers(0, 2, size=100000) # generating 10 random integers between 0 and 1
prob_heads = np.mean(flips) # calculating the mean of the flips
print(f"Estimated chance of heads: {prob_heads}") # output: Estimated chance of heads: 0.50022 (the output will be the same each time you run the code with the same seed)

#==========================Vectorization========================
# Vectorization is the process of performing operations on entire arrays rather than individual elements. This can
#lead to significant performance improvements, especially for large datasets.


# python Loop
start_time = time.time()
squared = [i**2 for i in range(1000000)] # squaring each element in a list using a loop
end_time = time.time()
print(f"Time taken using Python loop: {end_time - start_time} seconds") # output: Time taken using Python loop: 0.123456789 seconds (the output will vary each time you run the code)

# NumPy Vectorization
start_time = time.time()
arr = np.arange(1000000)
squared = arr ** 2 # squaring each element in the array using vectorization
end_time = time.time()
print(f"Time taken using NumPy vectorization: {end_time - start_time} seconds") # output: Time taken using NumPy vectorization: 0.012345678 seconds (the output will vary each time you run the code)
