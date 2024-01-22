from tkinter import *
from tkinter import Entry
from bmi import BodyMassIndex as Bmi
from bmr import Bmr


def get_information():
    p2 = Bmr(
        Bmi(name.get(), float(weight.get()), float(height.get())),
        gender.get(),
        int(age.get()),
    )
    p2.save()
    string_val = f"Your bmi is: {str(p2.info()[3])}        {p2.is_right()}"
    my_label = Label(root, text=string_val, bg="grey")
    my_label.pack(pady=10)
    string_val_2 = f"Your bmr is: {str(p2.info()[6])} kcal"
    my_label_2 = Label(root, text=string_val_2, bg="grey")
    my_label_2.pack(pady=10)


root = Tk()
root.geometry("350x350")
root.configure(bg="white")

name = Entry(root, width=50)
name.insert(0, "Enter your name:")
name.bind("<Button-1>", lambda e: name.delete(0, END))
name.pack(pady=10)

gender = Entry(root, width=50)
gender.insert(0, "Enter your gender: [male/female]")
gender.bind("<Button-1>", lambda e: gender.delete(0, END))
gender.pack(pady=10)

weight = Entry(root, width=50)
weight.insert(0, "Enter your weigh: [in kg]")
weight.bind("<Button-1>", lambda e: weight.delete(0, END))
weight.pack(pady=10)

height: Entry = Entry(root, width=50)
height.insert(0, "Enter your height: [in cm]")
height.bind("<Button-1>", lambda e: height.delete(0, END))
height.pack(pady=10)

age = Entry(root, width=50)
age.insert(0, "Enter your age:")
age.bind("<Button-1>", lambda e: age.delete(0, END))
age.pack(pady=10)

myButton = Button(root, width=20, text="OK", bg="white", command=get_information)
myButton.pack(pady=10)

root.mainloop()
