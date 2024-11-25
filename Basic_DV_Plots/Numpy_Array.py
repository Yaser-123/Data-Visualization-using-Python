import numpy as np

# Get user input for array attributes
shape = tuple(map(int, input("Enter the shape of the array (e.g., 2 3 for a 2x3 array): ").split()))
dtype = input("Enter the data type of the array (e.g., int, float): ")

# Create the array dynamically
array = np.zeros(shape, dtype=dtype)

print("Dynamically created NumPy array:")
print(array)
