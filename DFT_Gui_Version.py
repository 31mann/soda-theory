"""
Hey This code is for calculating the dft of any 2-D signal,it uses a row wise and column wise matrix multiplication
with twiddle factor of  its corresponding given sequence, Well the application of this code is very narrow
(UG & PG Engineer)because this code just for finding the answer quickly and easily which is rather very boring and
inefficient ://

Hope this is useful for you :)
"""


import tkinter as tk
from dftimage import dft_calculate1  # Import the dft_calculate function


background_color = "#FAEBD7"  # Cream
button_bg = "#D35400"  # Subtle Brown
button_fg = "#FFFFFF"  # White

def create_matrix_input_window(matrix_size, main_window):
    def capture_data():
        for i in range(matrix_size):
            for j in range(matrix_size):
                data[i][j] = int(entry_boxes[i][j].get())

    def save_data():
        capture_data()
        display_matrix_data(data)
        matrix_window.destroy()  # Close the matrix input window after saving data

    def calculate_dft():
        capture_data()
        result_matrix = dft_calculate1(matrix_size, data)
        display_dft_result(result_matrix)

    matrix_window = tk.Toplevel(main_window)
    matrix_window.title("Matrix Input")
    matrix_window.configure(bg=background_color)

    # Create a 2D list to store the data
    data = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    # Create a label for matrix input
    label = tk.Label(matrix_window, text=f"Enter {matrix_size}x{matrix_size} Matrix:", bg=background_color)
    label.pack(pady=10)

    # Create a matrix of entry boxes for user input
    entry_boxes = []
    for i in range(matrix_size):
        row_entries = []
        entry_frame = tk.Frame(matrix_window, bg=background_color)
        entry_frame.pack()
        for j in range(matrix_size):
            entry = tk.Entry(entry_frame, width=6)
            entry.grid(row=i, column=j, padx=5, pady=5)
            row_entries.append(entry)
        entry_boxes.append(row_entries)

    save_button = tk.Button(matrix_window, text="Save", command=save_data, bg=button_bg, fg=button_fg, activebackground="#A04000", activeforeground="white")
    save_button.pack(pady=10)

    calculate_button = tk.Button(matrix_window, text="Calculate DFT", command=calculate_dft, bg=button_bg, fg=button_fg, activebackground="#A04000", activeforeground="white")
    calculate_button.pack(pady=10)

def display_matrix_data(data):
    print("Matrix Data:")
    for row in data:
        print(row)

def display_dft_result(result_matrix):
    result_window = tk.Toplevel()
    result_window.title("DFT Result")
    result_window.configure(bg=background_color)

    label = tk.Label(result_window, text="DFT Result Matrix:", bg=background_color)
    label.pack(pady=10)

    for row in result_matrix:
        row_label = tk.Label(result_window, text=row, bg=background_color)
        row_label.pack()

def main():
    main_window = tk.Tk()
    main_window.title("Matrix Calculator")
    main_window.configure(bg=background_color)

    label = tk.Label(main_window, text="Enter the matrix size:", bg=background_color)
    label.pack(pady=10)

    matrix_size_entry = tk.Entry(main_window)
    matrix_size_entry.pack()

    def on_submit():
        try:
            size = int(matrix_size_entry.get())
            if size > 0:
                create_matrix_input_window(size, main_window)
            else:
                print("Invalid matrix size.")
        except ValueError:
            print("Please enter a valid number.")

    submit_button = tk.Button(main_window, text="Submit", command=on_submit, bg=button_bg, fg=button_fg, activebackground="#A04000", activeforeground="white")
    submit_button.pack(pady=10)

    main_window.mainloop()

if __name__ == "__main__":
    main()
