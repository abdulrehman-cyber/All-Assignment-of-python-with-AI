import pandas as pd
# Create a series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)

# index value and data type 
print("Index :", s.index)
print("Data type:", s.dtype)
print("Values :", s.values)