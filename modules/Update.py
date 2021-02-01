import mysql.connector as mysql
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")
database = config["database"]


def updateteacherinfo(TeacherID, TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, DepartmentID, CourseID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "UPDATE teacherinfo SET TPassword = md5(%s), Usertype = %s, FirstName = %s, LastName = %s, Address = %s, HireDate = %s, Qualification = %s, DepartmentID = %d, CourseID = %d WHERE TeacherID = %d)"
    val = (TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, DepartmentID, CourseID, TeacherID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def updatestudentinfo(StudentID, FirstName, Surname, Gender, DateOfBirth, Address, ContactInfo, EnrolmentDate):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "UPDATE studentinfo SET FirstName = %s, Surname = %s, Gender = %s, DateOfBirth = %s, Address = %s, ContactInfo = %s, EnrolmentDate = %s where StudentID = %d"
    val = (FirstName, Surname, Gender, DateOfBirth, Address, ContactInfo, EnrolmentDate, StudentID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def updatecourseinfo(CourseID, CourseName, DepartmentID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "UPDATE courseinfo SET CourseName = %s, DepartmentID = %s WHERE CourseID = %s"
    val = (CourseName, DepartmentID, CourseID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def updategradeinfo(GradeID, TeacherID, StudentID, CurrentTerm, CurrentYear, ClassID, CourseID, Coursework_1, Coursework_2, Coursework_3, ExamGrade):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "UPDATE gradeinfo (TeacherID = %d, StudentID = %d, CurrentTerm = %s, CurrentYear = %d, ClassID = %d, CourseID = %s, Coursework_1 = %.lf, Coursework_2 = %.lf, Coursework_3 = %.lf, ExamGrade = %.lf where GradeID = %d)"
    val = (TeacherID, StudentID, CurrentTerm, CurrentYear, ClassID, Coursework_1, Coursework_2, Coursework_3, ExamGrade, GradeID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True

