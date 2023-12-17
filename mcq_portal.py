import mysql.connector as mq

def Tdetails():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    myc.execute("drop table if exists Tdetails ")
    myc.execute("create table Tdetails(uid int, TID int, Name varchar(35), dob date, Salary float, doj date, Subject varchar(50), Contact bigint, primary key(TID),foreign key(uid) references Tlogin(uid))")
    myc.execute("commit")
    myc.close()
def TLogin():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    myc.execute("drop table if exists Tdetails ")
    myc.execute("drop table if exists TLogin ")
    myc.execute("create table TLogin(uid int, pwd varchar(10), primary key(uid))")
    myc.execute("commit")
def Sdetails():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    myc.execute("drop table if exists Sdetails ")
    myc.execute("create table Sdetails(uid int, SID int, Name varchar(35), class int, dob date, Contact bigint, primary key(SID),foreign key(uid) references Slogin(uid))")
    myc.execute("commit")
    myc.close()
def SLogin():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    myc.execute("drop table if exists Sdetails ")
    myc.execute("drop table if exists SLogin ")
    myc.execute("create table SLogin(uid int, pwd varchar(10), primary key(uid))")
    myc.execute("commit")

def menu():
    print("Enter 1 if you are a student. \nEnter 2 if you are a teacher.")
    a=int(input("Enter your choice: "))
    if a == 1:
         Smenu()

def Smenu():
        print("~MENU~ \nPress 1 to LOGIN. \nPress 2 to . \nPress 3 to check marks")


menu()
# TLogin()
# Tdetails()
# SLogin()
# Sdetails()