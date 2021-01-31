import mysql.connector as mysql
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")
database = config["database"]

def deleteteacherinfo(TeacherID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("DELETE FROM teacherinfo WHERE TeacherID ="+str(TeacherID))

    db.commit()
    db.close()
    return True


def deletestudentinfo(StudentID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("DELETE FROM studentinfo WHERE StudentID ="+str(StudentID))

    db.commit()
    db.close()
    return True

def deletecourseinfo(CourseID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("DELETE FROM courseinfo WHERE CourseID="+str(CourseID))

    db.commit()
    db.close()
    return True


def deletegradeinfo(GradeID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("DELETE FROM gradeinfo WHERE GradeID ="+str(GradeID))

    db.commit()
    db.close()
    return True


def deleteclassinfo(ClassID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("DELETE FROM ClassTable WHERE ClassID="+str(ClassID))

    db.commit()
    db.close()
    return True


def deletedept(DepartmentID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("DELETE FROM DeptTable WHERE DepartmentID="+str(DepartmentID))

    db.commit()
    db.close()

    return True

