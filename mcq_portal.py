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
    myc.execute("create table Sdetails(uid int, SID varchar(15), Name varchar(35), class int, dob date, Contact bigint, primary key(SID),foreign key(uid) references Slogin(uid))")
    myc.execute("commit")
    myc.close()
def Sdentry():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    uid=int(input("Enter your User-ID "))
    sid=input("Enter your Student-ID ")
    pwd=input("Enter the password")
    name=input("Enter your name ")
    dob=input("Enter your date of birth ")
    clas=int(input("Enter the class "))
    con=int(input("Enter your contact no. "))
    info="INSERT into Sdetails values ({},'{}','{}',{},'{}',{})".format(uid,sid,name,clas,dob,con)
    info1="INSERT into SLogin values ({},'{}')".format(uid,pwd)
    myc.execute(info1)
    myc.execute(info)
    myc.execute("commit")
    myc.close()
def SLentry():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    name = input("Enter your username(uid)")
    passw = input("Enter your new Password:")
    q="select pwd from SLogin where uid='{}'".format(name)
    myc.execute(q)
    x=myc.fetchone()
    if passw == x[0]:
         print ("Login Sucessfull")
    else:
         print("Person Not Found")
    myc.close()

def TLentry():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    name = input("Enter your username(uid)")
    passw = input("Enter your new Password:")
    q="select pwd from TLogin where uid='{}'".format(name)
    myc.execute(q)
    x=myc.fetchone()
    if passw == x[0]:
         print ("Login Sucessfull")
    else:
         print("Person Not Found")
    myc.close()
def Tdentry():
    mydb=mq.connect(host="localhost",user="root",password="2005",database="cs_proj")
    myc=mydb.cursor()
    uid=input("Enter your Teacher-ID ")
    tid=input("Enter your Teacher-ID ")
    pwd=input("Enter your password-")
    name=input("Enter your name ")
    sub=input("Enter the suject you are expertised in ")
    dob=input("Enter your Date of Birth(yyyy-mm-dd) ")
    sal=float(input("Enter your Salary "))
    doj=input("Enter your Date of Joining(yyyy-mm-dd) ")
    con=int(input("Enter your contact no. "))
    info="INSERT into Tdetails values ({},{},'{}','{}',{},'{}','{}',{})".format(uid,tid,name,dob,sal,doj,sub,con)
    info1="INSERT into TLogin values ({},'{}')".format(uid,pwd)
    myc.execute(info1)
    myc.execute(info)
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
    if a == 2:
         Tmenu()

def Smenu():
        print("~MENU~ \nPress 1 to SignIn. \nPress 2 to SignUp . \nPress 3 to check marks")
        c=int(input("Enter your choice: "))
        if c == 1:
             SLentry()
        if c == 2:
            Sdentry()
def Tmenu():
        print("~MENU~ \nPress 1 to SignIn. \nPress 2 to SignUp . \nPress 3 to check marks")
        c=int(input("Enter your choice: "))
        if c == 1:
             TLentry()
        if c == 2:
            Tdentry()
        

menu()

# TLogin()
# Tdetails()
# SLogin()
# Sdetails()