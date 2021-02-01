import mysql.connector as mysql
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")
database = config["database"]


def teacherinfo(TeacherID, TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, DepartmentID, CourseID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "INSERT INTO teacherinfo(TeacherID, TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, DepartmentID, CourseID) VALUES (%d, md5(%s), %s, %s, %s, %s, %s, %s, %d, %d)"
    val = (TeacherID, TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, DepartmentID, CourseID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def studentinfo(StudentID, FirstName, Surname, Gender, DateOfBirth, Address, ContactInfo, EnrolmentDate):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "INSERT INTO studentinfo(StudentID, FirstName, Surname, Gender, DateOfBirth, Address, ContactInfo, EnrolmentDate) VALUES (%d, %s, %s, %s, %s, %s, %d, %s)"
    val = (StudentID, FirstName, Surname, Gender, DateOfBirth, Address, ContactInfo, EnrolmentDate)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True

def deptinfo(DepartmentID, DeptName):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    sql = "INSERT INTO DeptTable(DepartmentID, DeptName)VALUES(%d, %s)"
    val = (DepartmentID, DeptName)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def classinfo(ClassID, ClassName):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    sql = "INSERT INTO ClassTable(ClassID, ClassName)VALUES(%d, %s)"
    val = (ClassID, ClassName)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def courseinfo(CourseID, CourseName, DepartmentID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "INSERT INTO courseinfo(CourseID, CourseName, DepartmentID)VALUES(%d, %s, %s)"
    val =  (CourseID, CourseName, DepartmentID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def gradeinfo(TeacherID, StudentID, CurrentTerm, CurrentYear, ClassID, CourseID, Coursework_1, Coursework_2, Coursework_3, ExamGrade):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "INSERT INTO gradeinfo(TeacherID, StudentID, CurrentTerm, CurrentYear, ClassID, CourseID, Coursework_1, Coursework_2, Coursework_3, ExamGrade)VALUES(%d, %d, %d, %d, %d, %d, %.1f, %.1f, %.1f, %.1f)"
    val = (TeacherID, StudentID, CurrentTerm, CurrentYear, ClassID, CourseID, Coursework_1, Coursework_2, Coursework_3, ExamGrade)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True
