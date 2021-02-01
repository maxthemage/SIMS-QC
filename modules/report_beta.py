#!/usr/bin/env python

from tkinter import *
from PIL import ImageTk, Image

def generateReport(studentid_entry, current_year_entry, current_term_entry):
    def clearFields():
        studentid_entry.delete(0, END)
        current_year_entry.delete(0, END)
        current_term_entry.delete(0, END)

    sid = studentid_entry.get()
    current_year = current_year_entry.get()
    current_term = current_term_entry.get()
    if (sid or current_year or current_term) == "":
        messagebox.showerror("Error", "Fields cannot be empty")
    else:
        clearFields()
        pass
        root = Toplevel()
        root.title("Report Cards")
        root.geometry("580x671") 
        root.iconbitmap("images/logo.ico")
        root.config(bg="#ffffff")
        root.resizable(width=False, height=False)

        heading_frame = LabelFrame(root, bg="#ffffff")
        heading_title = Label(heading_frame, text="QUEEN'S COLLEGE", font=("Times New Roman", 16), bg="#ffffff")
        qclogo_img = ImageTk.PhotoImage(Image.open("images/logo.jpeg"))
        qclogo = Label(heading_frame, image=qclogo_img, bg="#ffffff")
        heading_term = Label(heading_frame, text="EASTER TERM 2021", font=("Times New Roman", 16), bg="#ffffff")
        info_frame = LabelFrame(root, bg="#ffffff")
        student_name_lbl = Label(info_frame, text="Student Name: ##########", font=("Times New Roman", 13), bg="#ffffff")
        class_average_lbl = Label(info_frame, text="Class Average: ", font=("Times New Roman", 13), bg="#ffffff") 
        percentage_lbl = Label(info_frame, text="Percentage: ", font=("Times New Roman", 13), bg="#ffffff")
        title_frame = LabelFrame(root, bg="#ffffff")
        subject_title = Label(title_frame, text="Subject", font=("Times New Roman", 13), bg="#ffffff")
        grades_title = Label(title_frame, text="Grades", font=("Times New Roman", 13), bg="#ffffff")
        comments_title = Label(title_frame, text="Comments/Remarks", font=("Times New Roman", 13), bg="#ffffff")
        subject_frame = LabelFrame(root, bg="#ffffff")
        one = Label(subject_frame, text="", font=("Times New Roman", 12), bg="#ffffff")
        grades_frame = LabelFrame(root, bg="#ffffff")
        two = Label(grades_frame, text="", font=("Times New Roman", 12), bg="#ffffff")
        comments_frame = LabelFrame(root, bg="#ffffff")
        three = Label(comments_frame, text="", font=("Times New Roman", 12), bg="#ffffff")
        remarks_frame = LabelFrame(root, bg="#ffffff")
        class_teacher = Label(remarks_frame, text="Class Teacher's Remarks: ", bg="#ffffff", font=("Times New Roman", 11))
        head_teacher = Label(remarks_frame, text="Head Teacher's Remarks: ", bg="#ffffff", font=("Times New Roman", 11))
        house_captain = Label(remarks_frame, text="House Captain's Remarks: ", bg="#ffffff", font=("Times New Roman", 11))
        head_teacher_sig = Label(remarks_frame, text="Head Teacher's Signature: ", bg="#ffffff", font=("Times New Roman", 11))


        heading_frame.grid(column=0, row=0, ipadx=70, sticky=W)
        heading_title.grid(column=0, row=0, padx=(5,0))
        qclogo.grid(column=1, row=0, padx=(45,0))
        heading_term.grid(column=2, row=0, padx=(50,0))
        info_frame.grid(column=0, row=1, sticky=W, ipadx=110)
        student_name_lbl.grid(column=0, row=0, padx=(5,0))
        class_average_lbl.grid(column=1, row=0, padx=(70,0))
        percentage_lbl.grid(column=2, row=0, padx=(55,0))
        title_frame.grid(column=0, row=2, sticky=W, ipadx=50)
        subject_title.grid(column=0, row=0, padx=(5,0))
        grades_title.grid(column=1, row=0, padx=(125,0))
        comments_title.grid(column=2, row=0, padx=(145,0))
        subject_frame.grid(column=0, row=3, sticky=W, ipadx=100, ipady=195)
        two.grid(column=0, row=0)
        grades_frame.grid(column=0, row=3, sticky=W, ipadx=100, ipady=195, padx=(170,0))
        one.grid(column=0, row=0)
        comments_frame.grid(column=0, row=3, sticky=W, ipadx=150, ipady=195, padx=(350,0))
        three.grid(column=0, row=0)
        remarks_frame.grid(column=0, row=4, sticky=W, ipadx=220, ipady=1)
        class_teacher.grid(column=0, row=0)
        head_teacher.grid(column=0, row=1)
        house_captain.grid(column=0, row=2)
        head_teacher.grid(column=0, row=3)
        head_teacher_sig.grid(column=0, row=4)

        root.mainloop()
