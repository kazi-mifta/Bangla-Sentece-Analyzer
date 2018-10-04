# ->TODO: Design the Database Pattern so data can be fetched quickly 


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QPlainTextEdit,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import yaml
 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'NLP Analysis'
        self.left = 50
        self.top = 50
        self.width = 600
        self.height = 640
        self.initUI()
 
    #User Interface Design Code
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create inputBox
        self.inputBox = QLineEdit(self)
        self.inputBox.move(20, 20)
        self.inputBox.setPlaceholderText("Input Sentence")
        self.inputBox.resize(280,30)

        # Create pofBox where the Part Of Speech Analysis Will Be Shown
        self.pofBox = QPlainTextEdit(self)
        self.pofBox.move(20, 70)
        self.pofBox.setPlaceholderText("Parts Of Speech Extraction")
        self.pofBox.resize(280,100)
 
        # Create sentenceTypeBox
        self.stPatternBox = QLineEdit(self)
        self.stPatternBox.move(20, 190)
        self.stPatternBox.setPlaceholderText("Sentence Pattern")
        self.stPatternBox.resize(280,30)

        # Create sentence Category Box
        self.stCtgryBox = QLineEdit(self)
        self.stCtgryBox.move(20, 250)
        self.stCtgryBox.setPlaceholderText("Sentence Category")
        self.stCtgryBox.resize(280,30)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,600)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.setFocus()
        self.show()

    @pyqtSlot()
    def on_click(self):
        #Openning YAML Database file and for Parsing, opening  parts of speech database and Pattern Database
        with open("pofData.yaml",'r',encoding = 'utf-8') as streamA, open("patternData.yaml",'r',encoding = 'utf-8') as streamB:
            pofData = yaml.load(streamA)
            patternData = yaml.load(streamB)

        #Variable for parts of Speech box
        pofString = ""
        #Variable for pattern, it will be used to search pattern Database
        patternStr =""
        #This is a list, it will be shown on Pattern Box 
        pattern = [] 

        #value fetched from input Box and split into an Array
        inputSentence = self.inputBox.text()
        inputWord = inputSentence.split()

        #Checking The parts of speech Database and Building the pattern
        for words in inputWord:
            item = pofData.get(words,"NULL")
            #String for the parts of Speech Box
            pofString += words +" : "+ item + "\n"
            #String For querying from Pattern Database
            patternStr += item
            #String for the Sentence Pattern Box
            pattern.append(item)

        #Setting text of Parts of Speech Box
        self.pofBox.setPlainText(pofString)

        #Joining the List Items with a '+' sign in it
        self.stPatternBox.setText('+ '.join(pattern))
        
        #Getting a value from Pattern Database, 
        #if a positive match then show result
        patternBase = patternData.get(patternStr)
        if(patternBase):
            self.stCtgryBox.setText(patternBase)
        else:          
            self.stCtgryBox.setText("NULL")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())