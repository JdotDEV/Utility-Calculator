def fuel_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Fuel Efficiency Calculator")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def efficiency_calc():
        try:
            litre_cost = int(litre_entry.get())
            kms = int(kilometer_entry.get())
            litre_price=100
            litre=litre_cost/litre_price
            eff=kms/litre
            eff_rounded=round(eff,2)
            cost=100/eff
            cost_rounded=round(cost,2)
            eff_label.config(text=f"Efficiency: {eff_rounded} kms/litre")
            cost_label.config(text=f"The cost per kilometre is ₹ {cost_rounded}.")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid amount for both quantities.")


    litre_label = t.Label(root, text="Enter the cost of fuel used: ", font=("Poppins", 15), bg="cyan")
    litre_label.pack()
    litre_entry = t.Entry(root)
    litre_entry.pack()

    kilometer_label = t.Label(root, text="Enter the number of kilometres traveled: ", font=("Poppins", 15), bg="cyan")
    kilometer_label.pack()
    kilometer_entry = t.Entry(root)
    kilometer_entry.pack()


    convert_button = t.Button(root, text="Calculate Efficiency", font=("Poppins", 15), command=efficiency_calc)
    convert_button.pack(pady=20)

    eff_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    eff_label.pack(pady=10)
    cost_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    cost_label.pack(pady=5)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()