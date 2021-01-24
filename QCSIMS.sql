DROP DATABASE IF EXISTS qcsimsdb;
CREATE DATABASE IF NOT EXISTS qcsimsdb;
USE qcsimsdb;
SET sql_mode = strict_all_tables;

DROP TABLE IF EXISTS 	StudentInfo,
                        CourseInfo,
                        TeacherInfo,
                        GradeInfo,
                        AttendanceInfo;
                        
CREATE TABLE StudentInfo(
	StudentID INT(7) NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    Surname VARCHAR(20) NOT NULL, 
    Gender ENUM ('MALE', 'FEMALE') NOT NULL,
    DateOfBirth DATE NOT NULL,
    Address TEXT(40) NOT NULL,
    ContactInfo INT(7) NOT NULL, 
    GuardianName TEXT(40) NOT NULL,
    GuardianContactInfo INT(7) NOT NULL,
    EnrolmentDate DATE NOT NULL, 
    PRIMARY KEY (StudentID));
    
CREATE TABLE AttendanceInfo(
	AttendID INT NOT NULL AUTO_INCREMENT,
    StudentID INT(7) NOT NULL, 
    CurrentClass ENUM('1A', '1B', '1C', '1D',
						'2A', '2B', '2C', '2D',
                        '3A', '3B', '3C', '3D',
                        '4A', '4B', '4C', '4D',
                        '5A', '5B', '5C', '5D',
                        'L6A', 'L6B', 'L6C',
                        'U6A', 'U6B') NOT NULL, 
	CurrentYear YEAR NOT NULL, 
    CurrentTerm ENUM ('1ST', '2ND', '3RD'),
    ClassesPresent INT, 
    ClassesAbsent INT,
    Detentions INT,
    PRIMARY KEY (AttendID),
    FOREIGN KEY (StudentID) REFERENCES StudentInfo (StudentID) ON DELETE CASCADE ON UPDATE CASCADE);
    
CREATE TABLE CourseInfo(
	CourseID CHAR(7) NOT NULL,
    CourseName TEXT(40) NOT NULL,
    CourseCategory ENUM(	'Linquistics', 'Mathematics', 
							'Science', 'Humanities',
							'Technical Vocation','Business',
							'Foreign Languages', 'Modern Arts',
							'Information & Communication Technology'),
	PRIMARY KEY (CourseID));

CREATE TABLE TeacherInfo(
	TeacherID INT(7) NOT NULL, 
    TPassword CHAR(15) NOT NULL, 
    Usertype ENUM('Admin', 'Client') NOT NULL, 
    FirstName VARCHAR(20) NOT NULL, 
    LastName VARCHAR(20) NOT NULL, 
    Address TEXT(40) NOT NULL,
    HireDate DATE NOT NULL,
    Qualification TEXT(30) NOT NULL,
    Department ENUM(	'Linquistics', 'Mathematics', 
						'Science', 'Humanities',
						'Technical Vocation','Business',
						'Foreign Languages', 'Modern Arts',
						'Information & Communication Technology'),
	CourseID CHAR(7) NOT NULL,
	PRIMARY KEY (TeacherID),
    FOREIGN KEY (CourseID) REFERENCES CourseInfo (CourseID) ON DELETE CASCADE ON UPDATE CASCADE);

CREATE TABLE GradeInfo(
	GradeID INT(7) NOT NULL,
    TeacherID INT(7) NOT NULL, 
    StudentID INT(7) NOT NULL,
    CurrentTerm ENUM ('1ST', '2ND', '3RD'),
    CurrentYear INT(4) NOT NULL,
    CurrentClass ENUM ('1A', '1B', '1C', '1D',
						'2A', '2B', '2C', '2D',
                        '3A', '3B', '3C', '3D',
                        '4A', '4B', '4C', '4D',
                        '5A', '5B', '5C', '5D',
                        'L6A', 'L6B', 'L6C',
                        'U6A', 'U6B') NOT NULL, 
	Coursework_1 DECIMAL(3,1) NOT NULL, 
    Coursework_2 DECIMAL(3,1) NOT NULL, 
    Coursework_3 DECIMAL(3,1) NOT NULL, 
	Coursework_Avg DECIMAL(3,1) GENERATED ALWAYS AS ((Coursework_1+Coursework_2+Coursework_3)/3), 
    ExamGrade DECIMAL(3,1) DEFAULT 0,
    DateModified DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (GradeID),
    FOREIGN KEY (TeacherID) REFERENCES TeacherInfo (TeacherID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (StudentID) REFERENCES StudentInfo (StudentID) ON DELETE CASCADE ON UPDATE CASCADE);

DROP VIEW IF EXISTS Teacher_Subject;

CREATE OR REPLACE VIEW Teacher_Subject AS
 	SELECT CourseInfo.CourseID, CourseInfo.CourseName, TeacherInfo.TeacherID, 
    CONCAT(TeacherInfo.FirstName, " ", TeacherInfo.LastName) AS FullName 
    FROM CourseInfo INNER JOIN TeacherInfo 
   USING (CourseID);

DROP VIEW IF EXISTS SchoolReport_Term1,
					SchoolReport_Term2,
                    ClassPerformance_Term1,
                    ClassPerformance_Term2, 
                    ClassPerformance_Term3;

CREATE VIEW SchoolReport_Term1 AS
	SELECT GradeID, TeacherID, StudentID, CurrentTerm, CurrentClass, CurrentYear, Coursework_Avg AS OverallGrade
    FROM GradeInfo
    WHERE CurrentTerm = "1ST"
    ORDER BY CurrentYear, CurrentTerm, CurrentClass;
    
CREATE VIEW SchoolReport_Term2 AS
	SELECT GradeID, TeacherID, StudentID, CurrentTerm, CurrentClass, CurrentYear, Coursework_Avg, ExamGrade, ((Coursework_Avg *0.4) + (ExamGrade*0.6)) AS OverallGrade
    FROM GradeInfo
    WHERE CurrentTerm = "2ND" OR CurrentTerm = "3RD"
    ORDER BY CurrentYear, CurrentTerm, CurrentClass;
    
CREATE VIEW ClassPerformace_Term1 AS
	SELECT CurrentClass, CurrentYear, AVG(OverallGrade) AS Avg_Performance 
    FROM SchoolReport_Term1
    WHERE CurrentYear = YEAR(now()) AND CurrentTerm = "1ST"
    GROUP BY CurrentClass;

CREATE VIEW ClassPerformace_Term2 AS
	SELECT CurrentClass, CurrentYear, AVG(OverallGrade) AS Avg_Performance 
    FROM SchoolReport_Term2
    WHERE CurrentYear = YEAR(now()) AND CurrentTerm = "2ND"
    GROUP BY CurrentClass;

CREATE VIEW ClassPerformace_Term3 AS
	SELECT CurrentClass, CurrentYear, AVG(OverallGrade) AS Avg_Performance 
    FROM SchoolReport_Term2
    WHERE CurrentYear = YEAR(now()) AND CurrentTerm = "3RD"
    GROUP BY CurrentClass;