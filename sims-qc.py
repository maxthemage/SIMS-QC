#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("SIMS-QC")
root.iconbitmap("images/logo.ico")
root.geometry("800x600")
root.config(bg="#ffffff")
root.resizable(width=False, height=False)


padding_one = Label(root, text="", padx=110, bg="#ffffff")
logo_img = ImageTk.PhotoImage(Image.open("images/qc_logo.jpg"))
logo = Label(image=logo_img, bg="#ffffff")
heading = Label(root, text="Welcome to SIMS-QC 1.0.1", font=("Times New Roman", 25), bg="#ffffff", pady=10)
create_btn = Button(root, text="Create new record", font=("Arial", 13), padx=109, pady=9)
padding_two = Label(root, text="", font=("Arial", 3), bg="#ffffff")
view_btn = Button(root, text="View existing records", font=("Arial", 13), padx=100, pady=9)
padding_three = Label(root, text="", font=("Arial", 3), bg="#ffffff")
update_btn = Button(root, text="Update records", font=("Arial", 13), padx=121, pady=9)
padding_four = Label(root, text="4")
padding_five = Label(root, text="5", font=("Arial", 2))
delete_btn = Button(root, text="Delete records", font=("Arial", 13))
padding_six = Label(root, text="6", font=("Arial", 2))
generate_btn = Button(root, text="Generate report")
padding_seven = Label(root, text="7", font=("Arial", 2))
exit_btn = Button(root, text="Exit")



padding_one.grid(column=1, row=1)
logo.grid(column=2, row=2)
heading.grid(column=2, row=3)
create_btn.grid(column=2, row=4)
padding_two.grid(column=2, row=5)
view_btn.grid(column=2, row=6)
padding_three.grid(column=2, row=7)
update_btn.grid(column=2, row=8)
#padding_four.grid(column=2, row=9)
#padding_five.grid(column=1, row=10)
#delete_btn.grid(column=2, row=10)
#padding_six.grid(column=3, row=10)
#padding_six.grid()
#generate_btn.grid(column=4, row=10)
#padding_seven.grid(column=5, row=10)
#exit_btn.grid(column=6, row=10)









