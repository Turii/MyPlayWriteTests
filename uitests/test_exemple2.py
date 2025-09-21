import numpy as np


a = [1, 2, 3]
b = {1, 2, 3}
c = {1: 'a', 2: 'b', 3: 'c'}

print(len(a), len(b), len(c))

A = np.array([
    [1, 1, 1],
    [1, 2, 1],
    [1, 1, 2]
])

det = np.linalg.det(A)

print("Determinant:", det)

if det !=0:
    print("Non-singular → unique solution")
else:
    print("Singular → infinite or no solution")


A = np.array([
        [4, -3, 1],
        [2, 1, 3],
        [-1, 2, -5]
    ], dtype=np.dtype(float))

#1-dimensional NumPy array
b = np.array([-10, 0, 17], dtype=np.dtype(float))

#row vector, you need to give it 2 dimensions:
row_vec = np.array([[-10, 0, 17]])
print(row_vec.shape)  # ➞ (1, 3)

#column vector
col_vec = np.array([[-10], [0], [17]])
print(col_vec.shape)  # ➞ (3, 1)

print("Matrix A:")
print(A)
print("\nArray b:")
print(b)

print(f"Shape of A: {np.shape(A)}")
print(f"Shape of b: {np.shape(b)}")
