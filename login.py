#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
  
        
#root configurations
root = Tk()
root.title("SIMS-QC")
root.iconbitmap("images/logo.ico")
root.geometry("375x540")
root.config(bg="#ffffff")
root.resizable(width=False, height=False)


#signup button onclick function
def onClick():
    padding_four.grid(column=3, row=10)
    password_con.grid(column=3, row=11)
    confirm_ent.grid(column=3, row=12)
    log_in.config(text="Sign Up")
    padding_six.destroy()
    sign_up.destroy()
    padding_one.config(padx=42)
  

#submut button function
def submit():
        state = log_in.cget("text")
        #print(state)
        if state == "Log In":
            teacherid = teacherid_ent.get() 
            password = password_ent.get()
        else:
            teacherid = teacherid_ent.get()
            password = password_ent.get()
            confirmed_password = confirm_ent.get()
            if password != confirmed_password:
                messagebox.showerror("Error", "Passwords do not match")
            else:
                pass


#UI widgets in order of display
sims = Label(root, text="SIMS-QC", bg="#ffffff", font=("Times New Roman", 25), pady=5)
padding_one = Label(root, text="", padx=37, bg="#ffffff")
account_icon = ImageTk.PhotoImage(Image.open("images/account.png"))
account_img = Label(image=account_icon, bg="#ffffff")
log_in = Label(root, text="Log In", bg="#ffffff", pady=5, font=("Arial", 25))
padding_two = Label(root, text="", bg="#ffffff")
teacher_id = Label(root, text="Teacher ID", bg="#ffffff", font=("Arial", 14))
teacherid_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
padding_three = Label(root, text="", bg="#ffffff")
pass_word = Label(root, text="Password", bg="#ffffff", font=("Arial", 14))
password_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
padding_four = Label(root, text="", padx=5, bg="#ffffff")
password_con = Label(root, text="Confirm Password", font=("Arial", 14), bg="#ffffff")
confirm_ent = Entry(root, width=25, bg="#fafafa", font=("Times New Roman", 12))
padding_five = Label(root, text="", bg="#ffffff", pady=10)
submit_btn = Button(root, text="Submit", font=("Arial", 13), bg="#138808", fg="#ffffff", width=7, command=submit)
padding_six = Label(root, text="Don't have an account yet? Then sign up.", bg="#ffffff", pady=15)
sign_up = Button(root, text="Sign Up", fg="#ffffff", bg="#1338be", command=onClick)



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
padding_five.grid(column=3, row=13)
submit_btn.grid(column=3, row=14)
padding_six.grid(column=3, row=15)
sign_up.grid(column=3, row=16)


root.mainloop()
