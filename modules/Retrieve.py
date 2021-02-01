import mysql.connector as mysql
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")
database = config["database"]

def retrieveTeacher(TeacherID):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM teacherinfo WHERE TeacherID = "+str(TeacherID))

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def retrievestudent(StudentID):

    db = mysql.connect(
        host = database["host"],
        user = databse["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM studentinfo WHERE StudentID ="+str(StudentID))

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def retrievegrade(GradeID):

    db = mysql.connect(
        host = database["host"],
        user = databse["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM gradeinfo WHERE GradeID="+str(GradeID))

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def retrievegradereport(StudentID, CurrentYear, CurrentTerm):

    db = mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("""SELECT CONCAT(studentinfo.FirstName, " ", studentinfo.Surname) AS FullName,
                    courseinfo.CourseName, gradeinfo.Coursework_Avg, gradeinfo.ExamGrade
                    FROM studentinfo, gradeinfo INNER JOIN courseinfo USING (CourseID)
                    WHERE studentID ="""+str(StudentID)+" "+"AND CurrentYear ="+str(CurrentYear)+" "+"AND CurrentTerm ="+str(CurrentTerm))

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def teacherSubjectView():

    db = mysql.connect(
        host = database["host"],
        user = databse["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Teacher_Subject LIMIT 10")

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def userView():

    db = mysql.connect(
        host = database["host"],
        user = databse["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Users LIMIT 10")

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def schoolperformance1():

    db = mysql.connect(
        host = database["host"],
        user = databse["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM ClassPerformance_Term1")

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def schoolperformance2():

    db = mysql.connect(
        host = database["host"],
        user = databse["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM ClassPerformance_Term2")

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def schoolperformance3():

    db = mysql.connect(
        host = database["host"],
        user = databse["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM ClassPerformance_Term3")

    records = cursor.fetchall()

    db.commit()

    db.close()

    return records


def verifylogin(TeacherID, TPassword):

    db.mysql.connect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    sql = "SELECT TeacherID, Usertype FROM teacherinfo WHERE TeacherID = %s AND TPassword= md5(%s) AND active = TRUE"
    
    val = (TeacherID, TPassword)

    cursor.execute(sql, val)

    records = cursor.fetchall()

    db.commit()
    db.close()

    return records
