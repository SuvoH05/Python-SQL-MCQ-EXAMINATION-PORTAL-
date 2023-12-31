import mysql.connector as mq
import csv
from datetime import date
pwsd = input("Enter your password: ")
db = input("Enter your database: ")
def Tdetails():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Tdetails ")
    myc.execute("create table Tdetails(uid int, TID int, Name varchar(35), dob date, Salary float, doj date, Subject varchar(50), Contact bigint, primary key(TID),foreign key(uid) references Tlogin(uid))")
    myc.execute("commit")
    myc.close()


def TLogin():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Tdetails ")
    myc.execute("drop table if exists TLogin ")
    myc.execute("create table TLogin(uid int, pwd varchar(10), primary key(uid))")
    myc.execute("commit")
def Sdetails():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Sdetails ")
    myc.execute("create table Sdetails(uid int, SID varchar(15), Name varchar(35), class int, dob date, Contact bigint, primary key(SID),foreign key(uid) references Slogin(uid))")
    myc.execute("commit")
    myc.close()

def SMarks():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists SMarks ")
    myc.execute("create table SMarks(uid int, Marks int, foreign key(uid) references Slogin(uid))")
    myc.execute("commit")
    myc.close()
     
def Sdentry():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
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
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    name = input("Enter your username(uid)")
    passw = input("Enter your new Password:")
    q="select pwd from SLogin where uid='{}'".format(name)
    myc.execute(q)
    x=myc.fetchone()
    if passw == x[0]:
         print ("Login Sucessfull")
         Soption(name)
    else:
         print("Person Not Found")
    myc.close()

def TLentry():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    name = input("Enter your username(uid)")
    passw = input("Enter your new Password:")
    q="select pwd from TLogin where uid='{}'".format(name)
    myc.execute(q)
    x=myc.fetchone()
    if passw == x[0]:
         print ("Login Sucessfull")
         Toption(name)
    else:
         print("Person Not Found")
    myc.close()
def Tdentry():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
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
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
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

def Toption(tid):
    print("~Teacher MENU~ \nPress 1 to Upload Question paper. \nPress 2 to Check marks of the students. \nPress 3 to check Your Profile")
    # choice = int(input("Enter your choice: "))
    # if choice == 1:
         
def Soption(uid):
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    # today = date.today()
    print("~Student MENU~ \nPress 1 to Check available exams. \nPress 2 to Check Marks. \nPress 3 to check Your Profile")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        check_exams()
        p=5
        q="insert into smarks values(%s,%s,%s)"
        myc.execute(q,(uid,p))
        mydb.commit()
    if choice == 2:
        query="select * from smarks where uid=%s"
        myc.execute(query,(uid,))
        marks = myc.fetchone()
        print("Your Marks : ",marks[1])

def Exam():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Exam1 ")
    myc.execute("create table Exam1(QID varchar(5),question varchar(255),op1 varchar(100),op2 varchar(100),op3 varchar(100),op4 varchar(100),primary key(QID))")
    myc.execute("commit")
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Exam2 ")
    myc.execute("create table Exam2(QID varchar(5),question varchar(255),op1 varchar(100),op2 varchar(100),op3 varchar(100),op4 varchar(100),primary key(QID))")
    myc.execute("commit")
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Exam3 ")
    myc.execute("create table Exam3(QID varchar(5),question varchar(255),op1 varchar(100),op2 varchar(100),op3 varchar(100),op4 varchar(100),primary key(QID))")
    myc.execute("commit")
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Exam4 ")
    myc.execute("create table Exam4(QID varchar(5),question varchar(255),op1 varchar(100),op2 varchar(100),op3 varchar(100),op4 varchar(100),primary key(QID))")
    myc.execute("commit")
def Qupdate():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    csvname = input("Enter the name of your file: ")
    tname = csvname[0:-4]
    fl=open(csvname,"r")
    file=csv.reader(fl,delimiter=",")
    for row in file:
        query = f"insert into {tname} values (%s,%s,%s,%s,%s,%s)"
        myc.execute(query,(row[0],row[1],row[2],row[3],row[4],row[5]))
        myc.execute("commit")
# def check_exams():
#     mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
#     myc=mydb.cursor()
#     myc.execute("show tables")
#     exams=myc.fetchall()
#     print(exams)
#     e1=[]
#     print("~AVAILABLE EXAMS~")
#     for items in exams:
#         e1.append(items[0])
#     for i in range(len(e1)):
#         if e1[i][0:4]=="exam":
#              print(i+1,". ",e1[i])
def check_exams():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("Show tables")
    exams = myc.fetchall()
    e1=[]
    for item in exams:
        e1.append(item[0])
    print("~AVAILABLE EXAMS~")
    for item in e1:
         if(item[0:4]=="exam"):
              print(item)
    choice = input("Enter the exam you want to appear: ")
    ans="answer"+choice[4::]+".csv"
    print(ans)
    a_list=ans_list(ans)
    print(a_list)
    if choice in e1 :
        myc.execute(f"select qid from {choice}")
        qids = myc.fetchall()
    qid=[]
    for item in qids:
        qid.append(item[0])
    # print(qid)
    marks=0
    for i in range(len(qid)):
        opt=["A","B","C","D"]
        qn = "QC0"+str(i+1)
        # myc.execute(f"select question from {choice} where qid="{}"".format(qn))
        query = f"select question from {choice} where qid=%s"
        myc.execute(query,(qn,))
        p=myc.fetchone()
        print(i+1,".",p[0])
        query = f"select op1 from {choice} where qid=%s"
        myc.execute(query,(qn,))
        a=myc.fetchone()
        print("A.",a[0])
        query = f"select op2 from {choice} where qid=%s"
        myc.execute(query,(qn,))
        b=myc.fetchone()
        print("B.",b[0])
        query = f"select op3 from {choice} where qid=%s"
        myc.execute(query,(qn,))
        c=myc.fetchone()
        print("C.",c[0])
        query = f"select op4 from {choice} where qid=%s"
        myc.execute(query,(qn,))
        d=myc.fetchone()
        print("D.",d[0])
        x=input("Enter YOUR FUCKING CHOICE: ")
        if x == a_list[i][1]:
             marks+=1
        else:
             print("WRONG ANSWER !! U DUMBASS - .. Must be women ☕ hahaahahah")
    print("TOTAL MARKS: ",marks)
    return marks

def ans_list(a):
    fl=open(a,"r")
    file=csv.reader(fl,delimiter=",")
    q="A"
    answers=[]
    for row in file:
        answers.append(row)
    # print(answers)
    return answers
            
        

# Exam()
# Qupdate()
# check_exams()
# SMarks()
# Soption()
# ans()
SLentry()
# menu()
# TLogin()
# Tdetails()
# SLogin()
# Sdetails()