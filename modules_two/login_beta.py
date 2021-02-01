#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time

def loginWindow():
    #root configurations
    root = Tk()
    root.title("SIMS-QC")
    root.iconbitmap("images/logo.ico")
    root.geometry("350x440")
    root.config(bg="#ffffff")
    root.resizable(width=False, height=False)
    global allowed
    allowed = False
    global username
    username = ""


    #submut button function
    def submit():
            state = log_in.cget("text")
            if state == "Log In":
                tid = teacherid_ent.get() 
                password = password_ent.get()
                if tid == "admin":
                    global allowed
                    allowed = True
                    global username
                    username = tid
                    root.destroy()
                    time.sleep(1)
                else:
                    allowed = True
                    username = tid
                    root.destroy()
                    time.sleep(1)

    #UI widgets in order of display
    sims = Label(root, text="SIMS-QC", bg="#ffffff", font=("Times New Roman", 26), pady=5)
    account_icon = ImageTk.PhotoImage(Image.open("images/account.png"))
    account_img = Label(image=account_icon, bg="#ffffff")
    log_in = Label(root, text="Log In", bg="#ffffff", pady=5, font=("Arial", 25))
    teacher_id = Label(root, text="Teacher ID", bg="#ffffff", font=("Arial", 14))
    teacherid_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
    pass_word = Label(root, text="Password", bg="#ffffff", font=("Arial", 14))
    password_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12), show="*")
    password_con = Label(root, text="Confirm Password", font=("Arial", 14), bg="#ffffff")
    confirm_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
    submit_btn = Button(root, text="Submit", font=("Arial", 13), bg="#138808", fg="#ffffff", width=7, command=submit)

    #widgets being displayed using the grid method
    sims.grid(column=1, row=1, ipadx=105)
    account_img.grid(column=1, row=2)
    log_in.grid(column=1, row=3)
    teacher_id.grid(column=1, row=4, pady=(15,0))
    teacherid_ent.grid(column=1, row=5)
    pass_word.grid(column=1, row=6, pady=(15,0))
    password_ent.grid(column=1, row=7)
    submit_btn.grid(column=1, row=8, pady=(25,25))

    root.mainloop()
