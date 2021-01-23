#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def onClick():
    password_con = Label(root, text="Confirm Password", font=("Arial", 14))
    confirm_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))    



#root configurations
root = Tk()
root.title("SIMS-QC")
root.iconbitmap("images/logo.ico")
root.geometry("360x480")
root.config(bg="#ffffff")
root.resizable(width=False, height=False)


#UI widgets in order of display
sign_up = Button(root, text="Sign Up", bg="#ffffff", command=onClick)
sims = Label(root, text="SIMS-QC", bg="#ffffff", font=("Times New Roman", 24))
padding_one = Label(root, text="", padx=40, bg="#ffffff")
account_icon = ImageTk.PhotoImage(Image.open("images/account.jpg"))
account_img = Label(image=account_icon)
log_in = Label(root, text="Log In", bg="#ffffff", pady=5, font=("Arial", 25))
padding_two = Label(root, text="", bg="#ffffff")
teacher_id = Label(root, text="Teacher ID", bg="#ffffff", font=("Arial", 14))
teacherid_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
padding_three = Label(root, text="", bg="#ffffff")
pass_word = Label(root, text="Password", bg="#ffffff", font=("Arial", 14))
password_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
padding_four = Label(root, text="", bg="#ffffff", pady=10)
submit_btn = Button(root, text="Submit", font=("Arial", 13), bg="#138808", fg="#ffffff", width=7)


#widgets being displayed using the grid method
sims.grid(column=3, row=1)
padding_one.grid(column=2, row=2)
account_img.grid(column=3, row=2)
log_in.grid(column=3, row=3)
padding_two.grid(column=3, row=4)
teacher_id.grid(column=3, row=5)
teacherid_ent.grid(column=3, row=6)
padding_three.grid(column=3, row=7)
pass_word.grid(column=3, row=8)
password_ent.grid(column=3, row=9)
padding_four.grid(column=3, row=10)
submit_btn.grid(column=3, row=11)



root.mainloop()
