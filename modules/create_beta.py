#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Create import *

def createWindow():
    def clearFields():
        student_entry.delete(0, END)
        fname_entry.delete(0, END)
        lname_entry.delete(0, END)
        gender_entry.delete(0, END)
        dob_entry.delete(0, END)
        address_entry.delete(0, END)
        email_entry.delete(0, END)
        contact_entry.delete(0, END)
        enrol_entry.delete(0, END)
     
    def submit():
        sid = student_entry.get()
        fname = fname_entry.get()
        lname = lname_entry.get()
        gender = gender_entry.get()
        dob = dob_entry.get()
        address = address_entry.get()
        email = email_entry.get()
        contact = contact_entry.get()
        enrol_date = enrol_entry.get()
        if ((sid) or (fname) or (lname) or (gender) or (dob) or (address) or (email) or (contact) or (enrol_date)) == "":
            messagebox.showerror("Error", "All fields must be filled", parent=root)
        else:
            studentinfo(sid, fname, lname, gender, dob, address, contact, enrol_date)
            clearFields()
            messagebox.showinfo("Info", "Student record was successfully created")
            pass

    root = Toplevel()
    root.lift()
    root.title("Create Student Record")
    root.geometry("750x600")
    root.iconbitmap("images/logo.ico")
    root.config(bg="#ffffff")
    root.resizable(width=False, height=False)


    title = Label(root, text="Enter Record Information", font=("Times New Roman", 23), pady=15, padx=5, bg="#ffffff")
    background_img = PhotoImage(file="images/logo_trans.png")
    background = Label(root, image=background_img, bg="#ffffff")
    frame = LabelFrame(root, bg="#ffffff", padx=25, pady=10)
    frame_title = Label(frame, text="Input Necessary data into Fields", font=("Roboto", 18), pady=10, padx=2, bg="#ffffff")
    student_entry_title = Label(frame, text="Student ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    student_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    fname_entry_title = Label(frame, text="First Name: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    fname_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    lname_entry_title = Label(frame, text="Last Name: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    lname_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    gender_entry_title = Label(frame, text="Gender: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    gender_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    dob_entry_title = Label(frame, text="DOB: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    dob_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    address_entry_title = Label(frame, text="Address: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    address_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    email_entry_title = Label(frame, text="Email: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    email_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    contact_entry_title = Label(frame, text="Contact: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    contact_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    enrol_entry_title = Label(frame, text="Enrol. Date: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    enrol_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    submit_btn = Button(frame, text="Create", font=(13), padx=3, pady=2, bg="#138808", fg="#ffffff", command=submit)
    cancel_btn = Button(frame, text="Cancel", font=(13), padx=3, pady=2, command=clearFields)


    title.grid(column=0, row=0, sticky=W)
    background.place(x=0, y=45, relwidth=0.5, relheight=1)
    frame.grid(column=0, row=1, padx=(200,0))
    frame_title.grid(column=0, row=0, columnspan=2)
    student_entry_title.grid(column=0, row=1, sticky=W)
    student_entry.grid(column=1, row=1)
    fname_entry_title.grid(column=0, row=2, sticky=W)
    fname_entry.grid(column=1, row=2)
    lname_entry_title.grid(column=0, row=3, sticky=W)
    lname_entry.grid(column=1, row=3)
    gender_entry_title.grid(column=0, row=4, sticky=W)
    gender_entry.grid(column=1, row=4)
    dob_entry_title.grid(column=0, row=5, sticky=W)
    dob_entry.grid(column=1, row=5)
    address_entry_title.grid(column=0, row=6, sticky=W)
    address_entry.grid(column=1, row=6)
    email_entry_title.grid(column=0, row=7, sticky=W)
    email_entry.grid(column=1, row=7)
    contact_entry_title.grid(column=0, row=8, sticky=W)
    contact_entry.grid(column=1, row=8)
    enrol_entry_title.grid(column=0, row=9, sticky=W)
    enrol_entry.grid(column=1, row=9)
    submit_btn.grid(column=1, row=10, padx=(170,0), pady=3)
    cancel_btn.grid(column=2, row=10, padx=(10,0), pady=3)


    root.mainloop()

def createPerformanceWindow():
    def clearFields():
        sid_entry.delete(0, END)
        subject_entry.delete(0, END)
        subject_teacherid_entry.delete(0, END)
        course_grade1_entry.delete(0, END)
        course_grade2_entry.delete(0, END)
        course_grade3_entry.delete(0, END)
        exam_entry.delete(0, END)
        term = term_entry.delete(0, END)
        year = year_entry.delete(0, END)
        formid = formid_entry.delete(0, END)
        
        
    def submit():
        sid = sid_entry.get()
<<<<<<< HEAD
        subjectid = subject_entry.get()
=======
        subjectid = subjectid_entry.get() #changed subject to subjectid
>>>>>>> 71fbb76cf0a7c3b936531044ec4089053f57c5ed
        tid = subject_teacherid_entry.get()
        term = term_entry.get() #added var, create entry field for it
        year = year_entry.get() #added var, create entry field for it
        formid = formid_entry.get() #added var, create entry field for it
        grade_one = course_grade1_entry.get()
        grade_two = course_grade2_entry.get()
        grade_three = course_grade3_entry.get()
        exam_grade = exam_entry.get()
        term = term_entry.get()
        year = year_entry.get()
        formid = formid_entry.get()
        if ((sid) or (subjectid) or (tid) or (grade_one) or (grade_two ) or (grade_three) or (exam_grade) or (term) or (year) or (formid)) == "":
            messagebox.showerror("Error", "All fields must be filled")
        else:
            gradeinfo(tid, sid, term, year, formid, subjectid, grade_one, grade_two, grade_three, exam_grade)
            clearFields()
            messagebox.showinfo("Info", "Performance record was successfully created")
            pass
    
    root = Toplevel()
    root.title("Create Performance Record")
    root.geometry("750x600")
    root.iconbitmap("images/logo.ico")
    root.config(bg="#ffffff")
    root.resizable(width=False, height=False)


    title = Label(root, text="Enter Record Information", font=("Times New Roman", 23), pady=15, padx=5, bg="#ffffff")
    background_img = PhotoImage(file="images/logo_trans.png")
    background = Label(root, image=background_img, bg="#ffffff")
    frame = LabelFrame(root, bg="#ffffff", padx=25, pady=10)
    frame_title = Label(frame, text="Input Necessary data into Fields", font=("Roboto", 18), pady=10, padx=2, bg="#ffffff")
    sid_entry_title = Label(frame, text="Student ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    sid_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    subject_entry_title = Label(frame, text="Subject ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    subject_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    subject_teacherid_entry_title = Label(frame, text="Subject Teacher ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    subject_teacherid_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    course_grade1_entry_title = Label(frame, text="Course Grade #1: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    course_grade1_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    course_grade2_entry_title = Label(frame, text="Course Grade #2: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    course_grade2_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    course_grade3_entry_title = Label(frame, text="Course Grade #3: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    course_grade3_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    exam_entry_title = Label(frame, text="Exam Grade: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    exam_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    term_entry_title = Label(frame, text="Term: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    term_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    year_entry_title = Label(frame, text="Year: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    year_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    formid_entry_title = Label(frame, text="Form ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    formid_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    submit_btn = Button(frame, text="Create", font=(13), padx=3, pady=2, bg="#138808", fg="#ffffff", command=submit)
    cancel_btn = Button(frame, text="Cancel", font=(13), padx=3, pady=2, command=clearFields)


    title.grid(column=0, row=0, sticky=W)
    background.place(x=0, y=45, relwidth=0.5, relheight=1)
    frame.grid(column=0, row=1, padx=(200,0))
    frame_title.grid(column=0, row=0, columnspan=2)
    sid_entry_title.grid(column=0, row=1, sticky=W)
    sid_entry.grid(column=1, row=1)
    subject_entry_title.grid(column=0, row=2, sticky=W)
    subject_entry.grid(column=1, row=2)
    subject_teacherid_entry_title.grid(column=0, row=3, sticky=W)
    subject_teacherid_entry.grid(column=1, row=3)
    course_grade1_entry_title.grid(column=0, row=4, sticky=W)
    course_grade1_entry.grid(column=1, row=4)
    course_grade2_entry_title.grid(column=0, row=5, sticky=W)
    course_grade2_entry.grid(column=1, row=5)
    course_grade3_entry_title.grid(column=0, row=6, sticky=W)
    course_grade3_entry.grid(column=1, row=6)
    exam_entry_title.grid(column=0, row=7, sticky=W)
    exam_entry.grid(column=1, row=7)
    term_entry_title.grid(column=0, row=8, sticky=W)
    term_entry.grid(column=1, row=8)
    year_entry_title.grid(column=0, row=9, sticky=W)
    year_entry.grid(column=1, row=9)
    formid_entry_title.grid(column=0, row=10, sticky=W)
    formid_entry.grid(column=1, row=10)
    submit_btn.grid(column=1, row=11, padx=(170,0), pady=3)
    cancel_btn.grid(column=2, row=11, padx=(10,0), pady=3)

    root.mainloop()


def createTeacherWindow():
    def clearFields():
        tid_entry.delete(0, END)
        password_entry.delete(0, END)
        fname_entry.delete(0, END)
        lname_entry.delete(0, END)
        address_entry.delete(0, END)
        employ_date_entry.delete(0, END)
        qual_entry.delete(0, END)
        email_entry.delete(0, END)
        departmentid_entry.delete(0, END)
        subjectid_entry.delete(0, END)
        
    def submit():
        tid = tid_entry.get()
        password = password_entry.get()
        user_type = user_type_entry.get() # added var, created entry field for it
        fname = fname_entry.get()
        lname = lname_entry.get()
        address = address_entry.get()
        employ_date = employ_date_entry.get()
        qualifications = qual_entry.get()
        email = email_entry.get()
<<<<<<< HEAD
        departmentid = departmentid_entry.get()
        subjectid = subjectid_entry.get()
        if ((tid) or (password) or (fname) or (lname) or (address) or (employ_date) or (qualifications) or (email) or (departmentid) or (subjectid)) == "":
=======
        departmentid = departmentid_entry.get() #changed department tp departmentid
        subjectid = subjectid_entry.get() #added subjectid, create entry field for it
        if (tid or password or fname or lname or address or employ_date or qualifications or email or department) == "":
>>>>>>> 71fbb76cf0a7c3b936531044ec4089053f57c5ed
            messagebox.showerror("Error", "All fields must be filled")
        else:
            teacherinfo(tid, password, user_type, fname, lname, address, employ_date, qualifications, departmentid, subjectid)
            clearFields()
            messagebox.showinfo("Info", "Teacher record was successfully created")
            pass
    
    root = Toplevel()
    root.title("Create Teacher Record")
    root.geometry("750x600")
    root.iconbitmap("images/logo.ico")
    root.config(bg="#ffffff")
    root.resizable(width=False, height=False)


    title = Label(root, text="Enter Record Information", font=("Times New Roman", 23), pady=15, padx=5, bg="#ffffff")
    background_img = PhotoImage(file="images/logo_trans.png")
    background = Label(root, image=background_img, bg="#ffffff")
    frame = LabelFrame(root, bg="#ffffff", padx=25, pady=10)
    frame_title = Label(frame, text="Input Necessary data into Fields", font=("Roboto", 18), pady=10, padx=2, bg="#ffffff")
    tid_entry_title = Label(frame, text="Teacher ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    tid_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    password_entry_title = Label(frame, text="Password: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    password_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    fname_entry_title = Label(frame, text="First Name: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    fname_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    lname_entry_title = Label(frame, text="Last Name: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    lname_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    address_entry_title = Label(frame, text="Address: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    address_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    employ_date_entry_title = Label(frame, text="Employ. Date: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    employ_date_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    qual_entry_title = Label(frame, text="Qualifications: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    qual_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    email_entry_title = Label(frame, text="Email: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    email_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    departmentid_entry_title = Label(frame, text="Department ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    departmentid_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    subjectid_entry_title = Label(frame, text="Subject ID: ", font=("Roboto", 14), bg="#ffffff", pady=8)
    subjectid_entry = Entry(frame, width=25, font=(11), borderwidth=1.5)
    submit_btn = Button(frame, text="Create", font=(13), padx=3, pady=2, bg="#138808", fg="#ffffff", command=submit)
    cancel_btn = Button(frame, text="Cancel", font=(13), padx=3, pady=2, command=clearFields)


    title.grid(column=0, row=0, sticky=W)
    background.place(x=0, y=45, relwidth=0.5, relheight=1)
    frame.grid(column=0, row=1, padx=(200,0))
    frame_title.grid(column=0, row=0, columnspan=2)
    tid_entry_title.grid(column=0, row=1, sticky=W)
    tid_entry.grid(column=1, row=1)
    password_entry_title.grid(column=0, row=2, sticky=W)
    password_entry.grid(column=1, row=2)
    fname_entry_title.grid(column=0, row=3, sticky=W)
    fname_entry.grid(column=1, row=3)
    lname_entry_title.grid(column=0, row=4, sticky=W)
    lname_entry.grid(column=1, row=4)
    address_entry_title.grid(column=0, row=5, sticky=W)
    address_entry.grid(column=1, row=5)
    employ_date_entry_title.grid(column=0, row=6, sticky=W)
    employ_date_entry.grid(column=1, row=6)
    qual_entry_title.grid(column=0, row=7, sticky=W)
    qual_entry.grid(column=1, row=7)
    email_entry_title.grid(column=0, row=8, sticky=W)
    email_entry.grid(column=1, row=8)
    departmentid_entry_title.grid(column=0, row=9, sticky=W)
    departmentid_entry.grid(column=1, row=9)
    subjectid_entry_title.grid(column=0, row=10, sticky=W)
    subjectid_entry.grid(column=1, row=10)
    submit_btn.grid(column=1, row=11, padx=(170,0), pady=3)
    cancel_btn.grid(column=2, row=11, padx=(10,0), pady=3)


    root.mainloop()
