from PyQt5 import QtCore, QtWidgets,sip
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Regex import Regex
import Database
import sys


class AboutUs(QWidget):
    def __init__(self):
        super(AboutUs,self).__init__()
        self.setGeometry(200,30,1480,1000)
        self.setFixedSize(1480,1000)
        self.setWindowTitle("About Us")
        style="""
        QLabel#aboutUS
        {
            font-size: 18px;
            font-family: Arial, sans-serif;
            color: black;
            font-weight: 250;
        }
        QWidget
        {
            background-color: #5FB3CE;   
        }
        QWidget#title
        {
            font-size: 40px;
            font-family: Arial, sans-serif;
            font-weight: 2000;
        }
        QFrame
        {
            background: white;
            border-radius: 10px; 
            font-family: Arial, sans-serif;
        }
        QPushButton#Exitbtn
        {
                background: transparent;
                border: transparent;
                color: #5FB3CE;
                font-size: 20px;
                font-weight: 500;
                padding:5px;
        }
        QPushButton#Exitbtn:hover
            {
                border-bottom: 3px solid #5FB3CE;
            }
        """
        self.setStyleSheet(style)
        self.myUI()
    def goAdmin(self):
        self.adminWindow=Admin()
        self.hide()
        self.adminWindow.show()
    def myUI(self):
        self.hbox=QHBoxLayout()
        self.loginFrame=QtWidgets.QFrame(self)
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFixedSize(1400,500)

        self.title=QLabel(self.loginFrame)
        self.exit=QPushButton(self.loginFrame)
        self.exit.move(20,10)
        self.exit.setObjectName("Exitbtn")
        self.exit.clicked.connect(self.goAdmin)
        self.exit.setText("Exit")
        self.title.setText("About Us")
        self.title.setObjectName("title")
        self.title.move(600,20)
        
        self.aboutUS=QLabel(self.loginFrame)
        self.aboutUS.setObjectName("aboutUS")
        about='''
Our Project is a Hospital Database Management software. It is a system that minimizes the physical pen paper work at the hospitals. The system maintains the records of the 
patients, doctors and medicines. The authorized user can access, update and add all the information with just one click.
It’s easy to use user interface makes sure that even those who are not familiar to computers can easily operate the system. This system allows the Hospital 
admin department function quickly which can save the crucial minutes in the event of an emergency. 
This project is made by Pranshu Padia, Aagam Parekh, Lavhith Pragada and Siddh Sanghvi.
Everyone in this project contributed their skills equally therefore making this project possible.
Regards'''
        self.aboutUS.setText(about)
        self.aboutUS.move(10,100)
        self.hbox.addWidget(self.loginFrame)
        self.setLayout(self.hbox)

class Medicine(QWidget):
    def __init__(self):
        super(Medicine,self).__init__()
        self.setGeometry(200,30,1480,1000)
        self.setFixedSize(1480,1000)
        self.setWindowTitle("Login-Admin Mode-Medicine_Managment")
        style = """
             QWidget
            {
                 background-color: #5FB3CE;   
            }
            QFrame
            {
                background: white;
                border-radius: 20px; 
                font-family: Arial, sans-serif;
            }
            QWidget#MM
            {
               font-size: 35px;
               font-weight: 2500;
               color: #5FB3CE;
            }
            QFrame#TitleFrame
            {
                 background: white;
            }
            QWidget#MEDB 
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
            }
            QLabel#MEDLAB 
            {
                font-size: 18px;
                font-family: Arial, sans-serif;
                color: black;
                font-weight: 250;
            }
            QLabel#MELAB 
            {
                font-size: 15px;
                font-family: Arial, sans-serif;
                color: black;
                font-weight: 250;
            }
            QWidget#ADDBOX 
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
                border-radius: 0px;
            }
           QPushButton#Addbtn
            {
                background: #5FB3CE;
                border: 2px solid #5FB3CE;
                border-radius: 10px;
                padding: 10px;
                color: white;
                font-size: 15px;
                font-weight: 1000; 
                margin: 2px;
            }
             QPushButton#Addbtn:hover
            {
                Background: white;
                color: #5FB3CE;
             }
            QPushButton#Exitbtn
            {
                background: transparent;
                border: transparent;
                color: #5FB3CE;
                font-size: 20px;
                font-weight: 500;
                padding:5px;
            }
            QPushButton#Exitbtn:hover
            {
                border-bottom: 3px solid #5FB3CE;
            }
             QTextEdit#pres
             {
                 padding: 15px;
                background:rgb(245,245,245);
                font-size:20px;
                font-weight:500;
                font-family: Arial, sans-serif;
             }
    
    """
        self.setStyleSheet(style)
        self.myUI()

    def selectedCell(self):
        self.conn=Database.connect()
        cur = self.conn.cursor()
        self.index = self.tableWidget.selectedItems()

        query = "SELECT med_id,drug_name,man_com,man_date,exp_date,des,stock,price FROM medicine WHERE med_id=%s"
        value = (self.index[0].text(),)
        try:
            cur.execute(query,value)
            row = cur.fetchone()

            if row:
             
                self.medIDLine.setText(row[0])
                self.drugLine.setText(row[1])
                self.manufacturerLine.setText(row[2])
                self.qdate = QtCore.QDate.fromString(row[3], "d-MMM-yyyy")
                self.mfg.setDate(self.qdate)
                self.Edate = QtCore.QDate.fromString(row[4], "d-MMM-yyyy")
                self.exp.setDate(self.Edate)   
                self.descText.setPlainText(row[5])
                self.stockMenu.setCurrentText(row[6])
                self.priceLine.setText(row[7])
        except:
            print("Failed!!")
    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(layout)
    def reset(self):
        self.medIDLine.clear()
        self.drugLine.clear()
        self.manufacturerLine.clear()
        self.descText.clear()
        self.p=self.priceLine.clear()
        self.deleteLayout(self.textFrame.layout())
    def updateRecord(self):
        count=self.validateInputs()
        if count==5:
            self.MedID=self.medIDLine.text()
            self.drugname=self.drugLine.text()
            self.manufact=self.manufacturerLine.text()
            self.mfgdate=self.mfg.text()
            self.expdate=self.exp.text()
            self.description=self.descText.toPlainText()
            self.stock=str(self.stockMenu.currentText()) 
            self.p=self.priceLine.text()
            conn=Database.connect()
            self.cur=conn.cursor()
            self.query="UPDATE medicine SET drug_name=%s,man_com=%s,man_date=%s,exp_date=%s,des=%s,stock=%s,price=%s WHERE med_id=%s"
            val=(self.drugname,self.manufact,self.mfgdate,self.expdate,self.description,self.stock,self.p,self.MedID)
            self.cur.execute(self.query, val)
            self.loadDB()
            self.addText()
            conn.commit()
    def loadDB(self):
        self.conn=Database.connect()
        self.query="SELECT med_id,drug_name,man_com,man_date,exp_date,des,stock,price FROM medicine"
        self.cur=self.conn.cursor()
        self.cur.execute(self.query)
        record=self.cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(record):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def addRecord(self):
        count=self.validateInputs()
        if count==5:
            self.stock=str(self.stockMenu.currentText())
            self.mfgdate=self.mfg.text()
            self.expdate=self.exp.text()
            self.addText()
            self.val=(self.MedID,self.drugname,self.manufact,self.mfgdate,self.expdate,self.description,self.stock,self.p)
            Database.createMedicine(self.val)
            self.loadDB()
    def deleteRecord(self):
        self.conn=Database.connect()
        cur=self.conn.cursor()
        self.medID=self.medIDLine.text()
        self.query="DELETE FROM medicine WHERE med_id =%s"
        values=(self.medID,)
        cur.execute(self.query,values)
        self.conn.commit()
        self.loadDB()
    def addText(self):
        self.stock=str(self.stockMenu.currentText())
        self.hbox=QHBoxLayout()
        self.info=QTextEdit(self.textFrame)
        self.info.setObjectName("pres")
        self.info.insertPlainText(f"\tMEDICINE PREVIEW\n\n")
        self.info.insertPlainText(f"Medicine ID: {self.MedID}\n")
        self.info.insertPlainText(f"Drug Name: {self.drugname} \n")
        self.info.insertPlainText(f"Maufacturing Company: {self.manufact}\n")
        self.info.insertPlainText(f"Manufacturing Date: {self.mfgdate}\n")
        self.info.insertPlainText(f"Expiry Date: {self.expdate}\n")
        self.info.insertPlainText(f"Description: {self.description}\n")
        self.info.insertPlainText(f"Stock Available: {self.stock}\n")
        self.info.insertPlainText(f"Price: Rs {self.p}\n")
         
        self.hbox.addWidget(self.info)
        self.textFrame.setLayout(self.hbox)
    def errorBox(self,mess,title):
        self.msg=QtWidgets.QMessageBox()
        self.msg.setWindowTitle(title)
        self.msg.setText(mess)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec()
    
    def validateInputs(self):
        #Medicine Id
        count=0
        self.MedID=self.medIDLine.text()
        R=Regex(self.MedID)
        if self.MedID!="":
            if R.isMedicineID()==True:
                count+=1
            else:
                self.errorBox("Medicine Id is Invalid ! Please Try Again","Input Error")
        else:
            self.errorBox("Medicine Id is Blank","Input Error")
        #Drug Name
        self.drugname=self.drugLine.text()
        R=Regex(self.drugname)
        if self.drugname!="":
            if R.isAlphaNum()==True:
                count+=1
            else:
                self.errorBox("Drug Name is Invalid ! Please Try Again","Input Error")
        else:
            self.errorBox("Drug Name is Blank","Input Error")
        #Manufacturer Name
        self.manufact=self.manufacturerLine.text()
        R=Regex(self.manufact)
        if self.manufact!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("Manufacturer Name is Invalid ! Please Try Again","Input Error")
        else:
            self.errorBox("Manufacturer Name is Blank","Input Error")
        
        #Description
        self.description=self.descText.toPlainText()
        R=Regex(self.description)
        if self.description!="":
            count+=1
        else:
            self.errorBox("Description is blank","Input Error")
        #Price
        self.p=self.priceLine.text()
        R=Regex(self.p)
        if self.p!="":
            if R.isNumber()==True:
                count+=1
            else:
                self.errorBox("Price is wrong","Input Error")
        else:
            self.errorBox("Price is blank","Input Error")
        
        return count
    def goAdmin(self):
        self.adminWindow=Admin()
        self.hide()
        self.adminWindow.show()  
    def myUI(self):
        self.vbox=QVBoxLayout()
        self.vbox2=QVBoxLayout()

        self.titleFrame=QtWidgets.QFrame(self)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setObjectName("TitleFrame")
        self.titleFrame.setFixedSize(1450,100)
        self.vbox.addWidget(self.titleFrame)

        self.titleLabel=QLabel(self.titleFrame)
        self.exit=QPushButton(self.titleFrame)
        self.exit.move(20,10)
        self.exit.setObjectName("Exitbtn")
        self.exit.clicked.connect(self.goAdmin)
        self.exit.setText("Exit")
        self.titleLabel.setObjectName("MM")
        self.titleLabel.setText("Medicine Management")
        self.titleLabel.resize(500,100)
        self.titleLabel.move(550,0)

        self.hbox=QHBoxLayout()
        self.infoFrame=QtWidgets.QFrame(self)
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFixedSize(950,550)
        self.hbox.addWidget(self.infoFrame)

        self.textFrame=QtWidgets.QFrame(self)
        self.textFrame.setFrameShape(QFrame.StyledPanel)
        self.textFrame.setFixedSize(500,550)
        self.hbox.addWidget(self.textFrame)
        self.vbox.addLayout(self.hbox)

        self.grid=QGridLayout()

        self.medIDLabel=QLabel()
        self.medIDLine=QLineEdit()
        self.medIDLabel.setText("Medicine Id:") 
        self.medIDLabel.setObjectName("MEDLAB")
        self.medIDLine.resize(300,20)
        self.medIDLine.setPlaceholderText("Medicine ID")
        self.medIDLine.setObjectName("MEDB")
        self.grid.addWidget(self.medIDLabel,0,0)
        self.grid.addWidget(self.medIDLine,0,1)

        self.mfgLabel=QLabel()
        self.mfg = QDateEdit()
        self.mfg.setDate(QDate(2021,10,18))
        self.mfgLabel.setText("Manufacturing Date:")
        self.mfgLabel.setObjectName("MEDLAB")
        self.mfg.setObjectName("MEDB")
        self.grid.addWidget(self.mfgLabel,4,0)
        self.grid.addWidget(self.mfg,4,1)

        self.expLabel=QLabel()
        self.exp = QDateEdit()
        self.exp.setDate(QDate(2022,10,18))
        self.expLabel.setText("Expiry Date:")
        self.expLabel.setObjectName("MEDLAB")
        self.exp.setObjectName("MEDB")
        self.grid.addWidget(self.expLabel,5,0)
        self.grid.addWidget(self.exp,5,1)

        self.drugLabel=QLabel()
        self.drugLine=QLineEdit()
        self.drugLabel.setText("Drug Name:")
        self.drugLabel.setObjectName("MEDLAB")
        self.drugLine.setPlaceholderText("Medicine Name")
        self.drugLine.setObjectName("MEDB")
        self.grid.addWidget(self.drugLabel,2,0)
        self.grid.addWidget(self.drugLine,2,1)

        self.manufacturerLabel=QLabel()
        self.manufacturerLine=QLineEdit()
        self.manufacturerLabel.setText("Manufacturer:")
        self.manufacturerLabel.setObjectName("MEDLAB")
        self.manufacturerLine.setPlaceholderText("Manufacturer Name")
        self.manufacturerLine.setObjectName("MEDB")
        self.grid.addWidget(self.manufacturerLabel,3,0)
        self.grid.addWidget(self.manufacturerLine,3,1)

        self.descLabel=QLabel()
        self.descText=QTextEdit()
        self.descText.setFixedSize(520,50)
        self.descLabel.setText("Description:")
        self.descText.setPlaceholderText("Description of Medicine")
        self.descLabel.setObjectName("MEDLAB")
        self.descText.setObjectName("ADDBOX")
        self.grid.addWidget(self.descLabel,6,0)
        self.grid.addWidget(self.descText,6,1)
        
        self.stock=QLabel()
        self.stockMenu=QComboBox()
        self.stockMenu.addItems(["0-10","10-20","20-30","30-40","40-50","50-60","60-70","70-80","80-90","90-100","100+"])
        self.stock.setText("Stock Available (in packets):")
        self.stock.setObjectName("MEDLAB")
        self.stockMenu.setObjectName("MEDB")
        self.grid.addWidget(self.stock,7,0)
        self.grid.addWidget(self.stockMenu,7,1)

        self.priceLabel=QLabel()
        self.priceLine=QLineEdit()
        self.priceLabel.setText("Price:")
        self.priceLabel.setObjectName("MEDLAB")
        self.priceLine.setPlaceholderText("Price of Medicine (in Rs)")
        self.priceLine.setObjectName("MEDB")
        self.grid.addWidget(self.priceLabel,8,0)
        self.grid.addWidget(self.priceLine,8,1)
        
        self.addButton=QPushButton()
        self.addButton.setText("ADD")
        self.addButton.setObjectName("Addbtn")
        self.addButton.clicked.connect(self.addRecord)
        
        self.updateButton=QPushButton()
        self.updateButton.setText("UPDATE")
        self.updateButton.setObjectName("Addbtn")
        self.updateButton.clicked.connect(self.updateRecord)
        
        self.deleteButton=QPushButton()
        self.deleteButton.setText("DELETE")
        self.deleteButton.setObjectName("Addbtn")
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.resetButton=QPushButton()
        self.resetButton.setText("RESET")
        self.resetButton.setObjectName("Addbtn")
        self.resetButton.clicked.connect(self.reset)
        self.grid.addWidget(self.addButton,14,0)
        self.grid.addWidget(self.updateButton,14,1)
        self.grid.addWidget(self.deleteButton,14,2)
        self.grid.addWidget(self.resetButton,14,3)
    
        self.infoFrame.setLayout(self.grid)
        self.recordFrame=QtWidgets.QFrame(self)
        self.recordFrame.setFrameShape(QFrame.StyledPanel)
        self.recordFrame.setFixedSize(1450,300)


        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10) 
        self.tableWidget.setColumnCount(8)
        self.item=QTableWidgetItem("Medicine ID")
        self.tableWidget.setHorizontalHeaderItem(0, self.item)
        self.item=QTableWidgetItem("Drug Name")
        self.tableWidget.setHorizontalHeaderItem(1, self.item)
        self.item=QTableWidgetItem("Maufacturing Company")
        self.tableWidget.setHorizontalHeaderItem(2, self.item)
        self.item=QTableWidgetItem("Maufacturing Date")
        self.tableWidget.setHorizontalHeaderItem(3, self.item)
        self.item=QTableWidgetItem("Expiry Date")
        self.tableWidget.setHorizontalHeaderItem(4, self.item)
        self.item=QTableWidgetItem("Description")
        self.tableWidget.setHorizontalHeaderItem(5, self.item)
        self.item=QTableWidgetItem("Stock")
        self.tableWidget.setHorizontalHeaderItem(6, self.item)
        self.item=QTableWidgetItem("Price")
        self.tableWidget.setHorizontalHeaderItem(7, self.item)
        self.vbox2.addWidget(self.tableWidget)
        self.recordFrame.setLayout(self.vbox2)
        self.tableWidget.cellDoubleClicked.connect(self.selectedCell)
        self.tableWidget.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows)

        self.vbox.addWidget(self.recordFrame)
        self.setLayout(self.vbox)
class Employee(QWidget):
    def __init__(self):
        super(Employee,self).__init__()
        self.setGeometry(200,30,1480,1000)
        self.setFixedSize(1480,1000)
        self.setWindowTitle("Login-Admin Mode-Employee Managment")
        style = """
             QWidget
            {
                 background-color: #5FB3CE;   
            }
            QFrame
            {
                background: white;
                border-radius: 20px; 
                font-family: Arial, sans-serif;
            }
            QWidget#EM
            {
               font-size: 35px;
               font-weight: 2500;
               color: #5FB3CE;
            }
            QFrame#TitleFrame
            {
                 background: white;
            }
            QWidget#GENBOX
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
            }
            QLabel#GENLAB
            {
                font-size: 15px;
                font-family: Arial, sans-serif;
                color: black;
                font-weight: 250;
            }
            QWidget#ADDBOX
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
                border-radius: 0px;
            }
           QPushButton#Addbtn
            {
                background: #5FB3CE;
                border: 2px solid #5FB3CE;
                border-radius: 10px;
                padding: 10px;
                color: white;
                font-size: 15px;
                font-weight: 1000; 
                margin: 2px;
            }
             QPushButton#Addbtn:hover
            {
                Background: white;
                color: #5FB3CE;
             }
            QPushButton#Exitbtn
            {
                background: transparent;
                border: transparent;
                color: #5FB3CE;
                font-size: 20px;
                font-weight: 500;
                padding:5px;
            }
            QPushButton#Exitbtn:hover
            {
                border-bottom: 3px solid #5FB3CE;
            }
             QTextEdit#pres
             {
                 padding: 15px;
                background:rgb(245,245,245);
                font-size:20px;
                font-weight:500;
                font-family: Arial, sans-serif;
             }
    
    """
        self.setStyleSheet(style)
        self.myUI()
    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(layout)
    def reset(self):
        self.employeeIDLine.clear()
        self.nameLine.clear()
        self.midNameLine.clear()
        self.lastNameLine.clear()
        self.contactLine.clear()
        self.eContactLine.clear()
        self.eContactRLine.clear()
        self.addressText.clear()
        self.SalaryLine.clear()
        self.ExperienceMenu.clear()
        self.ProfessionMenu.clear()
        self.WorkingMenu.clear()
        self.deleteLayout(self.textFrame.layout())
    def deleteRecord(self):
        self.conn=Database.connect()
        cur = self.conn.cursor()
        self.query = "DELETE FROM employee WHERE emp_id = %s"
        values = (self.employeeIDLine.text(),)
        cur.execute(self.query, values)
        self.conn.commit()
        self.loadDB()
    def loadDB(self):
        self.conn=Database.connect()
        self.query="SELECT emp_id,first_name,mid_name,last_name,contact_no,eContact,rel_contact,address,experience,salary,joining_date,hours,prof from employee"
        self.cur=self.conn.cursor()
        self.cur.execute(self.query)
        record=self.cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(record):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    def updateRecord(self):
        count=self.validateInputs()
        if count==9:
            self.employeeID=self.employeeIDLine.text()
            print(self.employeeID)
            self.firstName=self.nameLine.text()
            print(self.firstName)
            self.midName=self.midNameLine.text()
            print(self.midName)
            self.lastName=self.lastNameLine.text()
            print(self.lastName)
            self.contact=self.contactLine.text()
            print(self.contact)
            self.eContact=self.eContactLine.text()
            print(self.eContact)
            self.eContactRelation=self.eContactRLine.text()
            print(self.eContactRelation)
            self.address=self.addressText.toPlainText()
            print(self.address)
            self.Salary=self.SalaryLine.text()
            print(self.Salary)
            self.exp=self.ExperienceMenu.currentText()
            print(self.exp)
            self.Prof=self.ProfessionMenu.currentText()
            print(self.Prof)
            self.workinghrs=self.WorkingMenu.currentText()
            print(self.workinghrs)
            self.JoinDate=self.Jdate.text()
            print(self.JoinDate)

            self.conn=Database.connect()
            self.cur=self.conn.cursor()
            self.query="UPDATE employee SET first_name=%s,mid_name=%s,last_name=%s,contact_no=%s,eContact=%s,rel_contact=%s,address=%s,experience=%s,salary=%s,joining_date=%s,hours=%s,prof=%s  WHERE emp_id=%s"
            val=(self.firstName,self.midName,self.lastName,self.contact,self.eContact,self.eContactRelation,self.address,self.exp,self.Salary,self.JoinDate,self.workinghrs,self.Prof,self.employeeID,)
            self.cur.execute(self.query, val)
            self.conn.commit()
            self.addText()
            self.loadDB()            
    def addText(self):
        self.hbox=QHBoxLayout()
        self.info=QTextEdit(self.textFrame)
        self.info.setObjectName("pres")
        self.info.insertPlainText(f"\t\tPREVIEW\n\n")
        self.info.insertPlainText(f"Employee ID: {self.employeeIDLine.text()}\n")
        self.info.insertPlainText(f"Name: {self.nameLine.text()} {self.midNameLine.text()} {self.lastNameLine.text()}\n")
        self.info.insertPlainText(f"Emergency Contact: {self.eContactLine.text()}\n")
        self.info.insertPlainText(f"Relation Emergency Contact: {self.eContactRLine.text()}\n")
        self.info.insertPlainText(f"Joining Date: {self.Jdate.text()}\n")
        self.info.insertPlainText(f"Address: {self.addressText.toPlainText()}\n")
        self.info.insertPlainText(f"Experience: {self.ExperienceMenu.currentText()}\n")
        self.info.insertPlainText(f"Salary: {self.SalaryLine.text()}\n")
        self.info.insertPlainText(f"Profession: {self.ProfessionMenu.currentText()}\n")
        self.info.insertPlainText(f"Working Hours: {self.WorkingMenu.currentText()}\n")
        
        self.hbox.addWidget(self.info)
        self.textFrame.setLayout(self.hbox)
    def addRecord(self):
        count=self.validateInputs()
        if count==9:
            self.JoinDate=self.Jdate.text()
            self.Prof=str(self.ProfessionMenu.currentText())
            self.workinghrs=str(self.WorkingMenu.currentText())
            self.exp=str(self.ExperienceMenu.currentText())
            self.val=(self.employeeID,self.firstName,self.midName,self.lastName,self.contact,self.eContact,self.eContactRelation,self.address,self.exp,self.Salary,self.JoinDate,self.workinghrs,self.Prof)
            Database.createEmployee(self.val)
            self.addText()
            self.loadDB()
    def errorBox(self,mess,title):
        self.msg=QtWidgets.QMessageBox()
        self.msg.setWindowTitle(title)
        self.msg.setText(mess)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec()
    
    def validateInputs(self):
        #Employee Id
        count=0
        self.employeeID=self.employeeIDLine.text()
        R=Regex(self.employeeID)
        if self.employeeID!="":
            if R.isEmployeeID()==True:
                count+=1
            else:
                self.errorBox("Employee Id is Invalid!Please Try Again","Input Error")
        else:
            self.errorBox("Employee Id is Blank","Input Error")
        #First Name
        self.firstName=self.nameLine.text()
        R=Regex(self.firstName)
        if self.firstName!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("First Name is Invalid!Please Try Again","Input Error")
        else:
            self.errorBox("First Name is Blank","Input Error")
        #Middle Name
        self.midName=self.midNameLine.text()
        R=Regex(self.midName)
        if self.midName!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("Middle Name is Invalid!Please Try Again","Input Error")
        else:
            self.errorBox("Middle Name is Blank","Input Error")
        #Last Name
        self.lastName=self.lastNameLine.text()
        R=Regex(self.lastName)
        if self.lastName!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("Last Name is Invalid!Please Try Again","Input Error")
        else:
            self.errorBox("Last Name is Blank","Input Error")
        #Contact No
        self.contact=self.contactLine.text()
        R=Regex(self.contact)
        if self.contact!="":
            if R.isContactNo()==True:
                count+=1
            else:
                self.errorBox("Contact No is Invalid!Please Try Again","Input Error")
        else:
            self.errorBox("Contact No is Blank","Input Error")
        #Emergency Contact
        self.eContact=self.eContactLine.text()
        R=Regex(self.eContact)
        if self.eContact!="":
            if R.isContactNo()==True:
                count+=1
            else:
                self.errorBox("Emergency Contact No is Invalid!Please Try Again","Input Error")
        else:
            self.errorBox("Emergency Contact No is Blank","Input Error")
        #Relation To Emergency Contact
        self.eContactRelation=self.eContactRLine.text()
        R=Regex(self.eContactRelation)
        if self.eContactRelation!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("Emergency Contact Relation is Invalid!Please Try Again","Input Error")
        else:
            self.errorBox("Emergency Contact Relation is Blank","Input Error")
        #Address
        self.address=self.addressText.toPlainText()
        R=Regex(self.address)
        if self.address!="":
            count+=1
        else:
            self.errorBox("Address is blank","Input Error")
        #Salary
        self.Salary=self.SalaryLine.text()
        R=Regex(self.Salary)
        if self.Salary!="":
           if R.isNumber()==True:
                count+=1
           else:
                self.errorBox("Salary is Invalid! Please Try Again","Input Error") 
        else:
            self.errorBox("Salary is blank","Input Error")
        return count
    def goAdmin(self):
        self.adminWindow=Admin()
        self.hide()
        self.adminWindow.show() 
    def myUI(self):
        self.vbox=QVBoxLayout()
        self.vbox2=QVBoxLayout()
        self.titleFrame=QtWidgets.QFrame(self)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setObjectName("TitleFrame")
        self.titleFrame.setFixedSize(1450,100)
        self.vbox.addWidget(self.titleFrame)

        self.titleLabel=QLabel(self.titleFrame)
        self.exit=QPushButton(self.titleFrame)
        self.exit.move(20,10)
        self.exit.setObjectName("Exitbtn")
        self.exit.clicked.connect(self.goAdmin)
        self.exit.setText("Exit")
        self.titleLabel.setObjectName("EM")
        self.titleLabel.setText("Employee Management")
        self.titleLabel.resize(500,100)
        self.titleLabel.move(550,0)

        self.hbox=QHBoxLayout()
        self.infoFrame=QtWidgets.QFrame(self)
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFixedSize(950,550)
        self.hbox.addWidget(self.infoFrame)

        self.textFrame=QtWidgets.QFrame(self)
        self.textFrame.setFrameShape(QFrame.StyledPanel)
        self.textFrame.setFixedSize(500,550)
        self.hbox.addWidget(self.textFrame)
        self.vbox.addLayout(self.hbox)

        self.grid=QGridLayout()
        self.employeeIDLabel=QLabel()
        self.employeeIDLine=QLineEdit()
        self.employeeIDLabel.setText("Employee Id:")
        self.employeeIDLabel.setObjectName("GENLAB")
        self.employeeIDLine.setPlaceholderText("Employee ID")
        self.employeeIDLine.setObjectName("GENBOX")
        self.grid.addWidget(self.employeeIDLabel,0,0)
        self.grid.addWidget(self.employeeIDLine,0,1)

        self.dateLabel=QLabel()
        self.date = QDateEdit()
        self.date.setDate(QDate(2021,10,9))
        self.dateLabel.setText("Date Of Birth:")
        self.dateLabel.setObjectName("GENLAB")
        self.date.setObjectName("GENBOX")
        self.grid.addWidget(self.dateLabel,2,2)
        self.grid.addWidget(self.date,2,3)

        self.nameLabel=QLabel()
        self.nameLine=QLineEdit()
        self.nameLabel.setText("First Name:")
        self.nameLabel.setObjectName("GENLAB")
        self.nameLine.setPlaceholderText("First name")
        self.nameLine.setObjectName("GENBOX")
        self.grid.addWidget(self.nameLabel,2,0)
        self.grid.addWidget(self.nameLine,2,1)

        self.midNameLabel=QLabel()
        self.midNameLine=QLineEdit()
        self.midNameLabel.setText("Middle Name:")
        self.midNameLabel.setObjectName("GENLAB")
        self.midNameLine.setPlaceholderText("Middle name")
        self.midNameLine.setObjectName("GENBOX")
        self.grid.addWidget(self.midNameLabel,4,0)
        self.grid.addWidget(self.midNameLine,4,1)

        self.lastNameLabel=QLabel()
        self.lastNameLine=QLineEdit()
        self.lastNameLabel.setText("Last Name:")
        self.lastNameLabel.setObjectName("GENLAB")
        self.lastNameLine.setPlaceholderText("Last name")
        self.lastNameLine.setObjectName("GENBOX")
        self.grid.addWidget(self.lastNameLabel,6,0)
        self.grid.addWidget(self.lastNameLine,6,1)
        
        self.contactLabel=QLabel()
        self.contactLine=QLineEdit()
        self.contactLabel.setText("Contact No:")
        self.contactLabel.setObjectName("GENLAB")
        self.contactLine.setPlaceholderText("Contact No")
        self.contactLine.setObjectName("GENBOX")
        self.grid.addWidget(self.contactLabel,8,0)
        self.grid.addWidget(self.contactLine,8,1)

        self.eContactLabel=QLabel()
        self.eContactLine=QLineEdit()
        self.eContactLabel.setObjectName("GENLAB")
        self.eContactLine.setPlaceholderText("Emergency Contact")
        self.eContactLine.setObjectName("GENBOX")
        self.eContactLabel.setText("Emergency Contact: ")
        self.grid.addWidget(self.eContactLabel,10,0)
        self.grid.addWidget(self.eContactLine,10,1)
        
        self.eContactRLabel=QLabel()
        self.eContactRLine=QLineEdit()
        self.eContactRLabel.setText("Relation To Emg Contact: ")
        self.eContactRLabel.setObjectName("GENLAB")
        self.eContactRLine.setPlaceholderText("Relation To Emergency Contact")
        self.eContactRLine.setObjectName("GENBOX")
        self.grid.addWidget(self.eContactRLabel,12,0)
        self.grid.addWidget(self.eContactRLine,12,1)

        self.addressLabel=QLabel()
        self.addressText=QTextEdit()
        self.addressText.setFixedSize(300,50)
        self.addressLabel.setText("Address: ")
        self.addressText.setPlaceholderText("Address")
        self.addressLabel.setObjectName("GENLAB")
        self.addressText.setObjectName("ADDBOX")
        self.grid.addWidget(self.addressLabel,4,2)
        self.grid.addWidget(self.addressText,4,3)
        
        self.Experience=QLabel()
        self.ExperienceMenu=QComboBox()
        self.ExperienceMenu.addItems(["0-1 years","2-3 years","4-5 years","5-10 years","10+ years"])
        self.Experience.setText("Experience:")
        self.Experience.setObjectName("GENLAB")
        self.ExperienceMenu.setObjectName("GENBOX")
        self.grid.addWidget(self.Experience,6,2)
        self.grid.addWidget(self.ExperienceMenu,6,3)
        
        
        self.WorkingLabel=QLabel()
        self.WorkingMenu=QComboBox()
        self.WorkingLabel.setText("Working Hours:")
        self.WorkingMenu.addItems(["3-5 hours","5-10 hours","10-15 hours","15-18 hours","18+ hours"])
        self.WorkingLabel.setObjectName("GENLAB")
        self.WorkingMenu.setObjectName("GENBOX")
        self.grid.addWidget(self.WorkingLabel,8,2)
        self.grid.addWidget(self.WorkingMenu,8,3)

        self.SalaryLabel=QLabel()
        self.SalaryLine=QLineEdit()
        self.SalaryLabel.setText("Salary:")
        self.SalaryLabel.setObjectName("GENLAB")
        self.SalaryLine.setPlaceholderText("Salary")
        self.SalaryLine.setObjectName("GENBOX")
        self.grid.addWidget(self.SalaryLabel,10,2)
        self.grid.addWidget(self.SalaryLine,10,3)
 
        self.JoinDateLabel=QLabel()
        self.Jdate = QDateEdit()
        self.Jdate.setDate(QDate(2021,10,9))
        self.JoinDateLabel.setText("Date of Joining:")
        self.JoinDateLabel.setObjectName("GENLAB")
        self.Jdate.setObjectName("GENBOX")
        self.grid.addWidget(self.JoinDateLabel,12,2)
        self.grid.addWidget(self.Jdate,12,3)

        self.Profession=QLabel()
        self.ProfessionMenu=QComboBox()
        self.ProfessionMenu.addItems(["Doctor","Receptionist","Nurse","Cleaner","Compounder","Hospital pharmacists","Medical Student","Accountant"])
        self.Profession.setText("Profession:")
        self.Profession.setObjectName("GENLAB")
        self.ProfessionMenu.setObjectName("GENBOX")
        self.grid.addWidget(self.Profession,0,2)
        self.grid.addWidget(self.ProfessionMenu,0,3)
        
        
        self.addButton=QPushButton()
        self.addButton.setText("ADD")
        self.addButton.setObjectName("Addbtn")
        self.addButton.clicked.connect(self.addRecord)
        self.updateButton=QPushButton()
        self.updateButton.setText("UPDATE")
        self.updateButton.setObjectName("Addbtn")
        self.updateButton.clicked.connect(self.updateRecord)
        self.deleteButton=QPushButton()
        self.deleteButton.setText("DELETE")
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.deleteButton.setObjectName("Addbtn")
       
        self.resetButton=QPushButton()
        self.resetButton.setText("RESET")
        self.resetButton.setObjectName("Addbtn")
        self.resetButton.clicked.connect(self.reset)
        self.grid.addWidget(self.addButton,14,0)
        self.grid.addWidget(self.updateButton,14,1)
        self.grid.addWidget(self.deleteButton,14,2)
        self.grid.addWidget(self.resetButton,14,3)

        self.infoFrame.setLayout(self.grid)
        self.recordFrame=QtWidgets.QFrame(self)
        self.recordFrame.setFrameShape(QFrame.StyledPanel)
        self.recordFrame.setFixedSize(1450,300)

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10) 
        self.tableWidget.setColumnCount(12)
        self.item=QTableWidgetItem("Employee ID")
        self.tableWidget.setHorizontalHeaderItem(0, self.item)
        self.item=QTableWidgetItem("Name")
        self.tableWidget.setHorizontalHeaderItem(1, self.item)
        self.item=QTableWidgetItem("Middle Name")
        self.tableWidget.setHorizontalHeaderItem(2, self.item)
        self.item=QTableWidgetItem("Last Name")
        self.tableWidget.setHorizontalHeaderItem(3, self.item)
        self.item=QTableWidgetItem("Contact No")
        self.tableWidget.setHorizontalHeaderItem(4, self.item)
        self.item=QTableWidgetItem("Emergency Contact No")
        self.tableWidget.setHorizontalHeaderItem(5, self.item)
        self.item=QTableWidgetItem("Relation To Emergency Contact No")
        self.tableWidget.setHorizontalHeaderItem(6, self.item)
        self.item=QTableWidgetItem("Address")
        self.tableWidget.setHorizontalHeaderItem(7, self.item)
        self.item=QTableWidgetItem("Experience")
        self.tableWidget.setHorizontalHeaderItem(8, self.item)
        self.item=QTableWidgetItem("Salary")
        self.tableWidget.setHorizontalHeaderItem(9, self.item)
        self.item=QTableWidgetItem("Joing Date")
        self.tableWidget.setHorizontalHeaderItem(10, self.item)
        self.item=QTableWidgetItem("Hours")
        self.tableWidget.setHorizontalHeaderItem(11, self.item)
        self.item=QTableWidgetItem("Profession")
        self.tableWidget.setHorizontalHeaderItem(12, self.item)
        self.vbox2.addWidget(self.tableWidget)
        self.recordFrame.setLayout(self.vbox2)
        self.vbox.addWidget(self.recordFrame)
        
        self.setLayout(self.vbox)

class Patient(QWidget):
    def __init__(self):
        super(Patient,self).__init__()
        self.setGeometry(200,30,1480,1000)
        self.setFixedSize(1480,1000)
        self.setWindowTitle("Login-Admin Mode")
        style = """
            QWidget
            {
                 background-color: #5FB3CE;   
            }
            QFrame
            {
                background: white;
                border-radius: 20px; 
                font-family: Arial, sans-serif;
            }
            QWidget#PM
            {
               font-size: 35px;
               font-weight: 2500;
               color: #5FB3CE;
            }
            QFrame#TitleFrame
            {
                 background: white;
            }
            QWidget#PATID
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
            }
            QLabel#PATLAB
            {
                font-size: 15px;
                font-family: Arial, sans-serif;
                color: black;
                font-weight: 250;
            }
            QWidget#FIRSTBOX
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
            }
            QLabel#FIRLAB
            {
                font-size: 15px;
                font-family: Arial, sans-serif;
                color: black;
                font-weight: 250;
            }
            QWidget#MIDBOX
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
            }
            QLabel#MIDLAB
            {
                font-size: 15px;
                font-family: Arial, sans-serif;
                color: black;
                font-weight: 250;
            }
            QWidget#ADDBOX
            {
                background: white;
                border-bottom: 2px solid #5FB3CE;
                border-top: transparent;
                font-size: 15px;
                border-radius: 0px;
            }
           QPushButton#Addbtn
            {
                background: #5FB3CE;
                border: 2px solid #5FB3CE;
                border-radius: 10px;
                padding: 10px;
                color: white;
                font-size: 15px;
                font-weight: 1000; 
                margin: 2px;
            }
             QPushButton#Addbtn:hover
            {
                Background: white;
                color: #5FB3CE;
             }
            QPushButton#Exitbtn
            {
                background: transparent;
                border: transparent;
                color: #5FB3CE;
                font-size: 20px;
                font-weight: 500;
                padding:5px;
            }
            QPushButton#Exitbtn:hover
            {
                border-bottom: 3px solid #5FB3CE;
            }
            QTextEdit#pres
            {
                padding: 15px;
                background:rgb(245,245,245);
                font-size:20px;
                font-weight:500;
                font-family: Arial, sans-serif;
            }
    """
        self.setStyleSheet(style)
        self.myUI()
    def updateRecord(self):
        count=self.validateInputs()
        if count==11:
            self.patientID=self.patientIDLine.text()
            self.firstName=self.nameLine.text()
            self.midName=self.midNameLine.text()
            self.lastName=self.lastNameLine.text()
            self.contact=self.contactLine.text()
            self.eContact=self.eContactLine.text()
            self.h=self.heightLine.text()
            self.weight=self.weightLine.text()
            self.address=self.addressText.toPlainText()
            self.disease = self.diseaseLine.text()
            self.bg=str(self.bloodGroupMenu.currentText())
            self.doctor=str(self.doctorMenu.currentText())

            conn=Database.connect()
            self.cur=conn.cursor()
            self.query="UPDATE patient SET name=%s,mName=%s,lName=%s,contact_no=%s,eContact=%s,address=%s,bg=%s,height=%s,weight=%s,disease=%s,doctor=%s WHERE patient_id=%s"
            values=(self.firstName,self.midName,self.lastName,self.contact,self.eContact,self.address,self.bg,self.h,self.weight,self.disease,self.doctor,self.patientID)
            self.cur.execute(self.query, values)
            conn.commit()
            self.addText()
            self.loadDB()
    def reset(self):
        self.patientIDLine.clear()
        self.nameLine.clear()
        self.midNameLine.clear()
        self.lastNameLine.clear()
        self.contactLine.clear()
        self.eContactLine.clear()
        self.heightLine.clear()
        self.weightLine.clear()
        self.addressText.clear()
        self.diseaseLine.clear()
        self.eContactRLine.clear()
        self.doctorMenu.clear()
        self.deleteLayout(self.textFrame.layout())
    
    def deleteLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.deleteLayout(item.layout())
            sip.delete(layout)

    def deleteRecord(self):
        self.conn=Database.connect()
        cur = self.conn.cursor()
        self.patientID = self.patientIDLine.text()
        self.query = "DELETE FROM patient WHERE patient_id = %s"
        values = (self.patientID,)
        cur.execute(self.query, values)
        self.conn.commit()
        self.loadDB()    
    def loadDB(self):
        self.conn=Database.connect()
        self.query="SELECT patient_id,name,mName,lName,contact_no,eContact,address,bg,height,weight,disease,doctor FROM patient"
        self.cur=self.conn.cursor()
        self.cur.execute(self.query)
        record=self.cur.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(record):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        self.cur.close()
    def addText(self):
            self.hbox=QHBoxLayout()
            self.info=QTextEdit(self.textFrame)
            self.info.setObjectName("pres")
            self.info.insertPlainText(f"Patient ID: {self.patientIDLine.text()}\n")
            self.info.insertPlainText(f"Name: {self.nameLine.text()}\n")
            self.info.insertPlainText(f"Middle Name: {self.midNameLine.text()}\n")
            self.info.insertPlainText(f"Last Name: {self.lastNameLine.text()}\n")
            self.info.insertPlainText(f"Contact No: {self.contactLine.text()}\n")
            self.info.insertPlainText(f"Emergency Contact: {self.eContactLine.text()}\n")
            self.info.insertPlainText(f"Address: {self.addressText.toPlainText()}\n")
            self.info.insertPlainText(f"Blood Group: {str(self.bloodGroupMenu.currentText())}\n")
            self.info.insertPlainText(f"Height: {self.heightLine.text()}\n")
            self.info.insertPlainText(f"Weight: {self.weightLine.text()}\n")
            self.info.insertPlainText(f"Disease: {self.diseaseLine.text()}\n")
            self.info.insertPlainText(f"Doctor Assigned: {str(self.doctorMenu.currentText())}\n")
            self.hbox.addWidget(self.info)
            self.textFrame.setLayout(self.hbox)
    def addRecord(self):
        count=self.validateInputs()
        if count==11:
            self.bg=str(self.bloodGroupMenu.currentText())
            self.doctor=str(self.doctorMenu.currentText())
            self.addText()
            self.val=(self.patientID,self.firstName,self.midName,self.lastName,self.contact,self.eContact,self.address,self.bg,self.height,self.weight,self.disease,self.doctor)
            Database.createPatient(self.val)
            self.addText()
            self.loadDB()
    def errorBox(self,mess,title):
        self.msg=QtWidgets.QMessageBox()
        self.msg.setWindowTitle(title)
        self.msg.setText(mess)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec()
    
    def validateInputs(self):
        #Patient Id
        count=0
        self.patientID=self.patientIDLine.text()
        R=Regex(self.patientID)
        if self.patientID!="":
            if R.isPatientId()==True:
                count+=1
            else:
                self.errorBox("Patient Id is Invalid! Please Try Again\t\t","Input Error")
        else:
            self.errorBox("Patient Id is Blank\t","Input Error")
        #First Name
        self.firstName=self.nameLine.text()
        R=Regex(self.firstName)
        if self.firstName!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("First Name is Invalid! Please Try Again\t\t","Input Error")
        else:
            self.errorBox("First Name is Blank\t","Input Error")
        #Middle Name
        self.midName=self.midNameLine.text()
        R=Regex(self.midName)
        if self.midName!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("Middle Name is Invalid! Please Try Again\t\t","Input Error")
        else:
            self.errorBox("Middle Name is Blank\t","Input Error")
        #Last Name
        self.lastName=self.lastNameLine.text()
        R=Regex(self.lastName)
        if self.lastName!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("Last Name is Invalid! Please Try Again\t","Input Error")
        else:
            self.errorBox("Last Name is Blank\t","Input Error")
        #Contact No
        self.contact=self.contactLine.text()
        R=Regex(self.contact)
        if self.contact!="":
            if R.isContactNo()==True:
                count+=1
            else:
                self.errorBox("Contact No is Invalid! Please Try Again\t\t","Input Error")
        else:
            self.errorBox("Contact No is Blank\t","Input Error")
        #Emergency Contact
        self.eContact=self.eContactLine.text()
        R=Regex(self.eContact)
        if self.eContact!="":
            if R.isContactNo()==True:
                count+=1
            else:
                self.errorBox("Emergency Contact No is Invalid! Please Try Again\t\t","Input Error")
        else:
            self.errorBox("Emergency Contact No is Blank\t","Input Error")
        #Relation To Emergency Contact
        self.eContactRelation=self.eContactRLine.text()
        R=Regex(self.eContactRelation)
        if self.eContactRelation!="":
            if R.isAlphabet()==True:
                count+=1
            else:
                self.errorBox("Emergency Contact Relation is Invalid! Please Try Again\t\t","Input Error")
        else:
            self.errorBox("Emergency Contact Relation is Blank\t","Input Error")
        #Address
        self.address=self.addressText.toPlainText()
        R=Regex(self.address)
        if self.address!="":
            count+=1
        else:
            self.errorBox("Address is blank\t","Input Error")
        #Height
        self.height=self.heightLine.text()
        R=Regex(self.height)
        if self.height!="":
            count+=1
        else:
            self.errorBox("Height is blank\t","Input Error")
        #Weight
        self.weight=self.weightLine.text()
        R=Regex(self.weight)
        if self.weight!="":
            count+=1
        else:
            self.errorBox("Weight is blank\t","Input Error")
        #Disease
        self.disease=self.diseaseLine.text()
        R=Regex(self.disease)
        if self.disease!="":
            count+=1
        else:
            self.errorBox("Disease is blank\t","Input Error")
        return count
    def goAdmin(self):
        self.adminWindow=Admin()
        self.hide()
        self.adminWindow.show()
    def myUI(self):
        self.vbox=QVBoxLayout()
        self.vbox2=QVBoxLayout()

        self.titleFrame=QtWidgets.QFrame(self)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setObjectName("TitleFrame")
        self.titleFrame.setFixedSize(1450,100)
        self.vbox.addWidget(self.titleFrame)

        self.titleLabel=QLabel(self.titleFrame)
        self.titleLabel.setObjectName("PM")
        self.titleLabel.setText("Patient Management")
        self.titleLabel.resize(500,100)
        self.titleLabel.move(550,0)

        self.exit=QPushButton(self.titleFrame)
        self.exit.clicked.connect(self.goAdmin)
        self.exit.move(20,10)
        self.exit.setObjectName("Exitbtn")
        self.exit.setText("Exit")

        self.hbox=QHBoxLayout()
        self.infoFrame=QtWidgets.QFrame(self)
        self.infoFrame.setFrameShape(QFrame.StyledPanel)
        self.infoFrame.setFixedSize(950,550)
        self.hbox.addWidget(self.infoFrame)

        self.textFrame=QtWidgets.QFrame(self)
        self.textFrame.setFrameShape(QFrame.StyledPanel)
        self.textFrame.setObjectName("Pre")
        self.textFrame.setFixedSize(500,550)
        self.hbox.addWidget(self.textFrame)
        self.vbox.addLayout(self.hbox)

        self.grid=QGridLayout()

        self.patientIDLabel=QLabel()
        self.patientIDLine=QLineEdit()
        self.patientIDLabel.setText("Patient Id:")
        self.patientIDLabel.setObjectName("PATLAB")
        self.patientIDLine.setPlaceholderText("Patient ID")
        self.patientIDLine.setObjectName("PATID")
        self.grid.addWidget(self.patientIDLabel,0,0)
        self.grid.addWidget(self.patientIDLine,0,1)

        self.dateLabel=QLabel()
        self.date = QDateEdit()
        self.date.setDate(QDate(2021,10,9))
        self.dateLabel.setText("Date Of Birth:")
        self.dateLabel.setObjectName("MIDLAB")
        self.date.setObjectName("MIDBOX")
        self.grid.addWidget(self.dateLabel,2,2)
        self.grid.addWidget(self.date,2,3)

        self.nameLabel=QLabel()
        self.nameLine=QLineEdit()
        self.nameLabel.setText("First Name:")
        self.nameLabel.setObjectName("FIRLAB")
        self.nameLine.setPlaceholderText("First name")
        self.nameLine.setObjectName("FIRSTBOX")
        self.grid.addWidget(self.nameLabel,2,0)
        self.grid.addWidget(self.nameLine,2,1)

        self.midNameLabel=QLabel()
        self.midNameLine=QLineEdit()
        self.midNameLabel.setText("Middle Name:")
        self.midNameLabel.setObjectName("MIDLAB")
        self.midNameLine.setPlaceholderText("Middle name")
        self.midNameLine.setObjectName("MIDBOX")
        self.grid.addWidget(self.midNameLabel,4,0)
        self.grid.addWidget(self.midNameLine,4,1)

        self.lastNameLabel=QLabel()
        self.lastNameLine=QLineEdit()
        self.lastNameLabel.setText("Last Name:")
        self.lastNameLabel.setObjectName("MIDLAB")
        self.lastNameLine.setPlaceholderText("Last name")
        self.lastNameLine.setObjectName("MIDBOX")
        self.grid.addWidget(self.lastNameLabel,6,0)
        self.grid.addWidget(self.lastNameLine,6,1)
        
        self.contactLabel=QLabel()
        self.contactLine=QLineEdit()
        self.contactLabel.setText("Contact No:")
        self.contactLabel.setObjectName("MIDLAB")
        self.contactLine.setPlaceholderText("Contact No")
        self.contactLine.setObjectName("MIDBOX")
        self.grid.addWidget(self.contactLabel,8,0)
        self.grid.addWidget(self.contactLine,8,1)

        self.eContactLabel=QLabel()
        self.eContactLine=QLineEdit()
        self.eContactLabel.setObjectName("MIDLAB")
        self.eContactLine.setPlaceholderText("Emergency Contact")
        self.eContactLine.setObjectName("MIDBOX")
        self.eContactLabel.setText("Emergency Contact: ")
        self.grid.addWidget(self.eContactLabel,10,0)
        self.grid.addWidget(self.eContactLine,10,1)
        
        self.eContactRLabel=QLabel()
        self.eContactRLine=QLineEdit()
        self.eContactRLabel.setText("Relation To Emergency Contact: ")
        self.eContactRLabel.setObjectName("MIDLAB")
        self.eContactRLine.setPlaceholderText("Relation To Emergency Contact")
        self.eContactRLine.setObjectName("MIDBOX")
        self.grid.addWidget(self.eContactRLabel,0,2)
        self.grid.addWidget(self.eContactRLine,0,3)

        self.addressLabel=QLabel()
        self.addressText=QTextEdit()
        self.addressText.setFixedSize(300,50)
        self.addressLabel.setText("Address:")
        self.addressText.setPlaceholderText("Address")
        self.addressLabel.setObjectName("MIDLAB")
        self.addressText.setObjectName("ADDBOX")
        self.grid.addWidget(self.addressLabel,4,2)
        self.grid.addWidget(self.addressText,4,3)
        
        self.bloodGroup=QLabel()
        self.bloodGroupMenu=QComboBox()
        self.bloodGroupMenu.addItems(["A+","B+","AB+","O+","A-","B-","AB-","O-"])
        self.bloodGroup.setText("Blood Group:")
        self.bloodGroup.setObjectName("FIRLAB")
        self.bloodGroupMenu.setObjectName("FIRSTBOX")
        self.grid.addWidget(self.bloodGroup,6,2)
        self.grid.addWidget(self.bloodGroupMenu,6,3)
        

        self.heightLabel=QLabel()
        self.heightLine=QLineEdit()
        self.heightLabel.setText("Height(In Centimeters):")
        self.heightLabel.setObjectName("MIDLAB")
        self.heightLine.setPlaceholderText("Height(In Centimeters)")
        self.heightLine.setObjectName("MIDBOX")
        self.grid.addWidget(self.heightLabel,8,2)
        self.grid.addWidget(self.heightLine,8,3)

        
        self.weightLabel=QLabel()
        self.weightLine=QLineEdit()
        self.weightLabel.setText("Weight(In Kilograms):")
        self.weightLabel.setObjectName("MIDLAB")
        self.weightLine.setPlaceholderText("Weight(In Kilograms)")
        self.weightLine.setObjectName("MIDBOX")
        self.grid.addWidget(self.weightLabel,10,2)
        self.grid.addWidget(self.weightLine)

        self.diseaseLabel=QLabel()
        self.diseaseLine=QLineEdit()
        self.diseaseLabel.setText("Disease:")
        self.diseaseLabel.setObjectName("MIDLAB")
        self.diseaseLine.setPlaceholderText("Disease")
        self.diseaseLine.setObjectName("MIDBOX")
        self.grid.addWidget(self.diseaseLabel,12,2)
        self.grid.addWidget(self.diseaseLine,12,3)

        self.doctor=QLabel()
        self.doctorMenu=QComboBox()
        self.doctorMenu.addItems(["Dr Ahmed","Dr Allen","Dr Shah","Dr Nene","Dr Kapadia","Dr D'Costa","Dr Kothari","Dr Ramesh","Dr Neville","Dr Sanghvi"])
        self.doctor.setText("Doctor Assigned:")
        self.doctor.setObjectName("MIDLAB")
        self.doctorMenu.setObjectName("MIDBOX")
        self.grid.addWidget(self.doctor,12,0)
        self.grid.addWidget(self.doctorMenu,12,1)
        
        
        self.addButton=QPushButton()
        self.addButton.setText("ADD")
        self.addButton.setObjectName("Addbtn")
        self.addButton.clicked.connect(self.addRecord)

        self.updateButton=QPushButton()
        self.updateButton.setText("UPDATE")
        self.updateButton.setObjectName("Addbtn")
        self.updateButton.clicked.connect(self.updateRecord)

        self.deleteButton=QPushButton()
        self.deleteButton.setText("DELETE")
        self.deleteButton.clicked.connect(self.deleteRecord)
        self.deleteButton.setObjectName("Addbtn")

        self.resetButton=QPushButton()
        self.resetButton.setText("RESET")
        self.resetButton.clicked.connect(self.reset)
        self.resetButton.setObjectName("Addbtn")

        self.grid.addWidget(self.addButton,14,0)
        self.grid.addWidget(self.updateButton,14,1)
        self.grid.addWidget(self.deleteButton,14,2)
        self.grid.addWidget(self.resetButton,14,3)

        self.infoFrame.setLayout(self.grid)
        self.recordFrame=QtWidgets.QFrame(self)
        self.recordFrame.setFrameShape(QFrame.StyledPanel)
        self.recordFrame.setFixedSize(1450,300)
        
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(10) 
        self.tableWidget.setColumnCount(12)
        self.item=QTableWidgetItem("Patient ID")
        self.tableWidget.setHorizontalHeaderItem(0, self.item)
        self.item=QTableWidgetItem("Name")
        self.tableWidget.setHorizontalHeaderItem(1, self.item)
        self.item=QTableWidgetItem("Middle Name")
        self.tableWidget.setHorizontalHeaderItem(2, self.item)
        self.item=QTableWidgetItem("Last Name")
        self.tableWidget.setHorizontalHeaderItem(3, self.item)
        self.item=QTableWidgetItem("Contact No")
        self.tableWidget.setHorizontalHeaderItem(4, self.item)
        self.item=QTableWidgetItem("Emergency Contact No")
        self.tableWidget.setHorizontalHeaderItem(5, self.item)
        self.item=QTableWidgetItem("Address")
        self.tableWidget.setHorizontalHeaderItem(6, self.item)
        self.item=QTableWidgetItem("Blood Group")
        self.tableWidget.setHorizontalHeaderItem(7, self.item)
        self.item=QTableWidgetItem("Height")
        self.tableWidget.setHorizontalHeaderItem(8, self.item)
        self.item=QTableWidgetItem("Weight")
        self.tableWidget.setHorizontalHeaderItem(9, self.item)
        self.item=QTableWidgetItem("Disease")
        self.tableWidget.setHorizontalHeaderItem(10, self.item)
        self.item=QTableWidgetItem("Doctor Assigned")
        self.tableWidget.setHorizontalHeaderItem(11, self.item)
        self.vbox2.addWidget(self.tableWidget)
        self.recordFrame.setLayout(self.vbox2)

        self.vbox.addWidget(self.recordFrame)
        self.setLayout(self.vbox)

class Admin(QWidget):
    def __init__(self):
        super(Admin,self).__init__()
        self.setGeometry(200,30,1480,1000)
        self.setWindowTitle("Login-Admin Mode")
        self.setFixedSize(1480,1000)
        self.myUI()
        self.style= """
            QWidget
            {
                 background-color: #5FB3CE;   
            }
            QFrame
            {
                background: white;
                border-radius: 10px; 
                font-family: Arial, sans-serif;
            }
            QWidget#AdminLabel
            {
                font-size: 40px;
                font-family: Arial, sans-serif;
                font-weight: 2000;
                color: #5FB3CE;
            }
            QWidget#Patient
            {
                background-color: #5FB3CE;
                border-radius: 15px;
                color: white;
                font-size: 22px;
                font-family: Arial, sans-serif;
                 font-weight: 500;
            }
            QWidget#Medicine
            {
                background-color: #5FB3CE;
                border-radius: 15px;
                color: white;
                font-size: 22px;
                font-family: Arial, sans-serif;
                 font-weight: 500;
            }
            QWidget#Employee
            {
                background-color:#5FB3CE;
                border-radius: 15px;
                color: white;
                font-size: 22px;
                font-family: Arial, sans-serif;
                font-weight: 500;
            }
            QWidget#Abt
            {
                background-color:#5FB3CE; 
                border-radius: 15px;
                color: white;
                font-size: 22px;
                font-family: Arial, sans-serif;
                font-weight: 500;
            }
            QWidget#logout
            {
                background-color:white;
                color:#5FB3CE;
                font-family: Arial, sans-serif;
                font-size: 23px;
                font-weight: 500;
                border: none;
            }
            QWidget#Patient:hover
            {
                background: white;
                color: #5FB3CE;
                border-radius: 0px;
                border-bottom: 3px solid #5FB3CE;
                border-top: transparent;
                border-left: transparent;
                border-right: transparent;
            }
            QWidget#Medicine:hover
            {
                background: white;
                color: #5FB3CE;
                border-radius: 0px;
                border-bottom: 3px solid #5FB3CE;
                border-top: transparent;
                border-left: transparent;
                border-right: transparent;
            }
            QWidget#Employee:hover
            {
                background: white;
                color: #5FB3CE;
                border-radius: 0px;
                border-bottom: 3px solid #5FB3CE;
                border-top: transparent;
                border-left: transparent;
                border-right: transparent;
            }
            QWidget#Abt:hover
            {
                background: white;
                color: #5FB3CE;
                border-radius: 0px;
                border-bottom: 3px solid #5FB3CE;
                border-top: transparent;
                border-left: transparent;
                border-right: transparent;
            }
            QWidget#logout:hover
            {
                border-bottom: 2px solid #5FB3CE;
            }
            """
        self.setStyleSheet(self.style)

    def logOut(self):
        self.loginWin=MyWindow()
        self.hide()
        self.loginWin.show()
    def openAboutUs(self):
        self.aboutUs=AboutUs()
        self.hide()
        self.aboutUs.show()
    def openMedicineWindow(self):
        self.medicine=Medicine()
        self.hide()
        self.medicine.show()
    def openEmployeeWindow(self):
        self.EmployeeWindow=Employee()
        self.hide
        self.EmployeeWindow.show()
    def openPatientWindow(self):
        self.patientWin=Patient()
        self.hide()
        self.patientWin.show()
    def myUI(self):
        hbox=QHBoxLayout()
        adminFrame=QtWidgets.QFrame(self)
        adminFrame.setFrameShape(QFrame.StyledPanel)  
        adminFrame.setFixedSize(700,800)
        
        #adminLabel
        adminLabel=QtWidgets.QLabel(adminFrame)
        adminLabel.setText("ADMIN MODE")
        adminLabel.setObjectName("AdminLabel")
        adminLabel.resize(280,60)
        adminLabel.move(220,80)
        
        #patient
        patientMan=QPushButton(adminFrame)
        patientMan.setText("Patient Management")
        patientMan.setObjectName("Patient")
        patientMan.resize(550,60)
        patientMan.move(80,200)
        patientMan.clicked.connect(self.openPatientWindow)

        #Employee
        employeeMan=QPushButton(adminFrame)
        employeeMan.setText("Employee Management")
        employeeMan.setObjectName("Employee")
        employeeMan.resize(550,60)
        employeeMan.move(80,300)
        employeeMan.clicked.connect(self.openEmployeeWindow)
        
        #medicine
        medicineMan=QPushButton(adminFrame)
        medicineMan.setText("Medicine Management")
        medicineMan.setObjectName("Medicine")
        medicineMan.clicked.connect(self.openMedicineWindow)
        medicineMan.resize(550,60)
        medicineMan.move(80,400)
        
        #about us
        aboutUs=QPushButton(adminFrame)
        aboutUs.setText("About Us")
        aboutUs.setObjectName("Abt")
        aboutUs.clicked.connect(self.openAboutUs)
        aboutUs.resize(550,60)
        aboutUs.move(80,500)

        #logout
        logout=QPushButton(adminFrame)
        logout.setText("Logout")
        logout.setObjectName("logout")
        logout.clicked.connect(self.logOut)
        logout.resize(85,40)
        logout.move(20,20)

        hbox.addWidget(adminFrame)
        self.setLayout(hbox)
class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setGeometry(200,30,1480,1000)
        self.setFixedSize(1480,1000)
        self.setWindowTitle("Login")
        self.myUI()
        Database.createDatabase()
    def errorBox(self,mess,title):
        self.msg=QtWidgets.QMessageBox()
        self.msg.setWindowTitle(title)
        self.msg.setText(mess)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec()

    def validateAdmin(self):
        self.username=self.nameLine.text()
        self.password=self.passLine.text()
        result=Database.validateAdmin(self.username,self.password)
        if result<=0:
            self.errorBox("Your Credentials Are Invalid! Please try again\t\t","Login Error")
        else:
            self.adminWindow=Admin()
            self.hide()
            self.adminWindow.show()
    def myUI(self):
        self.hbox=QHBoxLayout()
        self.loginFrame=QtWidgets.QFrame(self)
        self.loginFrame.setFrameShape(QFrame.StyledPanel)
        self.loginFrame.setFixedSize(560,500)
         
        #login 
        self.loginLabel=QtWidgets.QLabel(self.loginFrame)
        self.loginLabel.setText("Login")
        self.loginLabel.setObjectName("loginLabel")
        self.loginLabel.resize(180,60)
        self.loginLabel.move(220,20)
        #Username  
        self.nameLabel=QtWidgets.QLabel(self.loginFrame)
        self.nameLabel.setText("Username ")
        self.nameLabel.setObjectName("Name")
        self.nameLabel.resize(112,40)
        self.nameLabel.move(20,100)
        
        #Username box
        self.nameLine=QtWidgets.QLineEdit(self.loginFrame)
        self.nameLine.setObjectName("Namebox")
        self.nameLine.resize(500,32)
        self.nameLine.move(20,140)
        
        #password
        self.passLabel=QtWidgets.QLabel(self.loginFrame)
        self.passLabel.setObjectName("Pass")
        self.passLabel.setText("Password")
        self.passLabel.resize(112,40)
        self.passLabel.move(20,230)
        
        #password box
        self.passLine=QtWidgets.QLineEdit(self.loginFrame) 
        self.passLine.setEchoMode(QLineEdit.Password)
        self.passLine.setObjectName("Passbox")
        self.passLine.resize(500,32)
        self.passLine.move(20,270)
        
        #Login button
        self.submitButton=QtWidgets.QPushButton(self.loginFrame)
        self.submitButton.setObjectName("Login_btn")
        self.submitButton.resize(500, 50)
        self.submitButton.move(25,400)
        self.submitButton.setText("Login")
        self.submitButton.clicked.connect(self.validateAdmin)
        self.hbox.addWidget(self.loginFrame)
        self.setLayout(self.hbox)

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    style= """
            QWidget
            {
                background-color: #5FB3CE;   
            }
            QMessageBox
            {
                background-color: white;
                font-weight: 500;
                font-size: 15px;
            }
            QFrame
            {
                background: white;
                border-radius: 10px; 
                font-family: Arial, sans-serif;
            }
            QWidget#loginLabel
            {
                font-size: 40px;
                font-family: Arial, sans-serif;
                font-weight: 2000;
            }
            QWidget#Name
            {
                font-size: 20px;
                font-family: Arial, sans-serif;
                 font-weight: 450;
                color: rgb(91,92,97);
            }
            QWidget#Namebox
            { 
                 border: 2px solid black;
                 border-top: transparent;
                 border-left: transparent; border-right: transparent;
                 background: white;
                 font-size: 20px;  
            }
            QWidget#Pass
            {
                font-size: 20px;
                font-family: Arial, sans-serif;
                 font-weight: 450;
                color: rgb(91,92,97);
            }
            QWidget#Passbox
            { 
                 border: 2px solid black;
                 border-top: transparent;
                 border-left: transparent; border-right: transparent;
                 background: white;
                 font-size: 20px;  
            }
            QWidget#Login_btn
            {
                border-radius: 15px;
                font-size: 25px;
                color: white;
                font-weight: 500; 
                background-color: #5FB3CE;
            }
            QWidget#Login_btn:hover
            {
                color:#5FB3CE;
                background-color: white;
                border: 2px solid #5FB3CE;
            }
        """
    mainWin=MyWindow()
    mainWin.show()
    app.setStyleSheet(style)
    sys.exit(app.exec_())
