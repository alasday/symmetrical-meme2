import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
#...perhaps by beginning with these examples...

'''
q = "CREATE TABLE students (name TEXT, id INTEGER)"

c.execute(q)    #run SQL query


q = "CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)"

c.execute(q)
'''

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

#Testing out tables
print "Content for table students, data from peeps.csv: \n"
for row in c.execute('SELECT * FROM students'):
    print row
print "\n"

print "Content for table courses, data from sources.csv: \n"
for row in c.execute('SELECT * FROM courses'):
    print row
print "\n"

#==========================================================
db.commit() #save changes
db.close()  #close database



