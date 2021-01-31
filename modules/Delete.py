import mysql.connector as mysql
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")
database = config["database"]

def deleteteacherinfo(TeacherID, TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, Department, CourseID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "DELETE FROM teacherinfo(TPassword = md5(%s), Usertype = %s, FirstName = %s, LastName = %s, Address = %s, HireDate = %s, Qualification = %s, Department = %s, CourseID = %d where id = %d)"
    val = (TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, Department, CourseID, TeacherID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def deletestudentinfo(StudentID, FirstName, Surname, Gender, DateOfBirth, Address, ContactInfo, GuardianName, GuardianContactInfo, EnrolmentDate):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "DELETE FROM studentinfo(FirstName = %s, Surname = %s, Gender = %s, DateOfBirth = %s, Address = %s, ContactInfo = %s, GuardianName = %s, GuardianContactInfo = %d, EnrolmentDate = %s where id = %d) "
    val = (FirstName, Surname, Gender, DateOfBirth, Address, ContactInfo, GuardianName, GuardianContactInfo, EnrolmentDate, StudentID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def deleteattendanceinfo(AttendID, StudentID, CurrentClass, CurrentYear, CurrentTerm, ClassesPresent, ClassesAbsent, Detentions):
    
    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "DELETE FROM attendanceinfo(StudentID = %d, CurrentClass = %s, CurrentYear = %d, CurrentTerm = %s, ClassesPresent = %d, ClassesAbsent = %d, Detentions = %d where id = %d)"
    val = (StudentID, CurrentClass, CurrentYear, CurrentTerm, ClassesPresent, ClassesAbsent, Detentions, AttendID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def deletecourseinfo(CourseID, CourseName, CourseCategory):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "DELETE FROM courseinfo (CourseName = %s, CourseCategory = %s where id = %d)"
    val =  (CourseName, CourseCategory, CourseID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True


def deletegradeinfo(GradeID, TeacherID, StudentID, CurrentTerm, CurrentYear, CurrentClass, Coursework_1, Coursework_2, Coursework_3, Coursework_Avg, ExamGrade, DateModified):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor

    sql = "DELETE FROM gradeinfo (TeacherID = %d, StudentID = %d, CurrentTerm = %s, CurrentYear = %d, CurrentClass = %d, Coursework_1 = %.lf, Coursework_2 = %.lf, Coursework_3 = %.lf, Coursework_Avg = %.lf, ExamGrade = %.lf, DateModified = %s where id = %d)"
    val = (TeacherID, StudentID, CurrentTerm, CurrentYear, CurrentClass, Coursework_1, Coursework_2, Coursework_3, Coursework_Avg, ExamGrade, DateModified, GradeID)
    cursor.execute(sql, val)

    db.commit()
    db.close()
    return True
