# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Practice.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QTimer
import random, math
from time import time

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(170, 310, 50, 14))
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.label.setObjectName(_fromUtf8("label"))
        #self.q = 0
        #self.finish_para = 0

        #Add progress bar
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(680, 0, 121, 23))
        self.progressBar.setMinimumSize(QtCore.QSize(118, 23))
        self.progressBar.setStyleSheet(_fromUtf8("color: rgb(0, 0, 50);"))
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(5)

        #Add text box
        self.timeToStart = QtGui.QTextEdit(Form)
        self.timeToStart.setGeometry(QtCore.QRect(80, 40, 111, 31))
        self.timeToStart.setObjectName(_fromUtf8("timeToStart"))
        self.timeToStart.setReadOnly(True)
        self.timeToStart.setText(" Start in ")

        # Add show text paragraph
        self.showPara = QtGui.QTextEdit(Form)
        self.showPara.setGeometry(QtCore.QRect(170, 130, 581, 161))
        self.showPara.setObjectName(_fromUtf8("showPara"))
        self.showPara.setReadOnly(True)

        # Add Edit text box
        self.editPara = QtGui.QTextEdit(Form)
        self.editPara.setGeometry(QtCore.QRect(170, 325, 581, 161))
        self.editPara.setObjectName(_fromUtf8("editPara"))
        self.editPara.setReadOnly(True)
        #if self.finish_para == 0:
        #self.editPara.textChanged.connect(self.text_changed)

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 110, 81, 16))
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        # add Ok button
        self.finish = QtGui.QPushButton(Form)
        self.finish.setGeometry(QtCore.QRect(670, 530, 51, 27))
        self.finish.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.finish.setObjectName(_fromUtf8("finish"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Game TypeRacer", None))
        self.label.setText(_translate("Form", "Type Here", None))
        self.label_2.setText(_translate("Form", "Your Paragraph", None))
        self.finish.setText(_translate("Form", "Finish", None))
        #self.Cancel.setText(_translate("Form", "Cancel", None))

    #function to update progress bar
    def update_progressbar(self, val):
        self.progressBar.setValue(val)
        if val == 5:
            self.timeToStart.setText("Go..Game will start ")
            self.timeToStart.setStyleSheet("QTextEdit {color:green}")

    #function to directly close App 
    def closeApp(self):
        print "Cancel pressed"
        app.exit()


    #function to start game in 5sec

    def tick(self):
        print "self"
        print "tick"


"""    def text_changed(self):
        self.editPara.setReadOnly(True)
        mytext = self.editPara.toPlainText()
        l=len(mytext)
        if l==1:
            st = self.begin_time()
        k=len(self.st)
        print k
        print l
        if l <= k:
            if mytext == self.st[0:l]:
                print "match"
                self.editPara.setStyleSheet("QTextEdit {color:black}")
            else:
                self.editPara.setStyleSheet("QTextEdit {color:red}")
            if l <= k:
                self.editPara.setReadOnly(False)
        else:
            self.final_time(k)
            
    def begin_time(self):
        start_time = time()
        print start_time
        return start_time

    def final_time(self, k):
        end_time = time()
        #begin = self.begin_time()
        total_time = (end_time - begin)/60
        print total_time
        word_length = int(k/4)
        self.wpm(total_time, word_length)

    def wpm(self, t, l):
        t = round(t, 2)
        print t
        print l
        word_p_m = l/t
        print round(word_p_m, 2)"""

"""    def startIn(self):
        #ui = Ui_Form()
        print "not call startIn"
        #q = self.timer.q
        if q < 6:
            self.update_progressbar(q)
            print self
            print 'tick'
            q += 1
        else:
            self.editPara.setReadOnly(False)
            #return q

    #function to start game within timer
    def start_Timer(self):
        #timer = QTimer()
        #test = Ui_Form()
        #print timer
        #ui = Ui_Form()
        #print self
        global q
        q =0
        #self.startIn(q)
        #timer.timeout.connect(self.startIn)
        #timer.start(1000)
        #print "timer"
        #print timer.isActive()"""

if __name__ == "__main__":
    ui = Ui_Form()

"""def practice_session(self):
                import sys
                from PyQt4.QtCore 
                app = QtGui.QApplication(sys.argv)
                Form = QtGui.QWidget()
                ui = Ui_Form()
    self.setupUi(Form)
    Form.show()
                #set timer
    timer = QTimer()
    timer.q = 0
    timer.timeout.connect(self.startIn)
    timer.start(1000)
         
                #sys.exit(app.exec_())"""