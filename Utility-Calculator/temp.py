def temp_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Temperature Conversion")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def temp_calc():
        try:
            celsius=int(celsius_entry.get())
            farh= (celsius* 9/5) + 32
            kelvin=celsius+273.15
            farehnheit_label.config(text=f"Celsius to Fahrenheit: %.2f" % farh)
            kelvin_label.config(text=f"Celsius to Kelvin: %.2f" % kelvin)
            

        except ValueError:
            messagebox.showerror("Error", "Please enter valid temperature.")


    celsius_label = t.Label(root, text="Enter the temperature in celsius: ", font=("Poppins", 15), bg="cyan")
    celsius_label.pack()
    celsius_entry = t.Entry(root)
    celsius_entry.pack()

    convert_button = t.Button(root, text="Convert Temperature", font=("Poppins", 15), command=temp_calc)
    convert_button.pack(pady=10)

    farehnheit_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    farehnheit_label.pack(pady=10)
    kelvin_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    kelvin_label.pack(pady=10)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()