def loan_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Loan Calculator")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def loan_calc():
        try:
            amount=int(amount_entry.get())
            rate=float(rate_entry.get())
            time=float(time_entry.get())
            interest=(amount*rate*time)/100
            total_interest=(amount + (amount*rate*time)/100)
            
            interest_label.config(text=f"Your Interest Amount: %.2f" % interest)
            total_label.config(text=f"Your Total Amount with interest: %.2f" % total_interest)


        except ValueError:
            messagebox.showerror("Error", "Please enter valid figures for amount, rate and time.")


    amount_label = t.Label(root, text="Enter the loan amount: ", font=("Poppins", 15), bg="cyan")
    amount_label.pack()
    amount_entry = t.Entry(root)
    amount_entry.pack()

    rate_label = t.Label(root, text="Enter the interest rate: ", font=("Poppins", 15), bg="cyan")
    rate_label.pack()
    rate_entry = t.Entry(root)
    rate_entry.pack()

    time_label = t.Label(root, text="Enter the loan duration in years: ", font=("Poppins", 15), bg="cyan")
    time_label.pack()
    time_entry = t.Entry(root)
    time_entry.pack()

    calculate_button = t.Button(root, text="Calculate Total Amount", font=("Poppins", 15), command=loan_calc)
    calculate_button.pack(pady=10)

    interest_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    interest_label.pack(pady=10)
    total_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    total_label.pack(pady=10)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)
    root.mainloop()