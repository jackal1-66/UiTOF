# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UiTOF.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 220)
        MainWindow.setStatusTip("")
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(190, 0, 221, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 10, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.helptxt = QtWidgets.QTextBrowser(self.frame)
        self.helptxt.setGeometry(QtCore.QRect(0, 50, 221, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.helptxt.setFont(font)
        self.helptxt.setObjectName("helptxt")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(10, 0, 181, 211))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(0, 70, 181, 23))
        self.comboBox.setObjectName("comboBox")
        self.par = QtWidgets.QLineEdit(self.frame_2)
        self.par.setGeometry(QtCore.QRect(0, 140, 181, 23))
        self.par.setText("")
        self.par.setObjectName("par")
        self.exeB = QtWidgets.QPushButton(self.frame_2)
        self.exeB.setGeometry(QtCore.QRect(50, 170, 80, 41))
        self.exeB.setObjectName("exeB")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLineWidth(0)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lsearch = QtWidgets.QLineEdit(self.frame_2)
        self.lsearch.setGeometry(QtCore.QRect(0, 50, 131, 21))
        self.lsearch.setObjectName("lsearch")
        self.searchB = QtWidgets.QPushButton(self.frame_2)
        self.searchB.setGeometry(QtCore.QRect(130, 50, 51, 21))
        self.searchB.setObjectName("searchB")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Help"))
        self.exeB.setText(_translate("MainWindow", "Execute"))
        self.label.setText(_translate("MainWindow", "Scripts"))
        self.label_3.setText(_translate("MainWindow", "Parameters"))
        self.lsearch.setText(_translate("MainWindow", "Text search"))
        self.searchB.setText(_translate("MainWindow", "Search"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
