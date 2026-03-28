import numpy as np

arr = np.arange(20)

mat = arr.reshape(4,5)
print("Matrix:\n", mat)

print("After adding 10:\n", mat + 10)

print("Column sum:", mat.sum(axis=0))
print("Row sum:", mat.sum(axis=1))

a = np.array([1,2,3])
b = np.array([4,5,6])

print("Vertical:\n", np.vstack((a,b)))
print("Horizontal:\n", np.hstack((a,b)))