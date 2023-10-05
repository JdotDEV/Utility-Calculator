def perc_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Percentage Calculator")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def perc_calc():
        try:
            num1=int(num1_entry.get())
            num2=int(num2_entry.get())
            num3=int(num3_entry.get())
            num4=int(num4_entry.get())
            num5=int(num5_entry.get())
            perc=((num1+num2+num3+num4+num5)/5)
            percentage_label.config(text=f"Percentage obtained: %.2f" % perc)
            

        except ValueError:
            messagebox.showerror("Error", "Please enter valid marks.")


    num1_label = t.Label(root, text="Enter marks for PSC: ", font=("Poppins", 15), bg="cyan")
    num1_label.pack()
    num1_entry = t.Entry(root)
    num1_entry.pack()
    num2_label = t.Label(root, text="Enter marks for CN: ", font=("Poppins", 15), bg="cyan")
    num2_label.pack()
    num2_entry = t.Entry(root)
    num2_entry.pack()
    num3_label = t.Label(root, text="Enter marks for AMP: ", font=("Poppins", 15), bg="cyan")
    num3_label.pack()
    num3_entry = t.Entry(root)
    num3_entry.pack()
    num4_label = t.Label(root, text="Enter marks for DAA: ", font=("Poppins", 15), bg="cyan")
    num4_label.pack()
    num4_entry = t.Entry(root)
    num4_entry.pack()
    num5_label = t.Label(root, text="Enter marks for WT: ", font=("Poppins", 15), bg="cyan")
    num5_label.pack()
    num5_entry = t.Entry(root)
    num5_entry.pack()

    calculate_button = t.Button(root, text="Calculate Percentage", font=("Poppins", 15), command=perc_calc)
    calculate_button.pack(pady=10)

    percentage_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    percentage_label.pack(pady=10)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()