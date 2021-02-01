#!/usr/bin/env python

from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

def displayStudent():
    #Root window configurations
    root = Tk()
    root.title("View Student Records")
    root.iconbitmap("images/logo.ico")
    root.geometry("1170x600")
    root.config(bg="#ffffff")
    root.resizable(width=False, height=False)


    #Dummy data for Treeview
    heads = ["Student ID", "First name", "Last name", "Gender", "DOB", "Address", "Enrol. Date", "Email", "Contact #"]
    char = "QC1A"
    sid = 93550
    emails = ["grossman@msn.com", "hardin@comcast.net", "aaribaud@gmail.com", "hikoza@me.com", "microfab@me.com", "melnik@gmail.com", "morain@comcast.net", "yamla@icloud.com", "salesgeek@hotmail.com","drewf@verizon.net", "lipeng@me.com", "johnh@comcast.net", "policies@att.net", "munge@yahoo.com", "dcoppit@verizon.net", "fairbank@yahoo.com", "gordonjcp@aol.com", "mkearl@gmail.com","aegreene@icloud.com","bowmanbs@hotmail.com"]
    fnames = ["Beverly", "Cathryn", "Robbi", "Al", "Sterling", "Jamee", "Desirae", "Vonnie", "Melynda", "Rocio", "Dara", "Marissa", "Delila", "Catherin", "Agustina",  "Nichole", "Faries",  "Elena", "Corinna",  "Rusty"]
    lnames = ["Frakes", "Mankin", "Denby", "Forsman", "Schwartzkopf", "Hallinan", "Castenada", "Zoller", "Calderon", "Bence", "Matis", "Scherf", "Longnecker", "Fedele", "Aceto", "Mclachlan", "Augusta", "Kahle", "Nell", "Needles"]
    gender = ["male", "male", "female", "male", "female", "male", "female", "male", "female", "female", "male", "female", "male", "female", "male", "female", "male", "female", "male", "female"]
    date = "2021-01-24"
    number = 5926089341
    dummy = "###########"


    #Styling for Treeview
    style = ttk.Style()
    style.configure("Treeview", background="#d3d3d3", foreground="#000000", rowheight=25, fieldbackground="#d3d3d3")
    style.map("Treeview", background=[('selected', '#edc933')])
    #ffd700

    #Configuration for Treeview
    page_title = Label(root, text="Student Records", font=("Times New Roman", 18), bg="#ffffff")
    search_ent = Entry(root, width="25", borderwidth=2)
    search_btn = Button(root, text="Search", bg="#138808", fg="#ffffff")
    main_tree = ttk.Treeview(root)
    main_tree["show"] = "headings"
    main_tree["columns"] = tuple(heads)
    main_tree.column("#0", width=0)
    for i in range(len(heads)):
        main_tree.column(f"{heads[i]}", width=130, anchor=CENTER)
        main_tree.heading(f"{heads[i]}", text=heads[i], anchor=CENTER)

    for i in range(len(fnames)):
        main_tree.insert(parent="", index="end", iid=i, text="", values=(char+str(sid), fnames[i], lnames[i], gender[i], date, dummy, date, emails[i], number))


    #Putting elements on the screen
    page_title.grid(column=0, row=0, sticky=W, padx=32)
    search_ent.grid(column=0, row=0, padx=(850,0))
    search_btn.grid(column=0, row=0, padx=(1070,0))
    main_tree.grid(column=0, row=1, ipady =(100))

    root.mainloop()
