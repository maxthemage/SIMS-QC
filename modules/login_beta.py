#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def loginWindow():
    #root configurations
    root = Tk()
    root.title("SIMS-QC")
    root.iconbitmap("images/logo.ico")
    root.geometry("375x540")
    root.config(bg="#ffffff")
    root.resizable(width=False, height=False)
    global allowed
    allowed = False 

    #signup button onclick function
    def onClick():
        password_con.grid(column=1, row=8, pady=(15,0))
        confirm_ent.grid(column=1, row=9)
        submit_btn.grid(column=1, row=10, pady=(25,25))
        log_in.config(text="Sign Up")
        sign_up_text.destroy()
        sign_up.destroy()

    #submut button function
    def submit():
            state = log_in.cget("text")
            if state == "Log In":
                tid = teacherid_ent.get() 
                password = password_ent.get()
                if tid == "admin":
                    global allowed
                    allowed = True
                    root.destroy()
            else:
                teacherid = teacherid_ent.get()
                password = password_ent.get()
                confirmed_password = confirm_ent.get()
                if password != confirmed_password:
                    messagebox.showerror("Error", "Passwords do not match")
                else:
                    allowed = True
                    root.destroy()

    #UI widgets in order of display
    sims = Label(root, text="SIMS-QC", bg="#ffffff", font=("Times New Roman", 26), pady=5)
    account_icon = ImageTk.PhotoImage(Image.open("images/account.png"))
    account_img = Label(image=account_icon, bg="#ffffff")
    log_in = Label(root, text="Log In", bg="#ffffff", pady=5, font=("Arial", 25))
    teacher_id = Label(root, text="Teacher ID", bg="#ffffff", font=("Arial", 14))
    teacherid_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
    pass_word = Label(root, text="Password", bg="#ffffff", font=("Arial", 14))
    password_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
    password_con = Label(root, text="Confirm Password", font=("Arial", 14), bg="#ffffff")
    confirm_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
    submit_btn = Button(root, text="Submit", font=("Arial", 13), bg="#138808", fg="#ffffff", width=7, command=submit)
    sign_up_text = Label(root, text="Don't have an account yet? Then sign up.", bg="#ffffff", pady=10)
    sign_up = Button(root, text="Sign Up", fg="#ffffff", bg="#1338be", command=onClick)

    #widgets being displayed using the grid method
    sims.grid(column=1, row=1, ipadx=120)
    account_img.grid(column=1, row=2)
    log_in.grid(column=1, row=3)
    teacher_id.grid(column=1, row=4, pady=(15,0))
    teacherid_ent.grid(column=1, row=5)
    pass_word.grid(column=1, row=6, pady=(15,0))
    password_ent.grid(column=1, row=7)
    submit_btn.grid(column=1, row=8, pady=(25,25))
    sign_up_text.grid(column=1, row=9)
    sign_up.grid(column=1, row=10)

    root.mainloop()
