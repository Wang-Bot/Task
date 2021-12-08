import numpy as np

matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
matrix3 = matrix1 + matrix2
matrix4 = matrix1 - matrix2
matrix5 = matrix1.dot(matrix2)
print("The Addition of Matrix1 and Matrix2 is")
print (matrix3)
print("The Difference between Matrix1 and Matrix2 is")
print (matrix4)
print("The Multiplication of Matrix1 and Matrix2 is")
print (matrix5)