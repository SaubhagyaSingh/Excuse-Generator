from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PyQt5.uic import loadUi
import sys
import random

excuse=""
replacementlist=[]

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui", self)
        self.b1.clicked.connect(self.login)
    
    def show_details(self):
        widget.setCurrentIndex(1)
        
        
    def login(self):
        global excuse
        excuse=self.list.currentText()
        self.show_details()
        

class Details(QDialog):
    def __init__(self):
        super(Details,self).__init__()
        loadUi("requirements.ui",self)
        self.gen.clicked.connect(self.getdata)

    def getdata(self):
        
        global replacementlist
        
        your_name=self.i1.text()
        your_address=self.i2.text()
        your_city=self.i3.text()
        email=self.i4.text()
        ph=self.i5.text()
        date=self.i6.text()
        college=self.i7.text()
        receiver =self.i8.text()
        col_address=self.i11.text()
        col_city=self.i12.text()
        start_date=self.i9.text()
        end_date=self.i10.text()

        replacementlist.append(your_name)
        replacementlist.append(your_address)
        replacementlist.append(your_city)
        replacementlist.append(email)
        replacementlist.append(ph)
        replacementlist.append(date)
        replacementlist.append(college)
        replacementlist.append(receiver)
        replacementlist.append(col_address)
        replacementlist.append(col_city)
        replacementlist.append(start_date)
        replacementlist.append(end_date)

        self.generate()
    
    def search_replace(self,file_name,replacelist):
        
        with open(file_name, 'r') as file:
            content = file.read()
        
        searchlist=["Your Name","Your Address","yCity","Email Address","Phone Number","Date","College Head's Name","College Name","Address","City","start_date","end_date"]
        
        for i in range(0,12):
            content=content.replace(searchlist[i],replacelist[i])
        
        with open(file_name, 'w') as file:
            file.write(content)
    
        
    def generate(self):
        global excuse
        global replacementlist
        print(excuse)
        file_name=""
        if excuse=="Cultural Event":
            file_name="excuses/culturalevent.txt"
            
        elif excuse=="Financial":            
            file_name="excuses/financial.txt"

        elif excuse=="Medical":
            file_name="excuses/medical.txt"
                
        elif excuse=="Mental Health":
            file_name="excuses/mentalhealth.txt"
        
        elif excuse=="Death of a relative":
            file_name="excuses/relative.txt"
        
        elif excuse=="Sports":
            file_name="excuses/sports.txt"

        elif excuse=="Weather":
            file_name="excuses/weather.txt"
        
        
        with open(f"{file_name}") as f:
            x=random.randint(0,500)
            with open(f"newfile{x}.txt", "w") as f1:
                for line in f:
                    f1.write(line)
            myfile=f"newfile{x}.txt"
        
        self.search_replace(myfile,replacementlist)


        




app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
ls = LoginScreen()
req=Details()
#widget.addWidget()
widget.addWidget(ls)
widget.addWidget(req)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()

app.exec_()