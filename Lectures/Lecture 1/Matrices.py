matrix = [[1, 2, 3, 4], 
    [5, 6, 7, 8],
    [9, 10, 11, 12]]

print("Matrix =", matrix)
print("------------------------------------------------------------------------------------------")


Row = int(input("Enter the number of rows:"))
Column = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries row wise:")

# For user input
# A for loop for row entries
for row in range(Row):    
    a = []
    # A for loop for column entries
    for column in range(Column):   
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for row in range(Row):
    for column in range(Column):
        print(matrix[row][column], end=" ")
    print()
print("------------------------------------------------------------------------------------------")


matrix = [[column for column in range(4)] for row in range(4)]
print(matrix)
print("------------------------------------------------------------------------------------------")


X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row = column = 1
X[row][column] = 11
print(X)
print("------------------------------------------------------------------------------------------")


row = -2
column = -1
X[row][column] = 21
print(X)
print("------------------------------------------------------------------------------------------")


print("Matrix at 1 row and 3 column=", X[0][2]) 
print("Matrix at 3 row and 3 column=", X[2][2])
print("------------------------------------------------------------------------------------------")


import numpy as np

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(X[-1][-2])
print("------------------------------------------------------------------------------------------")


# Program to add two matrices using nested loop
X = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
Y = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for row in range(len(X)):

    # iterate through columns
    for column in range(len(X[0])):
        result[row][column] = X[row][column]+ Y[row][column]

for r in result:
    print(r)
print("------------------------------------------------------------------------------------------")


Add_result = [[X[row][column] + Y[row][column]
               for column in range(len(X[0]))] 
               for row in range(len(X))]
Sub_result = [[X[row][column] - Y[row][column]
               for column in range(len(X[0]))] 
               for row in range(len(X))]

print("Matrix Addition")
for r in Add_result:
    print(r)

print("\nMatrix Subtraction")
for r in Sub_result:
    print(r)
print("------------------------------------------------------------------------------------------")


rmatrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(X)):
    for column in range(len(X[0])):
        rmatrix[row][column] = X[row][column] * Y[row][column]
        
print("Matrix Multiplication",)
for r in rmatrix:
    print(r)
        
for i in range(len(X)):
    for j in range(len(X[0])):
        rmatrix[row][column] = X[row][column] // Y[row][column]

print("\nMatrix Division",)   
for r in rmatrix:
    print(r)
print("------------------------------------------------------------------------------------------")


X = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# iterate through rows
for row in range(len(X)):
    # iterate through columns
    for column in range(len(X[0])):
        result[column][row] = X[row][column]

for r in result:
    print(r)
    
# # Python Program to Transpose a Matrix using the list comprehension

# rez = [[X[column][row] for column in range(len(X))] 
#    for row in range(len(X[0]))]

# for row in rez:
#     print(row)
print("------------------------------------------------------------------------------------------")

  
# 1st argument --> numbers ranging from 0 to 9, 
# 2nd argument, row = 3, col = 3
array = np.random.randint(10, size=(3, 3))
print(array)
print("------------------------------------------------------------------------------------------")


import numpy

# initializing matrices
x = numpy.array([[1, 2], [4, 5]])
y = numpy.array([[7, 8], [9, 10]])

# using add() to add matrices
print ("The element wise addition of matrix is : ")
print (numpy.add(x,y))

# using subtract() to subtract matrices
print ("The element wise subtraction of matrix is : ")
print (numpy.subtract(x,y))

print ("The element wise multiplication of matrix is : ")
print (numpy.multiply(x,y))

# using divide() to divide matrices
print ("The element wise division of matrix is : ")
print (numpy.divide(x,y))
print("------------------------------------------------------------------------------------------")


X = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

Y = [[9, 8, 7], [6, 5, 4],[3, 2, 1]]

dotproduct = np.dot(X, Y)
print("Dot product of two array is:", dotproduct)

dotproduct = np.cross(X, Y)
print("Cross product of two array is:", dotproduct)
print("------------------------------------------------------------------------------------------")


matrix = [[1, 2, 3], [4, 5, 6]]
print("\n", numpy.transpose(matrix))
print("------------------------------------------------------------------------------------------")


a = np.zeros([2, 2], dtype=int)
print("\nMatrix of 2x2: \n", a)

c = np.zeros([3, 3])
print("\nMatrix of 3x3: \n", c)
print("------------------------------------------------------------------------------------------")