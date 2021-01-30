#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def deleteStudent():
    def delete():
        sid = student_entry.get()
        if sid == "":
            messagebox.showerror("Error", "Field cannot be empty")
        else:
            pass
        

    #Configure root window
    root = Toplevel()
    root.title("Delete Student Record")
    root.geometry("750x550")
    root.iconbitmap("images/logo.ico")
    root.config(bg="#ffffff")


    title = Label(root, text="Enter Record Information", font=("Times New Roman", 23), pady=10, padx=5, bg="#ffffff")
    background_img = PhotoImage(file="images/logo_trans.png")
    background = Label(root, image=background_img, bg="#ffffff")
    frame = LabelFrame(root, bg="#ffffff", padx=25, pady=10)
    frame_title = Label(frame, text="Enter Student ID to Delete Student Info", font=("Roboto", 16), pady=10, padx=2, bg="#ffffff")
    student_entry_title = Label(frame, text="Student ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    student_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    delete_btn = Button(frame, text="Delete", font=(13), padx=3, pady=2, bg="#ff0000", fg="#ffffff", command=delete)
    cancel_btn = Button(frame, text="Cancel", font=(13), padx=3, pady=2)


    title.grid(column=0, row=0, sticky=W)
    background.place(x=0, y=45, relwidth=0.5, relheight=1)
    frame.grid(column=0, row=1, padx=(200,0))
    frame_title.grid(column=0, row=0, columnspan=2)
    student_entry_title.grid(column=0, row=1, sticky=W)
    student_entry.grid(column=1, row=1)
    delete_btn.grid(column=1, row=10, padx=(170,0), pady=(250,0))
    cancel_btn.grid(column=2, row=10, padx=(10,0), pady=(250,0))

    root.mainloop()

def deletePerformance():
    def delete():
        subject = subject_entry.get()
        if subject == "":
            messagebox.showerror("Error", "Field cannot be empty")
        else:
            pass
        

    #Configure root window
    root = Toplevel()
    root.title("Delete Performance Record")
    root.geometry("750x550")
    root.iconbitmap("images/logo.ico")
    root.config(bg="#ffffff")


    title = Label(root, text="Enter Record Information", font=("Times New Roman", 23), pady=10, padx=5, bg="#ffffff")
    background_img = PhotoImage(file="images/logo_trans.png")
    background = Label(root, image=background_img, bg="#ffffff")
    frame = LabelFrame(root, bg="#ffffff", padx=25, pady=10)
    frame_title = Label(frame, text="Enter Subject ID to Delete Subject Info", font=("Roboto", 16), pady=10, padx=2, bg="#ffffff")
    subject_entry_title = Label(frame, text="Subject ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    subject_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    delete_btn = Button(frame, text="Delete", font=(13), padx=3, pady=2, bg="#ff0000", fg="#ffffff", command=delete)
    cancel_btn = Button(frame, text="Cancel", font=(13), padx=3, pady=2)


    title.grid(column=0, row=0, sticky=W)
    background.place(x=0, y=45, relwidth=0.5, relheight=1)
    frame.grid(column=0, row=1, padx=(200,0))
    frame_title.grid(column=0, row=0, columnspan=2)
    subject_entry_title.grid(column=0, row=1, sticky=W)
    subject_entry.grid(column=1, row=1)
    delete_btn.grid(column=1, row=10, padx=(170,0), pady=(250,0))
    cancel_btn.grid(column=2, row=10, padx=(10,0), pady=(250,0))

    root.mainloop()


def deleteTeacher():
    def delete():
        tid = tid_entry.get()
        if tid == "":
            messagebox.showerror("Error", "Field cannot be empty")
        else:
            pass
        

    #Configure root window
    root = Toplevel()
    root.title("Delete Teacher Record")
    root.geometry("750x550")
    root.iconbitmap("images/logo.ico")
    root.config(bg="#ffffff")


    title = Label(root, text="Enter Record Information", font=("Times New Roman", 23), pady=10, padx=5, bg="#ffffff")
    background_img = PhotoImage(file="images/logo_trans.png")
    background = Label(root, image=background_img, bg="#ffffff")
    frame = LabelFrame(root, bg="#ffffff", padx=25, pady=10)
    frame_title = Label(frame, text="Enter Teacher ID to Delete Teacher Info", font=("Roboto", 16), pady=10, padx=2, bg="#ffffff")
    tid_entry_title = Label(frame, text="Teacher ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    tid_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    delete_btn = Button(frame, text="Delete", font=(13), padx=3, pady=2, bg="#ff0000", fg="#ffffff", command=delete)
    cancel_btn = Button(frame, text="Cancel", font=(13), padx=3, pady=2)


    title.grid(column=0, row=0, sticky=W)
    background.place(x=0, y=45, relwidth=0.5, relheight=1)
    frame.grid(column=0, row=1, padx=(200,0))
    frame_title.grid(column=0, row=0, columnspan=2)
    tid_entry_title.grid(column=0, row=1, sticky=W)
    tid_entry.grid(column=1, row=1)
    delete_btn.grid(column=1, row=10, padx=(170,0), pady=(250,0))
    cancel_btn.grid(column=2, row=10, padx=(10,0), pady=(250,0))

    root.mainloop()
