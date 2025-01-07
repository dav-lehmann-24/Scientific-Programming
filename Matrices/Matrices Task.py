import random


# Functions
def CreateMatrix():
    Row = int(input("Enter the number of rows: "))
    Column = int(input("Enter the number of columns: "))

    # Initialize matrix
    matrix = []
    print("Enter the entries row wise: ")

    # For user input
    # A for loop for row entries
    for row in range(Row):
        a = []
        # A for loop for column entries
        for column in range(Column):
            a.append(int(input()))
        matrix.append(a)
    return matrix


def CreateMatrixRandom(Row, Column):
    # Initialize matrix with random numbers
    matrix = [[random.randint(0, 10) for _ in range(Column)] for _ in range(Row)]
    return matrix


# Validate List Dimensions
def ListSizeEquals(listA, listB):
    rowCountA = len(listA)
    rowCountB = len(listB)
    return rowCountA == rowCountB


# Validate matrix dimensions
def ValidateDimensions(matrixA, matrixB):
    rowsMatch = ListSizeEquals(matrixA, matrixB)
    columnA = matrixA[0]
    columnB = matrixB[0]
    return rowsMatch and ListSizeEquals(columnA, columnB)


# Adding the matrices
def AddMatrices(matrixA, matrixB):
    if not ValidateDimensions(matrixA, matrixB):
        return "Error: Addition not possible due to different dimensions of matrices."
    newMatrix = []
    for rowIndex in range(len(matrixA)):
        newRow = []
        for columnIndex in range(len(matrixA[0])):
            newRow.append(matrixA[rowIndex][columnIndex] + matrixB[rowIndex][columnIndex])
        newMatrix.append(newRow)
    return newMatrix


# Subtracting the matrices
def SubtractMatrices(matrixA, matrixB):
    if not ValidateDimensions(matrixA, matrixB):
        return "Error: Subtraction not possible due to different dimensions of matrices."
    newMatrix = []
    for rowIndex in range(len(matrixA)):
        newRow = []
        for columnIndex in range(len(matrixA[0])):
            newRow.append(matrixA[rowIndex][columnIndex] - matrixB[rowIndex][columnIndex])
        newMatrix.append(newRow)
    return newMatrix


# Multiply the matrices
def MultiplyMatrices(matrixA, matrixB):
    # Verify dimensions: Columns of A must match Rows of B
    if len(matrixA[0]) != len(matrixB):
        return "Error: Multiplication not possible due to different column length / row length"  # Invalid multiplication

    # Initialize result matrix with zeros
    result = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

    # Perform multiplication
    for firstMatrixRow in range(len(matrixA)):  # Iterate over rows of A
        for SecondmatrixColumns in range(len(matrixB[0])):  # Iterate over columns of B
            for SecondMatrixRows in range(len(matrixB)):  # Iterate over rows of B (or columns of A)
                cellValue = matrixA[firstMatrixRow][SecondMatrixRows] * matrixB[SecondMatrixRows][SecondmatrixColumns]
                result[firstMatrixRow][SecondmatrixColumns] += cellValue
    return result


# Transpose the matrix
def TransposeMatrix(matrix):
    transposedMatrix = [[matrix[row][column] for row in range(len(matrix))] for column in range(len(matrix[0]))]
    return transposedMatrix


MatA = CreateMatrix()
MatB = CreateMatrix()
MatResultAdd = AddMatrices(MatA, MatB)
print("Matrix Addition: " + str(MatResultAdd))
MatResultSub = SubtractMatrices(MatA, MatB)
print("Matrix Subtraction: " + str(MatResultSub))
MatResultMultiply = MultiplyMatrices(MatA, MatB)
print("Matrix Multiplication: "  + str(MatResultMultiply))
MatATransposed = TransposeMatrix(MatA)
print("Matrix A Transposed: " + str(MatATransposed))
MatBTransposed = TransposeMatrix(MatB)
print("Matrix B Transposed: " + str(MatBTransposed))

input("Press Enter to exit...")