import twiddle as tw
import numpy as np

def show_matrix(matrix):
    for row in matrix:
        formatted_row = [f"{element.real:.2f} + {element.imag:.2f}j" for element in row]
        print("[", "\t".join(formatted_row), "]")

def get_twiddle_matrix_size():
    while True:
        try:
            tw_size = int(input("Enter the size of the twiddle matrix: "))
            return tw_size
        except ValueError:
            print("Error: Please enter a valid number for the twiddle matrix size.")

def get_input_matrix(tw_size):
    ip_matrix = []

    for i in range(tw_size):
        while True:
            try:
                row = [float(x) for x in input(f"Enter space-separated values for row {i+1}: ").split()]
                ip_matrix.append(row)
                break
            except ValueError:
                print("Error: Please enter valid numeric elements for the row.")

    return ip_matrix

def dft_calculate():
    tw_size = get_twiddle_matrix_size()
    twiddle_matrix = tw.tw_matrix(tw_size)
    ip_matrix = get_input_matrix(tw_size)


    result_matrix = []

    for i in range(tw_size):
        row = ip_matrix[i]
        row_result = np.dot(row, twiddle_matrix)
        result_matrix.append(row_result)

    # Convert the result_matrix to a NumPy array for column-wise multiplication
    result_matrix = np.array(result_matrix)

    # Perform column-wise matrix multiplication on the result_matrix
    final_result = np.dot(result_matrix.T, twiddle_matrix)

    # Transpose the final result matrix
    final_result = final_result.T

    print("\nFinal Result Matrix:")
    show_matrix(final_result)



def dft_calculate1(tw_size,ip_matrix):
    twiddle_matrix = tw.tw_matrix(tw_size)
    result_matrix = []

    for i in range(tw_size):
        row = ip_matrix[i]
        row_result = np.dot(row, twiddle_matrix)
        result_matrix.append(row_result)

    # Convert the result_matrix to a NumPy array for column-wise multiplication
    result_matrix = np.array(result_matrix)

    # Perform column-wise matrix multiplication on the result_matrix
    final_result = np.dot(result_matrix.T, twiddle_matrix)

    # Transpose the final result matrix
    final_result = final_result.T
    return final_result
