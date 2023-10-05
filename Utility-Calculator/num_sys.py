def numsys_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Number System Conversion")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def convert_numsys():
        try:
            num=int(num_entry.get())
            binary_label.config(text=f"Decimal to Binary :{ bin(num)}")
            octal_label.config(text=f"Decimal to Octal :{ oct(num)}")
            hexadecimal_label.config(text=f"Decimal to Hexadecimal :{ hex(num)}")
            

        except ValueError:
            messagebox.showerror("Error", "Please enter valid decimal number.")


    num_label = t.Label(root, text="Enter a decimal number: ", font=("Poppins", 15), bg="cyan")
    num_label.pack()
    num_entry = t.Entry(root)
    num_entry.pack()

    convert_button = t.Button(root, text="Convert number", font=("Poppins", 15), command=convert_numsys)
    convert_button.pack(pady=10)

    binary_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    binary_label.pack(pady=10)
    octal_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    octal_label.pack(pady=10)
    hexadecimal_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    hexadecimal_label.pack(pady=10)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()