import mysql.connector as C
       
def createDatabase():
    conn=C.connect(host="localhost",user="root",password="")
    cur=conn.cursor()
    command=cur.execute("CREATE DATABASE IF NOT EXISTS Hospital")
    if not command:
        print("Database Created")
    else :
        print("Database Exists")
def connect():
        conn=C.connect(host="localhost",user="root",password="",db="hospital")
        if not conn:
            print("Failed to connect")
        return conn
def createAdmin():
    conn=connect()
    cur=conn.cursor()
    command=cur.execute("CREATE TABLE IF NOT EXISTS  admin(id INT AUTO_INCREMENT KEY,username VARCHAR(20),password VARCHAR(20))")
    query = "INSERT INTO admin (username, password) VALUES (%s, %s)"
    val =("ADM001", "001")
    cur.execute(query, val)
    val=("ADM002", "002")
    cur.execute(query, val)
    conn.commit()
    return conn

def validateAdmin(username,password):
    conn=createAdmin()
    cur=conn.cursor()
    query="SELECT * from admin where username=%s and password=%s"
    cur.execute(query,(username,password))
    result=len(cur.fetchall())
    return result

def createPatient(val):
    conn=connect()
    cur=conn.cursor()
    command=cur.execute("CREATE TABLE IF NOT EXISTS  patient(id INT AUTO_INCREMENT KEY,patient_id VARCHAR(7),name VARCHAR(20),mName VARCHAR(20),lName VARCHAR(20),contact_no VARCHAR(20),eContact VARCHAR(20),address VARCHAR(20),bg VARCHAR(20),height VARCHAR(20),weight VARCHAR(20),disease VARCHAR(20),doctor VARCHAR(20))")
    query="INSERT INTO patient (patient_id,name,mName,lName,contact_no,eContact,address,bg,height,weight,disease,doctor) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(query,val)
    conn.commit()

def createMedicine(val):
    conn=connect()
    cur=conn.cursor()
    command=cur.execute("CREATE TABLE IF NOT EXISTS medicine(id INT AUTO_INCREMENT KEY,med_id VARCHAR(7),drug_name VARCHAR(20),man_com VARCHAR(20),man_date VARCHAR(20),exp_date VARCHAR(20),des VARCHAR(100),stock VARCHAR(20),price VARCHAR(20))")
    query="INSERT INTO medicine (med_id,drug_name,man_com,man_date,exp_date,des,stock,price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(query,val)
    conn.commit()

def createEmployee(val):
    conn=connect()
    cur=conn.cursor()
    command=cur.execute("CREATE TABLE IF NOT EXISTS employee(id INT AUTO_INCREMENT KEY,emp_id VARCHAR(7),first_name VARCHAR(20),mid_name VARCHAR(20),last_name VARCHAR(20),contact_no VARCHAR(20),eContact VARCHAR(20),rel_contact VARCHAR(20),address VARCHAR(20),experience  VARCHAR(20),salary VARCHAR(20),joining_date VARCHAR(20) ,hours VARCHAR(20),prof VARCHAR(20))")
    query="INSERT INTO employee (emp_id,first_name,mid_name,last_name,contact_no,eContact,rel_contact,address,experience,salary,joining_date,hours,prof)  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(query,val)
    conn.commit()