
import twiddle as t
import MatrixMultiplication as mm


def run():
    print("******************************* *******************************")
    key = int(input(" Enter 1 to Calculate the DFT of any discrete sequence---\n "
                    "Enter 2 to Calculate the Inverse DFT of any fourier sequence---\n "
                    "Enter 0 to Terminate    :"))
    print("******************************* *******************************")
    flag = True
    while flag:
        if key == 1:
            xn = mm.input_matrix()
            twiddle_factor = int(input("Enter the twiddle factor for DFT calculation :"))
            twm = t.tw_matrix(twiddle_factor)
            mm.multiply_matrices(twm, xn)
        elif key == 2:
            t.inverse_dft()

        elif key == 0:
            break
        else:
            print("Please enter a valid key")

        print("******************************* *******************************")
        key = int(input(" Enter 1 to Calculate the DFT of any discrete sequence---\n "
                        "Enter 2 to Calculate the Inverse DFT of any fourier sequence---\n "
                        "Enter 0 to Terminate    :"))
        print("******************************* *******************************")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
