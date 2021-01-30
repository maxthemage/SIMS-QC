#!/usr/bin/env python

from tkinter import *
import random

root = Tk()
root.title("Display")
root.iconbitmap("images/logo.ico")
root.geometry("1030x500")


heads = ["Student ID", "First name", "Last name", "Gender", "DOB", "Address", "Enrol. Date", "Email", "Contact #"]
char = "QC1A"
sid = 93550
emails = ["grossman@msn.com", "hardin@comcast.net", "aaribaud@gmail.com", "hikoza@me.com", "microfab@me.com", "melnik@gmail.com", "morain@comcast.net", "yamla@icloud.com", "salesgeek@hotmail.com","drewf@verizon.net", "lipeng@me.com", "johnh@comcast.net", "policies@att.net", "munge@yahoo.com", "dcoppit@verizon.net", "fairbank@yahoo.com", "gordonjcp@aol.com", "mkearl@gmail.com","aegreene@icloud.com","bowmanbs@hotmail.com"]
fnames = ["Beverly", "Cathryn", "Robbi", "Al", "Sterling", "Jamee", "Desirae", "Vonnie", "Melynda", "Rocio", "Dara", "Marissa", "Delila", "Catherin", "Agustina",  "Nichole", "Faries",  "Elena", "Corinna",  "Rusty"]
lnames = ["Frakes", "Mankin", "Denby", "Forsman", "Schwartzkopf", "Hallinan", "Castenada", "Zoller", "Calderon", "Bence", "Matis", "Scherf", "Longnecker", "Fedele", "Aceto", "Mclachlan", "Augusta", "Kahle", "Nell", "Needles"]
gender = ["male", "female"]
date = "2021-01-24"
number = 5926089341
dummy = "###########"


display_frame = LabelFrame(root, bg = "#ffffff")
display_head = Label(root, text="Student Records", font=("Times New Roman", 18))
padding_one = Label(root, text="")
search_img = PhotoImage(file="loupe.png")
search_lbl = Label(image=search_img)
search_ent = Entry(root, width=15, font=("Times New Roman", 11))
search_btn = Button(root, text="Search", font=("Arial", 9))
#display_frame.grid(column=0, row=0)
#display_head.grid(column=0,row=0)
padding_one.grid(column=6, row=0)
search_ent.grid(column=7, row=0)
search_btn.grid(column=8, row=0)




for i in range(len(heads)):
    label = Label(root, text=heads[i], padx=20, pady=10, font=("Times New Roman", 14))
    label.grid(column=i, row=1)

for i in range(1, len(fnames)):
    studentid_lbl = Label(root, text=char + str((sid+10)), font=("Arial", 8))
    fname_lbl = Label(root, text=fnames[i], font=("Arial", 8))
    lname_lbl = Label(root, text=lnames[i], font=("Arial", 8))
    gender_lbl = Label(root, text=gender[random.randint(0,1)], font=("Arial", 8))
    dob_lbl = Label(root, text=date, font=("Arial", 8))
    address_lbl = Label(root, text=dummy, font=("Arial", 8))
    enrol_lbl = Label(root, text=date, font=("Arial", 8))
    email_lbl = Label(root, text=emails[i], font=("Arial", 8))
    contact_lbl = Label(root, text=str(number+1000), font=("Arial", 8))
    studentid_lbl.grid(column=0, row=i+1)     
    fname_lbl.grid(column=1, row=i+1)
    lname_lbl.grid(column=2, row=i+1)
    gender_lbl.grid(column=3, row=i+1)
    dob_lbl.grid(column=4, row=i+1)
    address_lbl.grid(column=5, row=i+1)
    enrol_lbl.grid(column=6, row=i+1)
    email_lbl.grid(column=7, row=i+1)
    contact_lbl.grid(column=8, row=i+1)
    
   






