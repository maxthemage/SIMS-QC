#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

#root configurations
root = Tk()
root.title("SIMS-QC")
root.iconbitmap("images/logo.ico")
root.geometry("360x480")
root.config(bg="#ffffff")
root.resizable(width=False, height=False)


#UI widgets in order of display
padding_one = Label(root, text="", bg="#ffffff")
padding_two = Label(root, text="", padx=40, bg="#ffffff")
account_icon = ImageTk.PhotoImage(Image.open("images/account.jpg"))
account_img = Label(image=account_icon)
log_in = Label(root, text="Log In", bg="#ffffff", pady=5, font=("Arial", 25))
padding_three = Label(root, text="", bg="#ffffff")
teacher_id = Label(root, text="Teacher ID", bg="#ffffff", font=("Arial", 14))
teacherid_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
padding_four = Label(root, text="", bg="#ffffff")
pass_word = Label(root, text="Password", bg="#ffffff", font=("Arial", 14))
password_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
padding_five = Label(root, text="", bg="#ffffff", pady=10)
submit_btn = Button(root, text="Submit", font=("Arial", 13), bg="#138808", fg="#ffffff", width=7)


#widgets being displayed using the grid method
padding_one.grid(column=3, row=1)
padding_two.grid(column=2, row=2)
account_img.grid(column=3, row=2)
log_in.grid(column=3, row=3)
padding_three.grid(column=3, row=4)
teacher_id.grid(column=3, row=5)
teacherid_ent.grid(column=3, row=6)
padding_four.grid(column=3, row=7)
pass_word.grid(column=3, row=8)
password_ent.grid(column=3, row=9)
padding_five.grid(column=3, row=10)
submit_btn.grid(column=3, row=11)
