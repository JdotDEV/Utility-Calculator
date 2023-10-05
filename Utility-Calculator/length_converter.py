def length_main():
    import tkinter as t
    from tkinter import messagebox
    root = t.Tk()
    root.title("Length Convertor")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def convert_length():
        try:
            length = float(length_entry.get())
            millimeters=length * 1000
            centimeters=length * 100
            inches=length * 39.3701
            foot=length * 3.28084
            yards=length * 1.09361
            miles=length * 0.000621371
            kilometers=length * 0.001 

            millimeters_label.config(text=f"Meter to Millimeters: %.2f" % millimeters)
            centimeters_label.config(text=f"Meter to Centimeters: %.2f" % centimeters)
            inches_label.config(text=f"Meter to Inches: %.2f" % inches)
            foot_label.config(text=f"Meter to Foots: %.2f" % foot)
            yards_label.config(text=f"Meter to Yards: %.2f" % yards)
            miles_label.config(text=f"Meter to Miles: %.2f" % miles)
            kilometers_label.config(text=f"Meter to Kilometers: %.2f" % kilometers)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid value of length.")


    length_label = t.Label(root, text="Enter the length in meters: ", font=("Poppins", 15), bg="cyan")
    length_label.pack()
    length_entry = t.Entry(root)
    length_entry.pack()

    convert_button = t.Button(root, text="Convert Length", font=("Poppins", 15), command=convert_length)
    convert_button.pack(pady=20)

    millimeters_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    millimeters_label.pack(pady=3)
    centimeters_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    centimeters_label.pack(pady=3)
    inches_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    inches_label.pack(pady=3)
    foot_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    foot_label.pack(pady=3)
    yards_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    yards_label.pack(pady=3)
    miles_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    miles_label.pack(pady=3)
    kilometers_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    kilometers_label.pack(pady=3)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()