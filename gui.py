import tkinter as tk
from tkinter import messagebox

def show_dialog():
    messagebox.showinfo("Custom Dialog", "This is a custom dialog box!")

def submit():
    name = name_entry.get()
    gender = gender_var.get()
    hobbies = ""
    if coding_var.get():
        hobbies += "Coding "
    if reading_var.get():
        hobbies += "Reading "
    if gaming_var.get():
        hobbies += "Gaming"
    result_label.config(text=f"Name: {name}\nGender: {gender}\nHobbies: {hobbies}")


root = tk.Tk()
root.title("Python GUI")


name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)


gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=1, column=0, sticky="w")
gender_var = tk.StringVar()
male_radio = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=1, column=1, sticky="w")
female_radio = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=1, column=2, sticky="w")


hobbies_label = tk.Label(root, text="Hobbies:")
hobbies_label.grid(row=2, column=0, sticky="w")
coding_var = tk.BooleanVar()
coding_check = tk.Checkbutton(root, text="Coding", variable=coding_var)
coding_check.grid(row=2, column=1, sticky="w")
reading_var = tk.BooleanVar()
reading_check = tk.Checkbutton(root, text="Reading", variable=reading_var)
reading_check.grid(row=2, column=2, sticky="w")
gaming_var = tk.BooleanVar()
gaming_check = tk.Checkbutton(root, text="Gaming", variable=gaming_var)
gaming_check.grid(row=2, column=3, sticky="w")


submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.grid(row=3, column=0)


result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0)


dialog_button = tk.Button(root, text="Show Dialog", command=show_dialog)
dialog_button.grid(row=5, column=0)


root.mainloop()
