# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import twiddle as t
import MatrixMultiplication as mm


def run():
    xn = mm.input_matrix()
    twiddle_factor = int(input("Enter the twiddle factor for DFT calculation :"))
    twm = t.tw_matrix(twiddle_factor)
    mm.multiply_matrices(twm, xn)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()


