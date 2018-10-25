import sys
import csv
import random
import string
from PyQt4 import QtCore, QtGui
picked_num=[]
try:
    with open('dic_file.csv', 'rb') as csv_file:
        reader = csv.reader(csv_file)
        dic_etin = dict(reader)
except:#if file does not exist, it creates a new file
    dic_etin={}
    with open('dic_file.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in dic_etin.items():
            writer.writerow([key, value])   
def code_gen():
    picked=random.randrange(1000,9999)
    return picked

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("Code Generator"))
        MainWindow.resize(558, 497)
 
        #self.lbl = QtGui.QLabel(self)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.LG = QtGui.QLineEdit(self.centralwidget)
        self.LG.setGeometry(QtCore.QRect(190, 58, 361, 27))
        self.LG.setObjectName(_fromUtf8("LG"))        
        
        self.WD = QtGui.QLineEdit(self.centralwidget)
        self.WD.setGeometry(QtCore.QRect(190, 110, 361, 27))
        self.WD.setObjectName(_fromUtf8("WD"))
        

        
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 161, 20))
        self.label.setObjectName(_fromUtf8("label"))
        #self.label.setStyleSheet("background-color: gray;")
        
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 113, 51, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 170, 111, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        #self.label_3.setStyleSheet("background-color: black;")
        
        
        self.info_checker = QtGui.QLabel(self.centralwidget)
        self.info_checker.setGeometry(QtCore.QRect(430, 320, 121, 17))
        self.info_checker.setObjectName(_fromUtf8("info_checker"))
        
        
        self.show_info = QtGui.QPushButton(self.centralwidget)
        self.show_info.setGeometry(QtCore.QRect(430, 390, 98, 27))
        self.show_info.setObjectName(_fromUtf8("show_info"))
        self.show_info.clicked.connect(self.buttonClickedInfo)
        
        self.info_number = QtGui.QLineEdit(self.centralwidget)
        self.info_number.setGeometry(QtCore.QRect(420, 340, 113, 27))
        self.info_number.setObjectName(_fromUtf8("info_number"))        
        
        self.lcdNumber = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(230, 300, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.lcdNumber.Dec
        self.lcdNumber.setStyleSheet("background-color: black;")
        #self.lcdNumber.display(gen_code)
        
        self.PU = QtGui.QLineEdit(self.centralwidget)
        self.PU.setGeometry(QtCore.QRect(190, 168, 361, 27))
        self.PU.setObjectName(_fromUtf8("lineEdit_2"))
        
#        global sometext
#        sometext = self.lineEdit_2.text 
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 240, 151, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.pushButton.clicked.connect(self.buttonClicked)
        
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 300, 51, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 558, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuEXIT = QtGui.QMenu(self.menubar)
        self.menuEXIT.setObjectName(_fromUtf8("menuEXIT"))
        
        MainWindow.setMenuBar(self.menubar)
        
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        
        MainWindow.setStatusBar(self.statusBar)
        
        self.actionQUIT = QtGui.QAction(MainWindow)
        self.actionQUIT.setObjectName(_fromUtf8("actionQUIT"))
        
        self.menuEXIT.addAction(self.actionQUIT)
        self.menubar.addAction(self.menuEXIT.menuAction())
        self.actionQUIT.triggered.connect(exit)

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("Code Generator", "Code Generator", None))
        self.label.setText(_translate("Code Generator", "LOCAL GOVERNMENT", None))
        self.label_2.setText(_translate("Code Generator", "WARD", None))
        self.label_3.setText(_translate("Code Generator", "POLLING UNIT", None))
        self.pushButton.setText(_translate("Code Generator", "GENERATE CODE", None))
        self.label_4.setText(_translate("Code Generator", "CODE", None))
        self.menuEXIT.setTitle(_translate("Code Generator", "EXIT", None))
        self.toolBar.setWindowTitle(_translate("Code Generator", "toolBar", None))
        self.actionQUIT.setText(_translate("Code Generator", "QUIT", None))
        self.info_checker.setText(_translate("Code Generator", "INFO CHECKER", None))
        self.show_info.setText(_translate("Code Generator", "SHOW INFO", None))

    def buttonClicked(self, sometext):
        lg_e1=str(self.LG.text())
        wd_e2=str(self.WD.text())
        pu_e3=str(self.PU.text())
        if len(lg_e1)>0 and len(wd_e2)>0 and len(pu_e3)>0:
            dic_comp=lg_e1+","+wd_e2+","+pu_e3
            if dic_comp in dic_etin:
                self.lcdNumber.display(dic_etin[dic_comp])
            else:              
                while True:
                    code_gen_res=code_gen()
                    if code_gen_res in picked_num:
                        continue
                    else:
                        break
                self.lcdNumber.display(code_gen_res)
                code_gen_res=str(code_gen_res)
                picked_num.append(code_gen_res)
        
                dic_etin[dic_comp] = code_gen_res

                with open('dic_file.csv', 'wb') as csv_file:
                    writer = csv.writer(csv_file)
                    for key, value in dic_etin.items():
                        writer.writerow([key, value])            
                    
                file = open("Register.txt","a+")                    
                    
                file.write("LG: "+lg_e1+"\n") 
                file.write("WR: "+wd_e2+"\n")                 
                file.write("PU: "+pu_e3+"\n")                
                file.write("CODE: "+code_gen_res+"\n")
                file.write("============================================================\n")
             
                file.close()
        else:
            1+1
    def buttonClickedInfo(self, sometext):
        try:
            info_num=self.info_number.text()
            for keys in dic_etin:
                key_value=dic_etin[keys]
                if key_value==info_num:
                    info_num_detail=keys
                    info_num_detail=info_num_detail.split(',')
                    self.LG.setText(info_num_detail[0])
                    self.WD.setText(info_num_detail[1])
                    self.PU.setText(info_num_detail[2])
                    self.lcdNumber.display(key_value)
                    #print(self.LG.setText(info_num_detail[0]))
        except:
            1+1


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet("background-color: darkgray;")
    app.setWindowIcon(QtGui.QIcon('g.png'))
    sys.exit(app.exec_())

