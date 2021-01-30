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
create_btn = Button(root, text="Create new record", font=("Arial", 13), padx=109, pady=15)
padding_two = Label(root, text="", font=("Arial", 3), bg="#ffffff")
view_btn = Button(root, text="View existing records", font=("Arial", 13), padx=100, pady=15)
padding_three = Label(root, text="", font=("Arial", 3), bg="#ffffff")
update_btn = Button(root, text="Update records", font=("Arial", 13), padx=121, pady=15)
padding_four = Label(root, text="", font=("Arial", 2), bg="#ffffff")
delete_btn = Button(root, text="Delete records", font=("Arial", 13), pady=13, padx=2)
generate_btn = Button(root, text="Report Cards", font=("Arial", 13), padx=7, pady=13)
exit_btn = Button(root, text="Exit", font=("Arial", 13), padx=35, pady=13)



padding_one.grid(column=1, row=1)
logo.grid(column=2, row=2)
heading.grid(column=2, row=3)
create_btn.grid(column=2, row=4)
padding_two.grid(column=2, row=5)
view_btn.grid(column=2, row=6)
padding_three.grid(column=2, row=7)
update_btn.grid(column=2, row=8)
padding_four.grid(column=2, row=9)
delete_btn.grid(column=2, row=10, padx=(0,243))
generate_btn.grid(column=2, row=10, columnspan=1, padx=(15,0))
exit_btn.grid(column=2, row=10, columnspan=2, padx=(259,0)
