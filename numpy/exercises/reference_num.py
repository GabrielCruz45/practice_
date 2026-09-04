# https://www.youtube.com/watch?v=zI5ducyfyNc

import numpy as np



#                                                               creating numpy arrays                                                       -------


# Method 1: From a Python List
arr1 = np.array([1, 2, 3, 4, 5]) # All elements must be of the same type
print(f"Using np.array([...]): {arr1}")

# Method 2: Using np.arange() - similar to range()
arr2 = np.arange(0, 10, 2) # (start, stop, step)
print(f"Using np.arange(): {arr2}")

# Method 3: np.linspace() - evenly spaced numbers
arr3 = np.linspace(0, 1, 5) # (start, stop, number of elements)
print(f"Using np.linspace(): {arr3}")

# Method 4: Creating arrays of zeros
arr4 = np.zeros(5)
print(f"Using np.zeros(): {arr4}")

# Method 5: Creating arrays of ones
arr5 = np.ones(5)
print(f"Using np.ones(): {arr5}")

# Method 6: Creating arrays with a specific value
arr6 = np.full((5, 30), 7) # shape, fill_value
print(f"Specific value; np.full():\n{arr6}")

# Method 7: Identity matrix
arr7 = np.eye(3)
print(f"Identity Matrix; np.eye():\n{arr7}")

# Method 8: Random array
arr8 = np.random.rand(5) # Uniform distribution [0, 1)
print(f"Random (uniform); np.random.ran(): {arr8}")

arr9 = np.random.randint(1, 10, size=5) # [low, high), size
print(f"Random integers: {arr9}")







#                                                               numpy datatypes                                                            -------


# type inference and common types
arr_int = np.array([1, 2, 3, 4, 5])
arr_float = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
arr_mixed = np.array([1, 2.0, 3, 4.1, 5.7])

print(f"Integer: {arr_int.dtype}")
print(f"Float: {arr_float.dtype}")
print(f"Mixed: {arr_mixed.dtype} -> Promoted to float")

# Specifying types

arr10 = np.array([1, 2, 3], dtype=np.float32)
arr11 = arr_int.astype(np.float64)

print(f"Specified float32: {arr10} {arr10.dtype}")
print(f"Converted to float64: {arr11} {arr11.dtype}")

# Common types: int32, int64, float32, float64, bool
print("Memory: int32/float32: 4bytes, int64/float64, 8bytes per element")







#                                                               numpy multi-dimensional arrays                                              ------


# 2D array (Matrix)
matrix_2d = np.array(
    [[1, 2, 3], 
     [4, 5, 6], 
     [7, 8, 9]]
)

print("\n2D Array (Matrix)")
print(matrix_2d)
print(f"Shape: {matrix_2d.shape}")
print(f"Dimensions: {matrix_2d.ndim}")
print(f"Size: {matrix_2d.size}")
print(f"Data Type: {matrix_2d.dtype}\n")

# 3D array
matrix_3d = np.array([
    [
        [1, 2], [3, 4]
    ], 
    [
        [5, 6], [7, 8]
    ]
])

print(f"3D array: \n{matrix_3d}")
print(f"3D array shape (depth, rows, columns): {matrix_3d.shape}\n")

# Creating mutli-dimensional arrays with specific shapes

zeros_2d = np.zeros((3, 4))
print(f"2D zeros array: \n{zeros_2d}")

ones_3d = np.ones((2, 3, 4))
print(f"\n3D ones array shape: {ones_3d.shape}")







#                                                               array attributes                                                            -------


arr12 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(f"Array:\n{arr12}")
print(f"""
        Shape: {arr12.shape}\n
        Size: {arr12.size}\n
        ndim: {arr12.ndim}\n
        dtype: {arr12.dtype}\n
        itemsize: {arr12.itemsize} bytes\n
        nbytes: {arr12.nbytes} bytes\n
        T (transpose):\n{arr12.T}\n
""")







#                                                               indexing and slicing                                                          ----


# 1D indexing (same as Python lists)
list = np.array([10, 20, 30, 40, 50])
print("1D array")
print(f"Original array: {list}")
print(f"First element: {list[0]}")
print(f"Last element: {list[-1]}")
print(f"Elements 1 through 3: {list[1:4]}") # Slicing [start:stop:step]
print(f"Every other element: {list[::2]}\n")


# 2D indexing arr[row, column] or arr[1D, 2D, 3D, ..., nD] 
# -> arr[start:stop:step-1D, start:stop:step-2D, start:stop:step-3D, ..., start:stop:step-nD]

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D array")
print(f"Original matrix:\n{matrix}")
print(f"Element at row 1, column 2 `matrix[1, 2]`: {matrix[1, 2]}")
print(f"All columns of first row `matrix[0, :]`: {matrix[0, :]}")
print(f"All rows of second column `matrix[:, 1]`: {matrix[:, 1]}")
print(f"Submatrix (first 2 rows, first 2 columns) `matrix[0:2, 0:2]`: {matrix[0:2, 0:2]}")

# Boolean indexing arr[condition]
arr13 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
print(f"Boolean indexing\nOriginal array: {arr13}")
print(f"Elements greater than 5: {arr13[arr13 > 5]}")
print(f"Even numbers: {arr13[arr13 % 2 == 0]}")







#                                                               array operations                                                            -----

print("-----Array Operations-----")
arr14 = np.array([1, 2, 3, 4])
arr15 = np.array([5, 6, 7, 8])

print(f"\narr14: {arr14}")
print(f"arr15: {arr15}")

# element-wise operations
print(f"\n-----Element-wise operations-----")
print(f"Addition a + b: {arr14 + arr15}")
print(f"Subtraction a - b: {arr14 - arr15}")
print(f"Multiplication a * b: {arr14 * arr15}") # NOT Matrix multiplication 
print(f"Division a / b: {arr14 / arr15}")
print(f"Power a ** b: {arr14 ** arr15}")
print(f"Square root np.sqrt(arr14): {np.sqrt(arr14)}")

# Scalar operations
print(f"\n-----Scalar operations-----")
print(f"arr14 + 10: {arr14 + 10}")
print(f"arr14 - 2: {arr14 - 2}")
print(f"arr14 * 2 {arr14 * 2}")
print(f"arr14 ** 2 {arr14 ** 2}")

# Comparison operations -> creates a boolean array with the comparisons
print(f"\n-----Comparison operations-----")
print(f"arr14 > 2: {arr14 > 2}")
print(f"arr14 == 3: {arr14 == 3}")
print(f"arr14 <= 2: {arr14 <= 2}")







#                                                               array manipulation                                                            -----


print(f"\n\n\n------array manipulation------")
arr16 = np.arange(12)
print(f"Original 1D array: {arr16}")

# Reshape - changes view, doesn't copy data
reshaped = arr16.reshape(3, 4) # MUST match total size; 3 * 4 = 12 
print(f"Reshaped to 3x4:\n{reshaped}")

# Flatten - convert to 1D
flatten = reshaped.flatten()
print(f"Flattened: {flatten}")

# Reshape with -1 (auto-calculate dimension)
auto_reshape = arr16.reshape(2, -1) # -1 means "calculate automatically"
print(f"\nAuto reshape; arr.reshape(2, -1) or (2 rows, autocolumns)\n{auto_reshape}")

# Transpose
matrix_two = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original matrix:\n{matrix_two}")

print(f"Transposed:\n{matrix_two.T}")

# Concatenation
matrix_three = np.array([[1, 2], [3, 4]])
matrix_four = np.array([[5, 6],[7, 8]])
print(f"matrix_three:\n{matrix_three}\nmatrix_four:\n{matrix_four}")

print(f"Vertical concatenation np.vstack()):\n{np.vstack((matrix_three, matrix_four))}")
print(f"Horizontal concatenation np.hstack():\n{np.hstack((matrix_three, matrix_four))}")

print("Using concatenate:")
print(np.concatenate((matrix_three, matrix_four), axis=0)) # axis=0 for vertical
print(f"{np.concatenate((matrix_three, matrix_four), axis=1)}\n\n") # axis=1 for horizontal







#                                                               dimensions and axis                                                           ----

print("-----Dimensions and Axis-----")
arr_1d = np.arange(5)
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f"1D array: {arr_1d}\nShape: {arr_1d.shape}\nndim: {arr_1d.ndim}\n(axis 0 only)\n")
print(f"2D array:\n{arr_2d}\nShape: {arr_2d.shape} (rows, columns)\nndim: {arr_2d.ndim} (axis 0=rows, 1=columns)")

print(f"Matrix:\n{matrix}\nShape: {matrix.shape}\n\n")

# axis=0 collapse rows (operate down columns) -> one value per column
sum_axis0 = np.sum(matrix, axis=0)
print(f"axis=0 (down rows): {sum_axis0} -> shape: {sum_axis0.shape}")
print(f"\tExample Column 0 sum = {matrix[0,0] + matrix[1,0] + matrix[2,0]} = {sum_axis0[0]}\n")

# axis=0 collapse columns (operate accross rows) -> one value per row
sum_axis1 = np.sum(matrix, axis=1)
print(f"axis=1 (accross columns): {sum_axis1} -> shape: {sum_axis1.shape}")
print(f"\tExample Row 0 sum = {matrix[0,0] + matrix[0,1] + matrix[0,2]} = {sum_axis1[0]}\n")

arr_3d = np.array([
    [
        [1, 2, 3], 
        [4, 5, 6]
    ], 
    [
        [7, 8, 9], 
        [10, 11, 12]
    ]
])


print(f"3D array (2x2x3):\n{arr_3d}\n")
print("Think 2 pages each with a 2x3 matrix.")
print(f"Shape: {arr_3d.shape} (depth = 2, rows = 2, columns = 3)")

sum_axis0 = np.sum(arr_3d, axis=0)
print(f"axis=0 (across pages):\n{sum_axis0} -> shape: {sum_axis0.shape}")
print(f"\tExample: [0, 0, 0] = {arr_3d[0, 0, 0]} + {arr_3d[1, 0, 0]} = {sum_axis0[0, 0]}")

sum_axis1 = np.sum(arr_3d, axis=1)
print(f"axis=1 (down rows):\n{sum_axis1} -> shape: {sum_axis1.shape}")
print(f"\tExample: [0, 0] = {arr_3d[0, 0, 0]} + {arr_3d[1, 0, 0]} = {sum_axis1[0, 0]}")

sum_axis2 = np.sum(arr_3d, axis=2)
print(f"axis=2 (across columns):\n{sum_axis2} -> shape: {sum_axis2.shape}")
print(f"\tExample: [0, 0] = {arr_3d[0, 0, 0]} + {arr_3d[0, 0, 1]} + {arr_3d[0, 0, 2]} = {sum_axis2[0, 0]}\n\n")







#                                                               dimensions and axis                                                           ----

arr17 = np.arange(10)
print(f"Array: {arr17}")

# Basic statistics; 1D array
print("--------Basic Statistics--------")
print(f"Sum: {np.sum(arr17)}")
print(f"Mean: {np.mean(arr17)}")
print(f"Median: {np.median(arr17)}")
print(f"Starndard Deviation: {np.std(arr17)}")
print(f"Variance: {np.var(arr17)}")
print(f"Min: {np.min(arr17)}")
print(f"Max: {np.max(arr17)}")
print(f"Index of min: {np.argmin(arr17)}")
print(f"Index of max: {np.argmax(arr17)}")

# 2D array statistics (with axis parameter)
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("--------2D Array (Matrix) Statistics--------")
print(f"Matrix:\n{matrix}")
print(f"Sum of all elements: {np.sum(matrix)}")
print(f"Sum along rows (axis=0): {np.sum(matrix, axis=0)}") # column sums
print(f"Sum along columns {np.sum(matrix, axis=1)}") # Row sums
print(f"Mean of each column: {np.mean(matrix, axis=0)}")
print(f"Mean of each row: {np.mean(matrix, axis=1)}")







#                                                               linear algebra                                                               ----

# Matrix multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(f"Matrix a:\n{a}")
print(f"Matrix b:\n{b}\n")

# Element-wise multiplication, NOT matrix multiplication
print(f"Element-wise multiplication (a * b):\n{a * b}")

# Dot product of vectors
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print(f"\nDot product of vectors {v1} and {v2}: {np.dot(v1, v2)}")

# Matrix properties
print(f"\n😎-----------Matrix Properties-----------😎")
print(f"Matrix:\n{matrix}")

print(f"Determinant: {np.linalg.det(matrix)}")
print(f"Inverse: {np.linalg.inv(matrix)}")
print(f"Transpose: {matrix.T}")

# Eigen values and eigen vectors
eigenvals, eigenvecs = np.linalg.eig(matrix)
print(f"Eigenvalues:\n{eigenvals}\n\nEigenvectors:\n{eigenvecs}")







#                                                               useful array methods                                                       -------


arr18 = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print("------------------------------------------useful array methods------------------------------------------")
print(f"Array: {arr18}\n\n")

print(f"Sorting\nSorted Array:\n{np.sort(arr18)}") # returns sorted copy
print(f"Array unchanged: {arr18}")
arr18.sort() # in-place sort
print(f"After in-place sort: {arr18}")

arr_with_duplicates = np.array([1, 1, 2, 2, 2, 3, 4, 4, 5, 1])
print(f"Array as is: {arr_with_duplicates}")
print(f"Unique elements: {np.unique(arr_with_duplicates)}")

arr19 = np.arange(100)
print(f"Search: Where is value > 5 on \n{arr19}?\n{np.where(arr19 > 5)}")
print(f"Values where condition is True:\n{arr19[np.where(arr19 > 5)]}") # get all those different values

c = np.array([1, 2, 3])
d = np.array([5, 6, 7])
print("---Stacking---")
print(f"Array c: {c} and array d: {d}")
print(f"Stack vertically:\n{np.vstack((c, d))}")
print(f"Stack horizontally:\n{np.hstack((c, d))}")
print(f"Stack as columns:\n{np.column_stack((c, d))}")







#                                                               practical examples                                                       -------

# Simulate a greyscale image (2D array) with values 0-255
image = np.random.randint(0, 255, size=(256, 256))
print(f"Original image (256x256):\n{image}\n\n\n")

# Image operations
print("----Image statistics----")
print(f"Brightness (mean): {np.mean(image):.2f}") # :.2f -> two decimal places
print(f"Min pixel value: {np.min(image)}")
print(f"max pixel value: {np.max(image)}")
print(f"Std: {np.std(image)}")

# Brightness adjustment (add a constant)
brighter = np.clip(image + 50, 0, 255) # clip (limit) to valid range
print(f"Brightness increased, mean: {np.mean(brighter):.2f}")

# Contrast adjustment (multiply)
contrast = np.clip(image * 1.5, 0, 255)
print(f"Contrast increased, std: {np.std(contrast):.2f}")

# Data analysis

scores = np.array([
    [85, 90, 88],
    [92, 87, 91],
    [78, 82, 80],
    [95, 98, 96],
    [88, 85, 90]
])

print("Test score matrix, (5 students, 3 tests)")
print(scores)

# Calculate Statistics
print("\n\n\n\t\t\t\t--- Student Statistics ---\n\n\n")

student_averages = np.mean(scores, axis=1)
print(f"Average score per student: {student_averages}")
print(f"Best student average: {np.max(student_averages)}")
print(f"Student with best average (index): {np.argmax(student_averages)}")

print("---Test statistics---")
test_averages = np.mean(scores, axis=0)
print(f"Hardest test (lower average): {np.argmin(test_averages)}")
print(f"Easiest test (higher average): {np.argmax(test_averages)}")

print("---Find students who scored over 90---")
excellent_students = np.all(scores > 90, axis=1)
print(f"Boolean mask: {excellent_students}")
print(f"Indices: {np.where(excellent_students)[0]}")
print("Scores of excellent students")
print(scores[excellent_students])


