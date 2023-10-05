def calc_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Basic Calculator")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def calc():
        try:
            num1=int(num1_entry.get())
            num2=int(num2_entry.get())
            operator=operator_entry.get()
            if operator == "+":
                total_label.config(text=f"Addition: %.2f" % (num1 + num2))
            elif operator == "-":
                total_label.config(text=f"Subtraction: %.2f" % (num1 - num2))
            elif operator == "*":
                total_label.config(text=f"Multiplication: %.2f" % (num1 * num2))
            elif operator == "/":
                total_label.config(text=f"Division: %.2f" % (num1 / num2))
            elif operator == "%":
                total_label.config(text=f"Modulus: %.2f" % (num1 % num2))
            else:
                total_label.config(text=f"Enter a valid operator.")
            

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for performing calculations.")


    num1_label = t.Label(root, text="Enter the first number: ", font=("Poppins", 15), bg="cyan")
    num1_label.pack()
    num1_entry = t.Entry(root)
    num1_entry.pack()

    num2_label = t.Label(root, text="Enter the second number: ", font=("Poppins", 15), bg="cyan")
    num2_label.pack()
    num2_entry = t.Entry(root)
    num2_entry.pack()

    operator_label = t.Label(root, text="Enter the operator(+,-,*,/,%): ", font=("Poppins", 15), bg="cyan")
    operator_label.pack()
    operator_entry = t.Entry(root)
    operator_entry.pack()

    calculate_button = t.Button(root, text="Calculate Output", font=("Poppins", 15), command=calc)
    calculate_button.pack(pady=10)

    total_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    total_label.pack(pady=10)

    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)
    root.mainloop()