def random_main():
    import tkinter as t
    import random
    from tkinter import messagebox
    root = t.Tk()
    root.title("Percentage Calculator")
    root.geometry("570x450")
    root.configure(bg="cyan")

    def rand_num():
        try:
            num1=int(num1_entry.get())
            num2=int(num2_entry.get())
            limit=int(limit_entry.get())
            nums=[]
            for i in range(limit):
                x=random.randint(num1,num2)
                nums.append(x)
            random_label.config(text=f"Number Genereated: {nums}")
            

        except ValueError:
            messagebox.showerror("Error", "Please enter valid integers.")


    num1_label = t.Label(root, text="Enter the lower limit: ", font=("Poppins", 15), bg="cyan")
    num1_label.pack()
    num1_entry = t.Entry(root)
    num1_entry.pack()
    num2_label = t.Label(root, text="Enter the upper limit: ", font=("Poppins", 15), bg="cyan")
    num2_label.pack()
    num2_entry = t.Entry(root)
    num2_entry.pack()

    limit_label = t.Label(root, text="Times number should be generated: ", font=("Poppins", 15), bg="cyan")
    limit_label.pack()
    limit_entry = t.Entry(root)
    limit_entry.pack()

    generate_button = t.Button(root, text="Generate Numbers", font=("Poppins", 15), command=rand_num)
    generate_button.pack(pady=10)

    random_label = t.Label(root, text="", font=("Poppins", 10), bg="cyan")
    random_label.pack(pady=10)

    root.mainloop()