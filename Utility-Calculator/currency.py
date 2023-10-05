def currency_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Currency Convertor")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def convert_currency():
        try:
            amount = int(amount_entry.get())
            usd=83.21
            cad=65.12
            inrtousd=float(amount/usd)
            inrtocad=float(amount/cad)
            inrtousd_rounded=round(inrtousd,2)
            inrtocad_rounded=round(inrtocad,2)
            usd_label.config(text=f"INR to USD : ${inrtousd_rounded}")
            cad_label.config(text=f"INR to CAD : ${inrtocad_rounded}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid amount.")


    amount_label = t.Label(root, text="Enter your amount in ₹: ", font=("Poppins", 15), bg="cyan")
    amount_label.grid(row=0, column=0, pady=10, padx=10)
    amount_entry = t.Entry(root)
    amount_entry.grid(row=0, column=1, pady=10, padx=10)


    convert_button = t.Button(root, text="Convert Currency", font=("Poppins", 15), command=convert_currency)
    convert_button.grid(row=3, column=0, columnspan=2, pady=20)

    usd_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    usd_label.grid(row=4, column=0, columnspan=2, pady=10)
    cad_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    cad_label.grid(row=5, column=0, columnspan=2, pady=10)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.grid(row=5, column=0, columnspan=2)

    root.mainloop()