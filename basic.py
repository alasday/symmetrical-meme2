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
    print ("\n >>Please enter a student's name.\n")


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
    c.execute(insertStmt(data, "students", "name", "age", "id"))

for data in courses:
    c.execute(insertStmt(data, "courses", "code", "mark", "id"))

'''
for item in c.execute("""
               SELECT age,id 
               FROM students
               WHERE name='
               """+name+"'"):
    print item
'''
