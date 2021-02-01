#!/usr/bin/env python

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import login_beta as login
import create_beta as create
import display_beta as display
import update_beta as update
import delete_beta as delete
import report_beta as report


login.loginWindow()
from login_beta import allowed, username
if allowed == True:
    pass
else:
    quit()
print(allowed, username)
def createWindow(username):
    root.title("Create New Records")
    flogo = Label(create_frame, image=logo_img, bg="#ffffff")
    fheading = Label(create_frame, text="Create New Records", font=("Times New Roman", 25), bg="#ffffff", pady=10)
    create_student_btn = Button(create_frame, text="Create Student records", font=("Arial", 13), padx=109, pady=15, command=create.createWindow)
    create_performance_btn = Button(create_frame, text="Create Performance records", font=("Arial", 13), padx=89, pady=15, command=create.createPerformanceWindow)
    create_teacher_btn = Button(create_frame, text="Create Teacher records", font=("Arial", 13), padx=107, pady=15, command=create.createTeacherWindow)

    if username == "admin":
        create_frame.grid(column=0, row=0, ipadx=150, ipady=40)
        back_btn_create.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        create_student_btn.grid(column=2, row=4, pady=(0, 7))
        create_performance_btn.grid(column=2, row=5, pady=(0, 7))
        create_teacher_btn.grid(column=2, row=6, pady=(0, 7))
    else:
        create_frame.grid(column=0, row=0, ipadx=150, ipady=40)
        back_btn_create.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        create_performance_btn.grid(column=2, row=5, pady=(0, 7))
        
        

def viewWindow(username):
    root.title("View Existing Records")
    flogo = Label(view_frame, image=logo_img, bg="#ffffff")
    fheading = Label(view_frame, text="View Exisiting Records", font=("Times New Roman", 25), bg="#ffffff", pady=10)
    view_student_btn = Button(view_frame, text="View Student records", font=("Arial", 13), padx=109, pady=15, command=display.displayStudent)
    view_performance_btn = Button(view_frame, text="View Performance records", font=("Arial", 13), padx=89, pady=15, command=display.displayStudent)
    view_teacher_btn = Button(view_frame, text="View Teacher records", font=("Arial", 13), padx=107, pady=15, command=display.displayStudent)

    if username == "admin":
        view_frame.grid(column=0, row=0, ipadx=150, ipady=40)
        back_btn_view.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        view_student_btn.grid(column=2, row=4, pady=(0, 7))
        view_performance_btn.grid(column=2, row=5, pady=(0, 7))
        view_teacher_btn.grid(column=2, row=6, pady=(0, 7))
    else:
        view_frame.grid(column=0, row=0, ipadx=150, ipady=40)
        back_btn_view.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        view_performance_btn.grid(column=2, row=5, pady=(0, 7))
        
def updateWindow(username):
    root.title("Update Existing Records")
    flogo = Label(update_frame, image=logo_img, bg="#ffffff")
    fheading = Label(update_frame, text="Update Exisiting Records", font=("Times New Roman", 25), bg="#ffffff", pady=10)
    update_student_btn = Button(update_frame, text="Update Student records", font=("Arial", 13), padx=109, pady=15, command=update.updateStudent)
    update_performance_btn = Button(update_frame, text="Update Performance records", font=("Arial", 13), padx=89, pady=15, command=update.updatePerformance)
    update_teacher_btn = Button(update_frame, text="Update Teacher records", font=("Arial", 13), padx=107, pady=15, command=update.updateTeacher)

    if username == "admin":
        update_frame.grid(column=0, row=0, ipadx=140, ipady=40)
        back_btn_update.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        update_student_btn.grid(column=2, row=4, pady=(0, 7))
        update_performance_btn.grid(column=2, row=5, pady=(0, 7))
        update_teacher_btn.grid(column=2, row=6, pady=(0, 7))
    else:
        update_frame.grid(column=0, row=0, ipadx=140, ipady=40)
        back_btn_update.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        update_performance_btn.grid(column=2, row=5, pady=(0, 7))

def deleteWindow(username):
    root.title("Delete Existing Records")
    flogo = Label(delete_frame, image=logo_img, bg="#ffffff")
    fheading = Label(delete_frame, text="Delete Exisiting Records", font=("Times New Roman", 25), bg="#ffffff", pady=10)
    delete_student_btn = Button(delete_frame, text="Delete Student records", font=("Arial", 13), padx=109, pady=15, command=delete.deleteStudent)
    delete_performance_btn = Button(delete_frame, text=" Delete Performance records", font=("Arial", 13), padx=87, pady=15, command=delete.deletePerformance)
    delete_teacher_btn = Button(delete_frame, text="Delete Teacher records", font=("Arial", 13), padx=107, pady=15, command=delete.deleteTeacher)

    if username == "admin":
        delete_frame.grid(column=0, row=0)
        back_btn_delete.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        delete_student_btn.grid(column=2, row=4, pady=(0, 7))
        delete_performance_btn.grid(column=2, row=5, pady=(0, 7))
        delete_teacher_btn.grid(column=2, row=6, pady=(0, 7))
    else:
        delete_frame.grid(column=0, row=0)
        back_btn_delete.grid(column=1, row=1, padx=(5,0))
        flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
        fheading.grid(column=2, row=3)
        delete_performance_btn.grid(column=2, row=5, pady=(0, 7))

def reportWindow():
    root.title("Generate Report Cards")
    flogo = Label(report_frame, image=logo_img, bg="#ffffff")
    fheading = Label(report_frame, text="Generate Report cards", font=("Times New Roman", 25), bg="#ffffff", pady=10)
    studentid_title = Label(report_frame, text="Student ID: ", font=("Times New Roman", 15), bg="#ffffff")
    studentid_entry = Entry(report_frame, width=19, borderwidth=2, font=("Times New Roman", 13))
    current_year_title = Label(report_frame, text="Current Year: ", font=("Times New Roman", 15), bg="#ffffff")
    current_year_entry = Entry(report_frame, width=19, borderwidth=2, font=("Times New Roman", 13))
    current_term_title = Label(report_frame, text="Current Term: ", font=("Times New Roman", 15), bg="#ffffff")
    current_term_entry = Entry(report_frame, width=19, borderwidth=2,font=("Times New Roman", 13))
    generate_report_btn = Button(report_frame, text="Generate", font=("Arial", 13), padx=109, pady=15, command= lambda: report.generateReport(studentid_entry, current_year_entry, current_term_entry))

    report_frame.grid(column=0, row=0)
    back_btn_report.grid(column=1, row=1, padx=(5,0))
    flogo.grid(column=2, row=2, ipadx=260, pady=(10,0))
    fheading.grid(column=2, row=3, pady=(0,10))
    studentid_title.grid(column=2, row=4, sticky=W, padx=(202,0))
    studentid_entry.grid(column=2, row=4, padx=(120,0)) 
    current_year_title.grid(column=2, row=5, sticky=W, padx=(202,0))
    current_year_entry.grid(column=2, row=5, padx=(120,0))
    current_term_title.grid(column=2, row=6, sticky=W, padx=(202,0))
    current_term_entry.grid(column=2, row=6, padx=(120,0))
    generate_report_btn.grid(column=2, row=7, pady=(7,0))
    
    

def back(frame):
    root.title("SIMS-QC")
    frame.grid_forget()

root = Tk()
root.title("SIMS-QC")
root.iconbitmap("images/logo.ico")
root.geometry("800x600")
root.config(bg="#ffffff")
root.resizable(width=False, height=False)

create_frame = LabelFrame(root, bg="#ffffff", pady=10, borderwidth=0, highlightthickness=0)
view_frame = LabelFrame(root, bg="#ffffff", pady=10, borderwidth=0, highlightthickness=0)
update_frame = LabelFrame(root, bg="#ffffff", pady=10, borderwidth=0, highlightthickness=0)
delete_frame = LabelFrame(root, bg="#ffffff", pady=10, borderwidth=0, highlightthickness=0)
report_frame = LabelFrame(root, bg="#ffffff", pady=10, borderwidth=0, highlightthickness=0)
back_img = PhotoImage(file="images/back.png")
back_label = Label(image=back_img, bg="#ffffff")
back_btn_create = Button(create_frame, image=back_img, borderwidth=0, bg="#ffffff", command = lambda: back(create_frame))
back_btn_view = Button(view_frame, image=back_img, borderwidth=0, bg="#ffffff", command = lambda: back(view_frame))
back_btn_update = Button(update_frame, image=back_img, borderwidth=0, bg="#ffffff", command = lambda: back(update_frame))
back_btn_delete = Button(delete_frame, image=back_img, borderwidth=0, bg="#ffffff", command = lambda: back(delete_frame))
back_btn_report = Button(report_frame, image=back_img, borderwidth=0, bg="#ffffff", command = lambda: back(report_frame))
logo_img = ImageTk.PhotoImage(Image.open("images/qc_logo.jpg"))
logo = Label(image=logo_img, bg="#ffffff")
heading = Label(root, text="Welcome to SIMS-QC 1.0.1", font=("Times New Roman", 25), bg="#ffffff", pady=10)
create_btn = Button(root, text="Create new record", font=("Arial", 13), padx=109, pady=15, command = lambda: createWindow(username))
view_btn = Button(root, text="View existing records", font=("Arial", 13), padx=100, pady=15, command = lambda: viewWindow(username))
update_btn = Button(root, text="Update records", font=("Arial", 13), padx=121, pady=15, command = lambda: updateWindow(username))
delete_btn = Button(root, text="Delete records", font=("Arial", 13), pady=13, padx=2, command = lambda: deleteWindow(username))
generate_btn = Button(root, text="Report Cards", font=("Arial", 13), padx=7, pady=13, command = reportWindow)
exit_btn = Button(root, text="Exit", font=("Arial", 13), padx=35, pady=13, command=root.destroy)

logo.grid(column=1, row=1, ipadx=305, pady=(10,0))
heading.grid(column=1, row=2)
create_btn.grid(column=1, row=3, pady=(0, 7))
view_btn.grid(column=1, row=5, pady=(0, 7))
update_btn.grid(column=1, row=7, pady=(0, 7))
delete_btn.grid(column=1, row=9, padx=(0,243))
generate_btn.grid(column=1, row=9, columnspan=1, padx=(15,0))
exit_btn.grid(column=1, row=9, columnspan=2, padx=(259,0))

root.mainloop()
