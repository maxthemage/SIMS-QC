import mysql.connector as mysql
import configparser

config = configparser.RawConfigParser()
config.read("config.ini")
database = config["database"]
extrapass = config["DEFAULT"]["extra"]

def setupDB():
    db = mysql.conect(
        host = database["host"],
        user = database["user"],
        password = database["password"],
        database = database["schema"]
    )

    cursor = db.cursor()

    cursor.execute("DROP DATABASE IF EXISTS qcsimsdb")
    cursor.execute("CREATE DATABASE IF NOT EXISTS qcsimsdb")
    cursor.execute("USE qcsimsdb")
    cursor.execute("SET sql_mode = strict_all_tables")
    
    cursor.execute("""DROP TABLE IF EXISTS
                        StudentInfo,
                        CourseInfo,
                        TeacherInfo,
                        GradeInfo,
                        ClassTable,
                        DeptTable""")

    cursor.execute("""CREATE TABLE ClassTable(
                        ClassID INT AUTO_INCREMENT NOT NULL,
                        ClassName VARCHAR(3) NOT NULL, 
                        PRIMARY KEY (ClassID))""")
    
    cursor.execute("""CREATE TABLE StudentInfo(
                        StudentID INT(7) NOT NULL,
                        FirstName VARCHAR(20) NOT NULL,
                        Surname VARCHAR(20) NOT NULL, 
                        Gender ENUM ('MALE', 'FEMALE') NOT NULL,
                        DateOfBirth DATE NOT NULL,
                        Address TEXT(40) NOT NULL,
                        ContactInfo INT(7) NOT NULL, 
                        EnrolmentDate DATE NOT NULL, 
                        PRIMARY KEY (StudentID))""")

    cursor.execute("""CREATE TABLE DeptTable(
                        DepartmentID INT(2) NOT NULL,
                        DeptName VARCHAR(50) NOT NULL,
                        PRIMARY KEY (DepartmentID))""")

    cursor.execute("""CREATE TABLE CourseInfo(
                        CourseID VARCHAR(7) NOT NULL,
                        CourseName TEXT(40) NOT NULL,
                        DepartmentID INT(2) NOT NULL, 
                        PRIMARY KEY (CourseID),
                        FOREIGN KEY (DepartmentID) REFERENCES DeptTable (DepartmentID) ON DELETE CASCADE ON UPDATE CASCADE)""")
    
    cursor.execute("""CREATE TABLE TeacherInfo(
                        TeacherID INT(7) NOT NULL, 
                        TPassword VARCHAR(500) NOT NULL, 
                        Usertype ENUM('Admin', 'Client') NOT NULL, 
                        FirstName VARCHAR(20) NOT NULL, 
                        LastName VARCHAR(20) NOT NULL, 
                        Address TEXT(40) NOT NULL,
                        HireDate DATE NOT NULL,
                        Qualification TEXT(30) NOT NULL,
                        DepartmentID INT(2) NOT NULL, 
                        CourseID CHAR(7) NOT NULL,
                        PRIMARY KEY (TeacherID),
                        FOREIGN KEY (DepartmentID) REFERENCES DeptTable (DepartmentID) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (CourseID) REFERENCES CourseInfo (CourseID) ON DELETE CASCADE ON UPDATE CASCADE)""")
    
    cursor.execute("""CREATE TABLE GradeInfo(
                        GradeID INT(10) NOT NULL AUTO_INCREMENT,
                        TeacherID INT(7) NOT NULL, 
                        StudentID INT(7) NOT NULL,
                        CurrentTerm INT(2) NOT NULL,
                        CurrentYear INT(4) NOT NULL,
                        ClassID INT(2) NOT NULL,
                        CourseID VARCHAR(7) NOT NULL, 
                        Coursework_1 DECIMAL(3,1) NOT NULL, 
                        Coursework_2 DECIMAL(3,1) NOT NULL, 
                        Coursework_3 DECIMAL(3,1) NOT NULL, 
                        Coursework_Avg DECIMAL(3,1) GENERATED ALWAYS AS ((Coursework_1+Coursework_2+Coursework_3)/3),  
                        ExamGrade DECIMAL(3,1) DEFAULT 0,
                        OverallGrade DECIMAL(3,1) GENERATED ALWAYS AS(IF((CurrentTerm!=1), (Coursework_Avg*0.4) + (ExamGrade*0.6), Coursework_Avg)),
                        Comments TEXT GENERATED ALWAYS AS(IF(OverallGrade >= 90 AND OverallGrade <= 100,"A-Excellent Job", 
                        IF(OverallGrade >= 80 AND OverallGrade <90, "B-Great Job", 
                        IF(OverallGrade>=70 AND OverallGrade < 80, "C-Good Job", 
                        IF(OverallGrade >=60 AND OverallGrade<70, "D-Try Harder Next Time", "F-Fail")))))
                        DateModified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
                        PRIMARY KEY (GradeID),
                        FOREIGN KEY (TeacherID) REFERENCES TeacherInfo (TeacherID) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (StudentID) REFERENCES StudentInfo (StudentID) ON DELETE CASCADE ON UPDATE CASCADE),
                        FOREIGN KEY (CourseID) REFERENCES CourseInfo (CourseID) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (CurrentTerm) REFERENCES TermTable (CurrentTerm),
                        FOREIGN KEY (ClassID) REFERENCES ClassTable (ClassID)""")
    
    cursor.execute("DROP VIEW IF EXISTS Teacher_Subject")
    
    cursor.execute("""CREATE OR REPLACE VIEW Teacher_Subject AS
                        SELECT CourseInfo.CourseID, CourseInfo.CourseName, TeacherInfo.TeacherID, 
                        CONCAT(TeacherInfo.FirstName, " ", TeacherInfo.LastName) AS FullName 
                        FROM CourseInfo INNER JOIN TeacherInfo 
                        USING (CourseID)""")
    
    cursor.execute("DROP VIEW IF EXISTS Users")
    
    cursor.execute("""CREATE VIEW Users AS
                        SELECT TacherInfo.TeacherID, TeacherInfo.TPassword, TeacherInfo.UserType
                        FROM TeacherInfo""")
    
    cursor.execute("""DROP VIEW IF EXISTS SchoolReport_Term1,
			SchoolReport_Term2,
                        ClassPerformance_Term1,
                        ClassPerformance_Term2, 
                        ClassPerformance_Term3""")
    
    cursor.execute("""CREATE VIEW SchoolReport_Term1 AS
                        SELECT GradeID, TeacherID, StudentID, CurrentTerm, CurrentClass, CurrentYear, Coursework_Avg AS OverallGrade
                        FROM GradeInfo
                        WHERE CurrentTerm = "1ST"
                        ORDER BY CurrentYear, CurrentTerm, CurrentClass""")
    
    cursor.execute("""CREATE VIEW SchoolReport_Term2 AS
                        SELECT GradeID, TeacherID, StudentID, CurrentTerm, CurrentClass, CurrentYear, Coursework_Avg, ExamGrade, ((Coursework_Avg *0.4) + (ExamGrade*0.6)) AS OverallGrade
                        FROM GradeInfo
                        WHERE CurrentTerm = "2ND" OR CurrentTerm = "3RD"
                        ORDER BY CurrentYear, CurrentTerm, CurrentClass""")
    
    cursor.execute("""CREATE VIEW ClassPerformace_Term1 AS
                        SELECT CurrentClass, CurrentYear, AVG(OverallGrade) AS Avg_Performance 
                        FROM SchoolReport_Term1
                        WHERE CurrentYear = YEAR(now()) AND CurrentTerm = "1ST"
                        GROUP BY CurrentClass""")
    
    cursor.execute("""CREATE VIEW ClassPerformace_Term2 AS
                        SELECT CurrentClass, CurrentYear, AVG(OverallGrade) AS Avg_Performance 
                        FROM SchoolReport_Term2
                        WHERE CurrentYear = YEAR(now()) AND CurrentTerm = "2ND"
                        GROUP BY CurrentClass""")
    
    cursor.execute("""CREATE VIEW ClassPerformace_Term3 AS
                        SELECT CurrentClass, CurrentYear, AVG(OverallGrade) AS Avg_Performance 
                        FROM SchoolReport_Term2
                        WHERE CurrentYear = YEAR(now()) AND CurrentTerm = "3RD"
                        GROUP BY CurrentClass""")
    
    cursor.execute("INSERT INTO teacherinfo(TeacherID, TPassword, Usertype, FirstName, LastName, Address, HireDate, Qualification, Department, CourseID) VALUES (1034212, md5('"+extrapass+"password"+"'), 'admin', 'Samantha', 'Liverpool', '43 Shirley Street, East Ruimveldt', '2002-09-12', 'Senior Mistress', 'Information and Communication Technology', 'ICT001')")

    db.commit()

    db.close()

    return True
