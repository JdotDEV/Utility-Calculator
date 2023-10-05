from age_calc import age_main
from bmi import bmi_main
from currency import currency_main
from fuel import fuel_main
from length_converter import length_main
from loan import loan_main
from perc import perc_main
from rand_num import random_main
from time_zone import time_main
from temp import temp_main
from normal_calculator import calc_main
from num_sys import numsys_main

import tkinter as t
root=t.Tk()
root.geometry("570x450")
root.minsize(570, 450)
root.maxsize(570, 450)   
root.title("UTITLITY CALCULATOR")
root.configure(bg="skyblue") 
l1=t.Label(root, text="Welcome to the Utility Calculator, User.", font=("Poppins",20,"bold"), bg="skyblue", fg="#FCA311")   
l1.pack(pady=20)     

buttonframe=t.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)

b1=t.Button(buttonframe, text="Age Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=age_main)
b1.grid(row=0, column=0, sticky=t.W+ t.E)
b2=t.Button(buttonframe, text="BMI Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=bmi_main)
b2.grid(row=1, column=0, sticky=t.W+ t.E)
b3=t.Button(buttonframe, text="Currency Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=currency_main)
b3.grid(row=2, column=0, sticky=t.W+ t.E)
b4=t.Button(buttonframe, text="Fuel Efficiency Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=fuel_main)
b4.grid(row=3, column=0, sticky=t.W+ t.E)
b5=t.Button(buttonframe, text="Length Converter", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=length_main)
b5.grid(row=4, column=0, sticky=t.W+ t.E)
b6=t.Button(buttonframe, text="Loan Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=loan_main)
b6.grid(row=5, column=0, sticky=t.W+ t.E)

b7=t.Button(buttonframe, text="Basic Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=calc_main)
b7.grid(row=0, column=1, sticky=t.W+ t.E)
b8=t.Button(buttonframe, text="Number System Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=numsys_main)
b8.grid(row=1, column=1, sticky=t.W+ t.E)
b9=t.Button(buttonframe, text="Percentage Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=perc_main)
b9.grid(row=2, column=1, sticky=t.W+ t.E)
b10=t.Button(buttonframe, text="Random Number Generator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=random_main)
b10.grid(row=3, column=1, sticky=t.W+ t.E)
b14=t.Button(buttonframe, text="Temperature Calculator", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=temp_main)
b14.grid(row=4, column=1, sticky=t.W+ t.E)
b12=t.Button(buttonframe, text="Time Zone Converter", font=("Poppins",14), bg="#E5E5E5",fg="#14213D", command=time_main)
b12.grid(row=5, column=1, sticky=t.W+ t.E)

buttonframe.pack(fill="both")
t.mainloop()