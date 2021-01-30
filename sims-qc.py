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


logo_img = ImageTk.PhotoImage(Image.open("images/qc_logo.jpg"))
logo = Label(image=logo_img, bg="#ffffff")
heading = Label(root, text="Welcome to SIMS-QC 1.0.1", font=("Times New Roman", 25), bg="#ffffff", pady=10)
create_btn = Button(root, text="Create new record", font=("Arial", 13), padx=109, pady=15)
view_btn = Button(root, text="View existing records", font=("Arial", 13), padx=100, pady=15)
update_btn = Button(root, text="Update records", font=("Arial", 13), padx=121, pady=15)
delete_btn = Button(root, text="Delete records", font=("Arial", 13), pady=13, padx=2)
generate_btn = Button(root, text="Report Cards", font=("Arial", 13), padx=7, pady=13)
exit_btn = Button(root, text="Exit", font=("Arial", 13), padx=35, pady=13)


logo.grid(column=1, row=1, ipadx=300)
heading.grid(column=1, row=2)
create_btn.grid(column=1, row=3, pady=(0, 7))
view_btn.grid(column=1, row=5, pady=(0, 7))
update_btn.grid(column=1, row=7, pady=(0, 7))
delete_btn.grid(column=1, row=9, padx=(0,243))
generate_btn.grid(column=1, row=9, columnspan=1, padx=(15,0))
exit_btn.grid(column=1, row=9, columnspan=2, padx=(259,0))









