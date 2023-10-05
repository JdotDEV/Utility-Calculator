def age_main():
    import tkinter as t
    from tkinter import messagebox
    from datetime import datetime
    root = t.Tk()
    root.title("Age Calculator")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def calculate_age():
        try:
            day = int(day_entry.get())
            month = int(month_entry.get())
            year = int(year_entry.get())
            today = datetime.today()
            
            birth_date = datetime(year, month, day)
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            
            age_label.config(text=f"Age: {age}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers for day, month, and year.")
    day_label = t.Label(root, text="Enter the day:", font=("Poppins", 15), bg="cyan")
    day_label.grid(row=0, column=0, pady=10, padx=10)
    day_entry = t.Entry(root)
    day_entry.grid(row=0, column=1, pady=10, padx=10)

    month_label = t.Label(root, text="Enter the month:", font=("Poppins", 15), bg="cyan")
    month_label.grid(row=1, column=0, pady=10, padx=10)
    month_entry = t.Entry(root)
    month_entry.grid(row=1, column=1, pady=10, padx=10)

    year_label = t.Label(root, text="Enter the year:", font=("Poppins", 15), bg="cyan")
    year_label.grid(row=2, column=0, pady=10, padx=10)
    year_entry = t.Entry(root)
    year_entry.grid(row=2, column=1, pady=10, padx=10)
    calculate_button = t.Button(root, text="Calculate Age", font=("Poppins", 15), command=calculate_age)
    calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

    age_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    age_label.grid(row=4, column=0, columnspan=2, pady=5)

    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.grid(row=5, column=0, columnspan=2)
    root.mainloop()