import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Shape of Array:", arr.shape)

reshaped_arr = arr.reshape(3, 2)
print("\nReshaped Array:")
print(reshaped_arr)
