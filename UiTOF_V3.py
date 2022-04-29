from PyQt5 import QtWidgets, uic, QtCore
import sys, os, glob, json


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()      # Call the inherited classes __init__ method
        uic.loadUi('UiTOF.ui', self)    # Load the .ui file
        self.searchB.clicked.connect(self.click_s)
        self.exeB.clicked.connect(self.exe)
        self.scrfold = ("/home/mgiacalo/GitHub/","/home/mgiacalo/alice/alidist/")
        self.diction = {}
        paths, names = self.getFiles()
        dictL = {names[i]: paths[i] for i in range(len(paths))}
        self.setupDict(dictL)
        names.sort()
        self.fillCombo(names)

        self.show()                     # Show the GUI
    
    def fillCombo(self, fill):
        self.comboBox.addItems(fill)    

    def click_s(self):
        index = self.comboBox.findText(self.lsearch.text(), QtCore.Qt.MatchFixedString|QtCore.Qt.MatchContains)
        if index != -1:
            self.comboBox.setCurrentIndex(index)
        else: 
            self.lsearch.setText("Not FOUND")     

    def setupDict(self, Dict):
        self.diction = Dict

    def exe(self):
        print(self.diction[self.comboBox.currentText()]) 

    def getFiles(self):
        paths = []
        names = []
        for fol in self.scrfold:
            os.chdir(fol)
            for file in glob.glob("*.sh"):
                paths.append(fol + file)
                names.append(file)      
        return paths, names                         

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()   