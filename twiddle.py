# This Code is to compute the DFT matrix of any given input sequence.
import math
import MatrixMultiplication as mm


# Below function is used to calculate the values of the twiddle factors up N-1.
def twiddle(n):
    N: int = n
    cn = complex(0, 1)
    arr = [int] * N
    for i in range(N):
        res = math.e ** ((-cn * 2 * math.pi * i) / N)
        arr[i] = complex(round(res.real, 3), round(res.imag, 3))
    # print(arr)
    return arr


# Below function is used to calculate the values of the twiddle Matrix of twiddle factor and return, computed values.
def tw_matrix(m):
    n = m  # temporary variable.
    rows = n
    cols = n
    matrix = []
    arr = twiddle(n)
    # this piece of code to set the values of the matrix.
    for i in range(rows):  # This outer-loop runs for creating  the row of matrix.
        row = []
        for j in range(cols):  # This inner-loop runs for creating  the columns of matrix.
            for k in range(n):  # This loop is used to utilise the cyclic property of the DFT.
                value = i * j
                if value % n == k:
                    row.append(arr[n - n + k])
        matrix.append(row)
    return matrix


def main():
    xn = mm.input_matrix()
    twiddle_factor = int(input("Enter the twiddle factor for DFT calculation :"))
    twm = tw_matrix(twiddle_factor)
    # print(twm, len(twm))
    mm.multiply_matrices(twm, xn)



