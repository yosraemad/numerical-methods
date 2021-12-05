from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from submit import Submit
import ctypes


class Ui_MainWindow(object):
    def submit(self):
        if(self.functionEntry.text() == ''):
                ctypes.windll.user32.MessageBoxW(0, "Please enter a function", "Error", 0)
                return
        if(self.precisionEntry.text() == ''):
                self.precisionEntry.setText("0.01")
        if(self.numberOfIterationsEntry.text() == ''):
                self.numberOfIterationsEntry.setText("20")
        if(self.initialGuess1Entry.text() == ''):
                ctypes.windll.user32.MessageBoxW(0, "Please enter the initial guess", "Error", 0)
                return
        if(self.methodComboBox.currentText() != "Newton Raphson" and self.initialGuess2Entry.text() == ''):
                ctypes.windll.user32.MessageBoxW(0, "Please enter the second initial guess", "Error", 0)
                return
        submit = Submit(self.functionEntry.text(), str(self.methodComboBox.currentText()), float(self.precisionEntry.text()), int(self.numberOfIterationsEntry.text()), self.initialGuess1Entry.text(), self.initialGuess2Entry.text())

    def read_from_file(self, MainWindow):
        filename = QFileDialog.getOpenFileName(self.centralwidget, 'Open file')
        if(filename[0] != ''):
            with open(filename[0], 'r') as f:
                self.functionEntry.setText(f.read())


    def setupInitialGuessLabels(self):
        self.initialGuess2Entry.show()
        if(self.methodComboBox.currentText() == "Fixed Point"):
            self.initialGuess1Label.setText("Initial Guess:")
            self.initialGuess2Label.setText("g(x)")
        elif(self.methodComboBox.currentText() == "Newton Raphson"):
            self.initialGuess1Label.setText("Initial Guess:")
            self.initialGuess2Label.setText("")
            self.initialGuess2Entry.hide()
        elif(self.methodComboBox.currentText() == "Secant"):
            self.initialGuess1Label.setText("x_(i-1):")
            self.initialGuess2Label.setText("x_i:")
        else:
            self.initialGuess1Label.setText("Initial Guess 1:")
            self.initialGuess2Label.setText("Initial Guess 2:")
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(238, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enterAFunctionLabel = QtWidgets.QLabel(self.centralwidget)
        self.enterAFunctionLabel.setGeometry(QtCore.QRect(50, 140, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.enterAFunctionLabel.setFont(font)
        self.enterAFunctionLabel.setStyleSheet("background: none;")
        self.enterAFunctionLabel.setObjectName("enterAFunctionLabel")
        self.functionEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.functionEntry.setGeometry(QtCore.QRect(180, 130, 211, 31))
        self.functionEntry.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;\n"
"background: none;")
        self.functionEntry.setText("")
        self.functionEntry.setObjectName("functionEntry")
        self.chooseFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.chooseFileButton.setGeometry(QtCore.QRect(410, 130, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chooseFileButton.setFont(font)
        self.chooseFileButton.setAcceptDrops(False)
        self.chooseFileButton.setStyleSheet("border-radius: 10px;\n"
"border: 1px solid black;\n"
"background: none;")
        self.chooseFileButton.setObjectName("chooseFileButton")
        self.chooseMethodLabel = QtWidgets.QLabel(self.centralwidget)
        self.chooseMethodLabel.setGeometry(QtCore.QRect(50, 200, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.chooseMethodLabel.setFont(font)
        self.chooseMethodLabel.setStyleSheet("background: none;")
        self.chooseMethodLabel.setObjectName("chooseMethodLabel")
        self.methodComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.methodComboBox.setGeometry(QtCore.QRect(180, 190, 211, 31))
        self.methodComboBox.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;\n"
"background: none;")
        self.methodComboBox.setObjectName("methodComboBox")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.methodComboBox.addItem("")
        self.precisionLabel = QtWidgets.QLabel(self.centralwidget)
        self.precisionLabel.setGeometry(QtCore.QRect(50, 260, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.precisionLabel.setFont(font)
        self.precisionLabel.setStyleSheet("background: none;")
        self.precisionLabel.setObjectName("precisionLabel")
        self.precisionEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.precisionEntry.setGeometry(QtCore.QRect(150, 250, 141, 31))
        self.precisionEntry.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;\n"
"background: none;")
        self.precisionEntry.setObjectName("precisionEntry")
        self.defaultPrecisionLabel = QtWidgets.QLabel(self.centralwidget)
        self.defaultPrecisionLabel.setGeometry(QtCore.QRect(220, 280, 81, 16))
        self.defaultPrecisionLabel.setStyleSheet("color: rgb(138, 134, 255);\n"
"background: none;")
        self.defaultPrecisionLabel.setObjectName("defaultPrecisionLabel")
        self.defaultIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.defaultIterationsLabel.setGeometry(QtCore.QRect(670, 280, 81, 16))
        self.defaultIterationsLabel.setStyleSheet("color: rgb(138, 134, 255);\n"
"background: none;")
        self.defaultIterationsLabel.setObjectName("defaultIterationsLabel")
        self.numberOfIterationsEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.numberOfIterationsEntry.setGeometry(QtCore.QRect(590, 250, 141, 31))
        self.numberOfIterationsEntry.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;\n"
"background: none;")
        self.numberOfIterationsEntry.setObjectName("numberOfIterationsEntry")
        self.numberOfIterationsLabel = QtWidgets.QLabel(self.centralwidget)
        self.numberOfIterationsLabel.setGeometry(QtCore.QRect(440, 260, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.numberOfIterationsLabel.setFont(font)
        self.numberOfIterationsLabel.setStyleSheet("background: none;")
        self.numberOfIterationsLabel.setObjectName("numberOfIterationsLabel")
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(270, 390, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.submitButton.setFont(font)
        self.submitButton.setStyleSheet("border: 1px solid black;\n"
"border-radius: 25px;\n"
"background-color: rgb(138, 134, 255);\n"
"color: white;")
        self.submitButton.setObjectName("submitButton")
        self.initialGuess2Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.initialGuess2Entry.setGeometry(QtCore.QRect(590, 310, 141, 31))
        self.initialGuess2Entry.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;\n"
"background: none;")
        self.initialGuess2Entry.setObjectName("initialGuess2Entry")
        self.initialGuess1Entry = QtWidgets.QLineEdit(self.centralwidget)
        self.initialGuess1Entry.setGeometry(QtCore.QRect(150, 310, 141, 31))
        self.initialGuess1Entry.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;\n"
"background: none;")
        self.initialGuess1Entry.setObjectName("initialGuess1Entry")
        self.initialGuess1Label = QtWidgets.QLabel(self.centralwidget)
        self.initialGuess1Label.setGeometry(QtCore.QRect(50, 320, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.initialGuess1Label.setFont(font)
        self.initialGuess1Label.setStyleSheet("background: none;")
        self.initialGuess1Label.setObjectName("initialGuess1Label")
        self.initialGuess2Label = QtWidgets.QLabel(self.centralwidget)
        self.initialGuess2Label.setGeometry(QtCore.QRect(480, 320, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.initialGuess2Label.setFont(font)
        self.initialGuess2Label.setStyleSheet("background: none;")
        self.initialGuess2Label.setObjectName("initialGuess2Label")
        self.background = QtWidgets.QGraphicsView(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(30, 50, 741, 431))
        self.background.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.943, y2:0.960227, stop:0 rgba(255, 255, 255, 200), stop:1 rgba(255, 255, 255, 100));\n"
"border: 1px solid white;")
        self.background.setInteractive(False)
        self.background.setObjectName("background")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 410, 121, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setStyleSheet("background: orange;\n"
"border-radius:60px;\n"
"border: none;")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.background.raise_()
        self.initialGuess2Label.raise_()
        self.initialGuess1Label.raise_()
        self.defaultPrecisionLabel.raise_()
        self.enterAFunctionLabel.raise_()
        self.functionEntry.raise_()
        self.chooseFileButton.raise_()
        self.chooseMethodLabel.raise_()
        self.methodComboBox.raise_()
        self.precisionLabel.raise_()
        self.precisionEntry.raise_()
        self.defaultIterationsLabel.raise_()
        self.numberOfIterationsEntry.raise_()
        self.numberOfIterationsLabel.raise_()
        self.submitButton.raise_()
        self.initialGuess2Entry.raise_()
        self.initialGuess1Entry.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submitButton.clicked.connect(self.submit)
        self.chooseFileButton.clicked.connect(self.read_from_file)
        self.methodComboBox.currentIndexChanged.connect(self.setupInitialGuessLabels)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Numerical Methods"))
        self.enterAFunctionLabel.setText(_translate("MainWindow", "Enter a function:"))
        self.chooseFileButton.setText(_translate("MainWindow", "Choose a file"))
        self.chooseMethodLabel.setText(_translate("MainWindow", "Choose a Method:"))
        self.methodComboBox.setItemText(0, _translate("MainWindow", "Bisection"))
        self.methodComboBox.setItemText(1, _translate("MainWindow", "False Position"))
        self.methodComboBox.setItemText(2, _translate("MainWindow", "Fixed Point"))
        self.methodComboBox.setItemText(3, _translate("MainWindow", "Newton Raphson"))
        self.methodComboBox.setItemText(4, _translate("MainWindow", "Secant"))
        self.precisionLabel.setText(_translate("MainWindow", "Precision:"))
        self.precisionEntry.setPlaceholderText(_translate("MainWindow", "0.0"))
        self.defaultPrecisionLabel.setText(_translate("MainWindow", "default is 0.01"))
        self.defaultIterationsLabel.setText(_translate("MainWindow", "default is 20"))
        self.numberOfIterationsEntry.setPlaceholderText(_translate("MainWindow", "0"))
        self.numberOfIterationsLabel.setText(_translate("MainWindow", "Max. No. of Iterations:"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
        self.initialGuess2Entry.setPlaceholderText(_translate("MainWindow", "0.0"))
        self.initialGuess1Entry.setPlaceholderText(_translate("MainWindow", "0.0"))
        self.initialGuess1Label.setText(_translate("MainWindow", "Initial Guess 1:"))
        self.initialGuess2Label.setText(_translate("MainWindow", "Initial Guess 2:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
