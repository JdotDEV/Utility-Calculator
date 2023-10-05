def time_main():
    import tkinter as t
    from tkinter import messagebox
    from datetime import datetime
    root = t.Tk()
    root.title("Time Zone Conversion")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def time_calc():
        try:
            hours=int(hours_entry.get())
            minutes=int(minutes_entry.get())
            seconds=int(seconds_entry.get())
            ist=f"{hours}:{minutes}:{seconds}"
            est_time="9:30:00"
            pst_time="12:30:00"
            start_time=datetime.strptime(ist, "%H:%M:%S")

            est_diff=datetime.strptime(est_time, "%H:%M:%S")
            pst_diff=datetime.strptime(pst_time, "%H:%M:%S")
            est=start_time-est_diff
            pst=start_time-pst_diff
            
            est_label.config(text=f"IST to EST: {est}")
            pst_label.config(text=f"IST to PST: {pst}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integer values for hours, minutes and seconds.")


    hours_label = t.Label(root, text="Enter the hour: ", font=("Poppins", 15), bg="cyan")
    hours_label.pack()
    hours_entry = t.Entry(root)
    hours_entry.pack()
    minutes_label = t.Label(root, text="Enter the minutes: ", font=("Poppins", 15), bg="cyan")
    minutes_label.pack()
    minutes_entry = t.Entry(root)
    minutes_entry.pack()
    seconds_label = t.Label(root, text="Enter the seconds: ", font=("Poppins", 15), bg="cyan")
    seconds_label.pack()
    seconds_entry = t.Entry(root)
    seconds_entry.pack()

    convert_button = t.Button(root, text="Convert Time Zone", font=("Poppins", 15), command=time_calc)
    convert_button.pack(pady=10)

    est_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    est_label.pack(pady=10)
    pst_label = t.Label(root, text="", font=("Poppins", 15), bg="cyan")
    pst_label.pack(pady=10)
    
    exit_button = t.Button(root, text="Exit", font=("Poppins", 15), command=root.destroy)
    exit_button.pack(pady=10)

    root.mainloop()