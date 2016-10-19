import csv
import sqlite3
import sys
import os

#database name
f="avrgs.db"

#remove database file
os.remove(f)

#create connection with database
db = sqlite3.connect(f)
c = db.cursor()

name=""
#prompt user to give a student name if the user didn't
try:
    name = sys.argv[1]
except IndexError:
    print ("\n>>Please enter a student's name.\n")

#variable used later to check whether student name exists
exist = False

#read peeps.csv & courses.csv into csv reader
peeps = csv.DictReader(open("peeps.csv"))
courses = csv.DictReader(open("courses.csv"))


#query statement for each csv file
peepsQ = """
         CREATE TABLE students 
                (name TEXT, age INTEGER, id INTEGER)
         """

coursesQ = """
           CREATE TABLE courses 
                  (code TEXT, mark INTEGER, id INTEGER)
           """

#create table for each csv file
c.execute(peepsQ)
c.execute(coursesQ)

#SELECT statements for each table
def insertStmt(data, table, fone, ftwo, fthree):
    stmt = "INSERT INTO " + table + " VALUES ('" + data[fone] + "'," + data[ftwo] + "," + data[fthree] + ")"
    return stmt


#populate each table
for data in peeps:
    #check if input name exists in csv file
    if data['name'] == name:
        exist = True
    c.execute(insertStmt(data, "students", "name", "age", "id"))

for data in courses:
    c.execute(insertStmt(data, "courses", "code", "mark", "id"))


def studentProfile():
    #create a table for chosen student
    c.execute("CREATE TABLE profile(code TEXT, grade REAL)")
    
    #write select statement to obtain the student's courses and grades
    getID = "SELECT id FROM students WHERE name='" + name + "'"
    getGrades = "SELECT code, mark FROM courses WHERE id=(" + getID + ")"

    #add records to table profile
    c.execute("INSERT INTO profile " + getGrades)
    return


def calcAvrg():
    #calculate and insert average into table profile
    total = 0
    courseNum = 0
    for item in c.execute("SELECT grade FROM profile"):
        total += item[0]
        courseNum += 1
    c.execute("INSERT INTO profile VALUES('average', " + str(total/courseNum) + ")")
    return


def output():
    c.execute("SELECT * FROM profile")
    content = c.fetchall()
    length = len(content)
    print "Report for " + name + ": \n"
    for pos in range(length):
        print content[pos][0] + "  " + str(content[pos][1]) + "\n"
    return


if name != "" and exist:
    studentProfile()
    calcAvrg()
    output()
elif (not exist) and name != "":
    print "\n>>Student name not found.\n"

    

#==========================
db.commit()
db.close()

