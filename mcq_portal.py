import mysql.connector

def registration(captcha,myc):
    def l_teacher():
        Username = input("Enter your name: ")
        Password = input("Enter your password: ")
        Confirm_password = input("Confirm your password: ")

        if Password != Confirm_password:   
            print("Passwords do not match.")
            password = input("Re-enter new password: ")
            Confirm_password = input("Re-confirm password: ")
        elif len(password)<8 or len(password)>30:
            print("Password should be between 8 and 30 characters long.")
            password = input("Re-enter new password: ")
            Confirm_password = input("Re-confirm password: ")
            else: