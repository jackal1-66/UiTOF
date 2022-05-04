from PyQt5 import QtWidgets, uic, QtCore, QtGui
import sys, json, os, glob


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()      # Call the inherited classes __init__ method
        uic.loadUi('UiTOF.ui', self)    # Load the .ui file
        self.setWindowIcon(QtGui.QIcon('ALICE.png'))
        self.setWindowTitle("WeTOF")

        self.searchB.clicked.connect(self.click_s)
        self.exeB.clicked.connect(self.exe)
        self.comboBox.currentIndexChanged.connect(self.changeBox)
        
        self.params = []
        
        with open("/home/mgiacalo/GitHub/UiTOF/programs.json", 'r') as fil:
            self.fildata = json.load(fil)
            for data in self.fildata:
                self.comboBox.addItem(data["name"])
            fil.close()    

        self.show()                     # Show the GUI

    def changeBox(self):
        helpline = self.fildata[self.comboBox.currentIndex()]["help"]        
        self.helptxt.clear()
        self.helptxt.append(helpline)
        self.helptxt.append("Location: " + self.fildata[self.comboBox.currentIndex()]["folder"])

    def click_s(self):
        index = self.comboBox.findText(self.lsearch.text(), QtCore.Qt.MatchFixedString|QtCore.Qt.MatchContains)
        if index != -1:
            self.comboBox.setCurrentIndex(index)
        else: 
            self.lsearch.setText("Not FOUND")     

    def exe(self):
        #print(self.fildata[self.comboBox.currentIndex()]["folder"])  
        self.process = QtCore.QProcess(self)
        hold = self.fildata[self.comboBox.currentIndex()]["hold"]
        if hold == False:
            if self.par.text():
                self.params = self.par.text().split()
                #print(self.params)   
            else:
                self.params = []       
            self.process.readyReadStandardOutput.connect(self.handle_stdout)
            self.process.readyReadStandardError.connect(self.handle_stderr)
            prog = self.fildata[self.comboBox.currentIndex()]["folder"]
            if ".sh" in prog:
                self.params.insert(0,prog)             
                self.process.start("/bin/sh", self.params)
            else:
                self.process.start(prog, self.params)
        else:
            prog = self.fildata[self.comboBox.currentIndex()]["folder"]
            self.params = ["-hold", "-e", prog]
            if self.par.text():
                self.params.append(self.par.text().split())
            self.process.start("xterm", self.params)    
                                

    def handle_stderr(self):
        data = self.process.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        if stderr:
            print(stderr)

    def handle_stdout(self):
        data = self.process.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        if stdout:
            print(stdout)          

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()   