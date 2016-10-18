import csv
import sqlite3
import sys

f="avrgs.db"

db = sqlite3.connect(f)
c = db.cursor()

name = sys.argv[1]

#read peeps.csv & courses.csv into csv reader
peeps = csv.DictReader(open("peeps.csv"))
courses = csv.DictReader(open("courses.csv"))


#query statement for each csv file
peepsQ = "CREATE TABLE students (name TEXT, age INTEGER, id INTEGER)"
coursesQ = "CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)"

#create table for each csv file
c.execute(peepsQ)
c.execute(coursesQ)

#populate each table
for data in peeps:
    c.execute("INSERT INTO students VALUES ('"+data["name"]+"',"+data["age"]+","+data["id"]+")")

for data in courses:
    c.execute("INSERT INTO courses VALUES ('"+data["code"]+"',"+data["mark"]+","+data["id"]+")")


