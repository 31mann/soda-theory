# This Code is to multiply to matrices.


# Function to take user input for a matrix
def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter the value for ({i + 1}, {j + 1}): "))
            row.append(value)
        matrix.append(row)
    return matrix

# Function to take user input for a matrix
def input_complex_matrix():
    # take input for matrix dimensions
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    # initialize matrix with zeros
    matrix = [[0 + 0j for j in range(cols)] for i in range(rows)]

    # take input for each element in matrix
    for i in range(rows):
        for j in range(cols):
            real_part = float(input(f"Enter the real part of element {i + 1},{j + 1}: "))
            imag_part = float(input(f"Enter the imaginary part of element {i + 1},{j + 1}: "))
            matrix[i][j] = complex(real_part, imag_part)
    return matrix


# Function to multiply two matrices
def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matrices cannot be multiplied")
        return None
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = 0
            for k in range(len(matrix1[0])):
                element += matrix1[i][k] * matrix2[k][j]
                element = complex(round(element.real, 3), round(element.imag, 3))
            row.append(element)
        result.append(row)
    print(result)
    return result
