def bmi_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("BMI Calculator")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def calculate_bmi():
        try:
            w = int(weight_entry.get())
            h = int(height_entry.get())
            
            bmi=float((w/(h/100)**2))
            bmi_rounded =round(bmi,2)
            bmi_label.config(text=f"BMI: {bmi_rounded}")
            if bmi_rounded < 18.5:
                bmi_category.config(text=f"You are underweight.")
            elif bmi_rounded < 25:
                bmi_category.config(text=f"You are in normal range.")
            elif bmi_rounded < 30:
                bmi_category.config(text=f"You are overweight.")
            else:
                bmi_category.config(text=f"You are obese.")


        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for height and weight.")


    weight_label = t.Label(root, text="Enter your weight in kg: ", font=("Poppins", 15), bg="cyan")
    weight_label.grid(row=0, column=0, pady=10, padx=10)
    weight_entry = t.Entry(root)
    weight_entry.grid(row=0, column=1, pady=10, padx=10)

    height_label = t.Label(root, text="Enter your height in cm: ", font=("Poppins", 15), bg="cyan")
    height_label.grid(row=1, column=0, pady=10, padx=10)
    height_entry = t.Entry(root)
    height_entry.grid(row=1, column=1, pady=10, padx=10)

    calculate_button = t.Button(root, text="Calculate BMI", font=("Poppins", 15), command=calculate_bmi)
    calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

    bmi_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    bmi_label.grid(row=4, column=0, columnspan=2, pady=10)
    bmi_category = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    bmi_category.grid(row=5, column=0, columnspan=2, pady=10)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.grid(row=5, column=0, columnspan=2)
    root.mainloop()