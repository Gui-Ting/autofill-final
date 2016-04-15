
# coding: utf-8

# In[4]:


import re
import sys
from robobrowser import RoboBrowser
import design
from PyQt4 import QtGui

class AutoFill(QtGui.QDialog, design.Ui_Dialog):
    def __init__(self, parent=None):
        super(AutoFill, self).__init__(parent)
        self.setupUi(self)
        self.lineEdit_3.setEchoMode(self.lineEdit_3.Password)
        self.pushButton.clicked.connect(self.pushedbutton)
        mess = QtGui.QMessageBox()
    
    def pushedbutton(self,b):
        account = self.lineEdit.text()
        pasw = self.lineEdit_3.text()
        #use robobrowser module to manipulate web page 
        browser = RoboBrowser(history = True)
        browser.open('http://web1.cmu.edu.tw/stdinfo/login.asp')
        form1 = browser.get_form(id = 'form1')
        form1['f_id'].value = account
        form1['f_pwd'].value = pasw
        browser.submit_form(form1)
        if browser.state.url == "http://web1.cmu.edu.tw/stdinfo/loginerr.asp":
            self.lineEdit_2.setText('帳號密碼錯了?')
        else:
            link_one = browser.get_link(text = re.compile('.意見調查'))
            browser.follow_link(link_one)
            list = []
            for l in browser.get_links(text = re.compile('.填寫.')): 
                list.append(l)
            list.pop(0)
            for li in list:
                browser.follow_link(li)
                form2 = browser.get_form(id = 'thisform')
                form2['Cos_Q1'].value = '1'
                browser.submit_form(form2)
            self.lineEdit_2.setText('Done!')

def main():
    app = QtGui.QApplication(sys.argv)
    form = AutoFill()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()

