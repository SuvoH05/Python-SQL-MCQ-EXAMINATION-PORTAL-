import mysql.connector as mq
import csv
from datetime import date

def titlee():
    print()
    print()
    print()
    print("\t\t        ******************************\n"
                "\t\t\t| ~ MCQ EXAMINATION PORTAL ~ |\n"
          "\t\t        ******************************\n"
                )
    print("")
def Tdetails():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Tdetails ")
    myc.execute("create table Tdetails(uid varchar(20), TID int, Name varchar(35), dob date, Salary float,doj date, Subject varchar(50), Contact bigint, primary key(TID),foreign key(uid) references Tlogin(uid))")
    myc.execute("commit")
    myc.close()

def Sdetails():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Sdetails ")
    myc.execute("create table Sdetails(uid varchar(20), SID varchar(15), Name varchar(35), class int, dob date, Contact bigint, primary key(SID),foreign key(uid) references Slogin(uid))")
    myc.execute("commit")
    myc.close()

def SLogin():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Sdetails ")
    myc.execute("drop table if exists SLogin ")
    myc.execute("create table SLogin(uid varchar(20), pwd varchar(10), primary key(uid))")
    myc.execute("commit")
    myc.close()

def TLogin():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists Tdetails ")
    myc.execute("drop table if exists TLogin ")
    myc.execute("create table TLogin(uid varchar(20), pwd varchar(10), primary key(uid))")
    myc.execute("commit")

def SMarks():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("drop table if exists SMarks ")
    myc.execute("create table SMarks(uid varchar(20), Marks int)")
    myc.execute("commit")
    myc.close()
     
def Sdentry():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    uid=input("Enter your User-ID: ")
    sid=input("Enter your Student-ID(RollNo.): ")
    pwd=input("Enter the password: ")
    name=input("Enter your name: ")
    dob=input("Enter your date of birth(YYYY-MM-DD): ")
    clas=int(input("Enter the class: "))
    con=int(input("Enter your contact no: "))
    info="INSERT into Sdetails values ('{}','{}','{}',{},'{}',{})".format(uid,sid,name,clas,dob,con)
    info1="INSERT into SLogin values ('{}','{}')".format(uid,pwd)
    myc.execute(info1)
    myc.execute(info)
    myc.execute("commit")
    myc.close()
    Smenu()
def SLentry():
    print()
    print("\t\t        ********************\n"
                "\t\t\t| ~ S I G N  I N ~ |\n"
          "\t\t        ********************\n","\t")
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    uid = input("Enter your username(uid): ")
    passw = input("Enter your Password: ")
    q="select pwd from SLogin where uid='{}'".format(uid)
    myc.execute(q)
    x=myc.fetchone()
# try:
    if passw == x[0]:
        print ("Login Sucessfull")
        Soption(uid)
    else:
        print("Person Not Found")
        SLentry()
# except TypeError:
    print("Type Error... try again.")
    Smenu()
    myc.close()

def TLentry():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    name = input("\nEnter your username(uid): ")
    passw = input("Enter your new Password: ")
    print()
    q="select pwd from TLogin where uid='{}'".format(name)
    myc.execute(q)
    x=myc.fetchone()
    try:
        if passw == x[0]:
            print ("Login Sucessfull")
            Toption(name)
        else:
            print("Person Not Found.")
    except TypeError:
        print("TypeError try agin...")
        Tmenu()
    myc.close()
def Tdentry():
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    print("Signing you up......")
    try:
        uid=input("Enter your Teacher-ID: ")
        tid=input("Enter your Teacher-ID(Roll.): ")
        pwd=input("Enter your password-")
        name=input("Enter your name: ")
        sub=input("Enter the suject you are expertised in: ")
        dob=input("Enter your Date of Birth(yyyy-mm-dd): ")
        sal=float(input("Enter your Salary: "))
        doj=input("Enter your Date of Joining(yyyy-mm-dd): ")
        con=int(input("Enter your contact no: "))
        info="INSERT into Tdetails values ('{}',{},'{}','{}',{},'{}','{}',{})".format(uid,tid,name,dob,sal,doj,sub,con)
        info1="INSERT into TLogin values ('{}','{}')".format(uid,pwd)
        myc.execute(info1)
        myc.execute(info)
        myc.execute("commit")
        Tmenu()
    except ValueError:
        print("Error!... Sign up and Try again.")
        Tmenu()
    myc.close()


def menu():
    print("\t   ENTER 1 IF YOU ARE A STUDENT. \n\t   ENTER 2 IF YOU ARE A TEACHER.\n\t   ENTER 3 TO EXIT.\n")
    try:
        a=int(input("Enter your choice: "))
        if a == 1:
            Smenu()
        if a == 2:
            Tmenu()
        if a == 3:
            exit
        elif a !=1 and a !=2 and a !=3 :
                print("Wrong input ! . . . enter your choice again....")
                menu()
    except ValueError:
        print("Value Error! Try Again..")
        menu()

def Smenu():
        print()
        print("\t\t        *******************************\n"
                "\t\t\t| ~ S T U D E N T   M E N U ~ |\n"
          "\t\t        *******************************\n","\n\t   PRESS 1 TO SIGNIN. \n\t   PRESS 2 TO SIGNUP . \n\t   PRESS 3 TO GO BACK TO MAIN MENU")
        print()
        try:
            c=int(input("Enter your choice: "))
            if c == 1:
                SLentry()
            if c == 2:
                Sdentry()
            if c == 3:
                menu()
            elif c != 1 and c != 2 and c != 3:
                print("Wrong input ! . . . enter your choice again....")
                Smenu()
        except ValueError:
            print("ValueError! Try again....")
            Smenu()
            
def Tmenu():
        print()
        print("\t\t        *******************************\n"
                "\t\t\t| ~ T E A C H E R   M E N U ~ |\n"
          "\t\t        *******************************\n","\t   PRESS 1 TO SIGNIN. \n\t   PRESS 2 TO SIGNUP . \n\t   PRESS 3 TO GO BACK TO MAIN MENU")
        print()
        try:
            c=int(input("Enter your choice: "))
            if c == 1:
                TLentry()
            if c == 2:
                Tdentry()
            if c == 3:
                menu()
            elif c != 1 and c != 2 and c != 3:
                    print("Wrong input ! . . . enter your choice again....")
                    Tmenu()
        except ValueError:
            print("ValueError! Please Enter numeric value.")
            Tmenu()
def Toption(tid):
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    #print("~Teacher MENU~ \nPress 1 to Upload Question paper. \nPress 2 to Check marks of the students. \nPress 3 to check Your Profile")
    print()
    print("\t\t        *********************\n"
                "\t\t\t| ~ O P T I O N S ~ |\n"
          "\t\t        *********************\n","\t \nPress 1 to Upload question paper. \nPress 2 to Check Marks of the students. \nPress 3 to LOG OUT")
    print()
    try:
        choice = int(input("Enter your choice: "))
        if (choice) == 1:
            Qupdate(tid)
            Toption(tid)
        if (choice) == 2:
            myc.execute("select * from smarks")
            marks=myc.fetchall()
            print("\n\t\t        **********************\n"
                "\t\t\t| ~ Students Marks ~ |\n"
          "\t\t        **********************\n")
            for i in range(len(marks)):
                print("\t\tStudent:",marks[i][0],", Marks",marks[i][1])
            Toption(tid)
        if (choice) == 3:
            Tmenu()
        elif (choice) !=1 and choice !=2 and choice !=3 :
            print("Wrong input ! . . . enter your choice again....")
            Toption(tid)
    except ValueError:
        print('Value Error')
        Toption(tid)
         
def Soption(uid):
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    # today = date.today()
    print()
    print("\t\t        *********************\n"
                "\t\t\t| ~ O P T I O N S ~ |\n"
          "\t\t        *********************\n","\t \nPress 1 to Check available exams. \nPress 2 to Check Marks. \nPress 3 to LOG OUT\n")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            check_exams(uid)
            Soption(uid)
        if choice == 2:
            query="select * from smarks where uid=%s"
            myc.execute(query,(uid,))
            marks = myc.fetchall()
            print("\n\t\tYOUR MARKS :- ")
            for i in range(len(marks)):
                print("\t\tExam no.",i+1," Marks: ",marks[i][1])
            Soption(uid)
        if choice == 3:
            menu()
        
        elif choice !=1 and choice !=2 and choice !=3 :
            print("Wrong input ! . . . enter your choice again....")
            Soption(uid)
    except (ValueError):
        print('Value Error')
        Soption(uid)

def Exam(x):
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    q1=f"drop table if exists {x}"
    myc.execute(q1)
    q2=f"create table {x} (QID varchar(5),question varchar(255),op1 varchar(100),op2 varchar(100),op3 varchar(100),op4 varchar(100),primary key(QID))"
    myc.execute(q2)
    myc.execute("commit")
    
def Qupdate(tid):
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    try:
        csvname = input("Enter the name of your file with extension: ")
        tname = csvname[0:-4]
        fl1=open(csvname,"r")
        Exam(tname)
        file=csv.reader(fl1,delimiter=",")
        for row in file:
            query = f"insert into {tname} values (%s,%s,%s,%s,%s,%s)"
            myc.execute(query,(row[0],row[1],row[2],row[3],row[4],row[5]))
            myc.execute("commit")
        
    except :
        print("File not found! Please re-enter.")
        Toption(tid)
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
def check_exams(n):
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("Show tables")
    exams = myc.fetchall()
    e1=[]
    for item in exams:
        e1.append(item[0])
    print()
    print("\t\t        ***********************\n"
                "\t\t\t| ~ Available Exams ~ |\n"
          "\t\t        ***********************\n")
    
    count=0
    for item in e1:
         if(item[0:4]=="exam"):
              count=count+1
              print(count,".",item)
    print()
    choice = input("Enter the exam you want to appear: ")
    ans="answer"+choice[4::]+".csv"
    # print(ans)
    a_list=ans_list(ans)
    # print(a_list)
    if choice in e1 :
        myc.execute(f"select qid from {choice}")
        qids = myc.fetchall()
    try:
        qid=[]
        for item in qids:
            qid.append(item[0])
    except UnboundLocalError:
        print("No such exam exists.")
        check_exams(n)
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
        if x == a_list[i][1] or x == a_list[i][1].lower():
             marks+=1
        else:
             print("WRONG ANSWER !! ")    #U DUMBASS - .. Must be women ☕ hahaahahah
    print("TOTAL MARKS: ",marks)
    q="insert into smarks values(%s,%s)"
    myc.execute(q,(n,marks))
    mydb.commit()

def ans_list(a):
    try:
        fl=open(a,"r")
        file=csv.reader(fl,delimiter=",")
    except FileNotFoundError:
        print("File not found... Enter again.")
        Soption(a)
    #q="A"
    answers=[]
    for row in file:
        answers.append(row)
    # print(answers)
    return answers
            
def db_Tcheck(pwsd,db):
    mydb=mq.connect(host="localhost",user="root",password=pwsd,database=db)
    myc=mydb.cursor()
    myc.execute("Show tables")
    values=['exam1', 'exam2', 'exam3', 'exam4', 'sdetails', 'slogin', 'smarks', 'tdetails', 'tlogin']
    tables = myc.fetchall()
    l=[]
    for i in range(len(tables)):
        l.append(tables[i][0])
    
    if all(value in l for value in values):
        # print("1")    code checking 
        titlee()
        menu()
    else:
        print("Creating required databases......")
        SLogin()       
        Sdetails()
        TLogin()
        Tdetails()
        SMarks()
        #print("2")    code checking
        menu()         

pwsd = input("Enter your MySql password: ")
db =input("Enter The database you want to use: ")
def db_check(pwsd,db):
    mydb=mq.connect(host="localhost",user="root",password=pwsd)
    myc=mydb.cursor()
    myc.execute("show databases")
    dbb=myc.fetchall()
    l1=[]
    for i in range(len(dbb)):
        l1.append(dbb[i][0])
    if db in l1:
        # print("true")
        db_Tcheck(pwsd,db)
    elif db != l1:
        print("Database doesnot exist.\nPlease enter the correct Database name.\nclosing.....")
    # print(l1)
    # if db in l1:
    #     db_Tcheck()
    # else:
    #     print("Wrong Database input...Try again with corrent database name and password..")
    #     db_check(pwsd,db)
db_check(pwsd,db)

# titlee()
# Exam()

# Qupdate()
# check_exams()
# Soption()
# ans()

# SLentry()
# print("")
# menu() 
